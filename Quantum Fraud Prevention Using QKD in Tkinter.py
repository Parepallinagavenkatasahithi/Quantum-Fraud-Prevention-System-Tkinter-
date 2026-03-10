import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer


# =========================
# Quantum Simulation Logic
# =========================
def quantum_fraud_prevention(num_qubits=25, attacker=False):

    backend = Aer.get_backend("aer_simulator")

    bank_bits = [random.randint(0, 1) for _ in range(num_qubits)]
    bank_bases = [random.choice(['Z', 'X']) for _ in range(num_qubits)]
    customer_bases = [random.choice(['Z', 'X']) for _ in range(num_qubits)]

    customer_results = []

    for i in range(num_qubits):

        qc = QuantumCircuit(1, 1)

        # Bank encoding
        if bank_bits[i] == 1:
            qc.x(0)
        if bank_bases[i] == 'X':
            qc.h(0)

        # -------- Attacker (Eve) --------
        if attacker:
            eve_basis = random.choice(['Z', 'X'])
            if eve_basis == 'X':
                qc.h(0)
            qc.measure(0, 0)
            qc.reset(0)

            compiled = transpile(qc, backend)
            result = backend.run(compiled, shots=1).result()
            measured_bit = int(list(result.get_counts().keys())[0])

            if measured_bit == 1:
                qc.x(0)

        # Customer measurement
        if customer_bases[i] == 'X':
            qc.h(0)

        qc.measure(0, 0)

        compiled = transpile(qc, backend)
        result = backend.run(compiled, shots=1).result()
        measured_bit = int(list(result.get_counts().keys())[0])
        customer_results.append(measured_bit)

    # QBER Calculation
    matched = 0
    error_count = 0
    secret_key = []

    for i in range(num_qubits):
        if bank_bases[i] == customer_bases[i]:
            matched += 1
            secret_key.append(bank_bits[i])
            if bank_bits[i] != customer_results[i]:
                error_count += 1

    qber = error_count / matched if matched > 0 else 0

    return secret_key, qber


# =========================
# GUI Section
# =========================

def run_simulation():

    result_box.delete(1.0, tk.END)

    attacker_enabled = attacker_var.get()

    secret_key, qber = quantum_fraud_prevention(attacker=attacker_enabled)

    threshold = 0.20

    result_box.insert(tk.END, "🔐 Quantum Secure Banking System\n\n")
    result_box.insert(tk.END, f"Attacker Present: {attacker_enabled}\n\n")
    result_box.insert(tk.END, f"Generated Secret Key:\n{secret_key}\n\n")
    result_box.insert(tk.END, f"QBER: {round(qber,3)}\n\n")

    progress['value'] = qber * 100

    if qber < threshold:
        status_label.config(text="✔ TRANSACTION APPROVED",
                            fg="green")
        result_box.insert(tk.END, "STATUS: SECURE CHANNEL\n")
    else:
        status_label.config(text="✖ FRAUD DETECTED",
                            fg="red")
        result_box.insert(tk.END, "STATUS: SECURITY BREACH\n")


# =========================
# Main Window
# =========================

root = tk.Tk()
root.title("Quantum Fraud Prevention System")
root.geometry("900x650")
root.configure(bg="#eef3f9")

# -------- Header --------
header = tk.Label(root,
                  text="🏦 Quantum Banking Security System",
                  font=("Helvetica", 22, "bold"),
                  bg="#1f4e79",
                  fg="white",
                  pady=15)
header.pack(fill="x")

# -------- Controls Frame --------
control_frame = tk.Frame(root, bg="#eef3f9")
control_frame.pack(pady=20)

attacker_var = tk.BooleanVar()

attacker_checkbox = tk.Checkbutton(control_frame,
                                   text="Enable Attacker (Eve)",
                                   variable=attacker_var,
                                   font=("Arial", 12),
                                   bg="#eef3f9")
attacker_checkbox.grid(row=0, column=0, padx=20)

start_button = tk.Button(control_frame,
                         text="Start Secure Transaction",
                         command=run_simulation,
                         font=("Arial", 12, "bold"),
                         bg="#2e75b6",
                         fg="white",
                         width=25,
                         height=2)
start_button.grid(row=0, column=1, padx=20)

# -------- Status Label --------
status_label = tk.Label(root,
                        text="System Ready",
                        font=("Arial", 16, "bold"),
                        bg="#eef3f9")
status_label.pack(pady=10)

# -------- QBER Progress --------
progress_label = tk.Label(root,
                    text="QBER Level (%)",
                        font=("Arial", 12),
                        bg="#eef3f9")
progress_label.pack()

progress = ttk.Progressbar(root,
                        orient="horizontal",
                        length=400,
                        mode="determinate")
progress.pack(pady=10)

# -------- Result Box --------
result_box = scrolledtext.ScrolledText(root,
                                    width=100,
                                    height=20,
                                    font=("Courier", 10),
                                    bg="white")
result_box.pack(pady=20)

# -------- Footer --------
footer = tk.Label(root,
                text="Quantum Fraud Prevention Using QKD",
                font=("Arial", 10),
                bg="#1f4e79",
                fg="white",
                pady=5)
footer.pack(side="bottom", fill="x")

root.mainloop()