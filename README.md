# 🏦 Quantum Fraud Prevention System (Tkinter)

## 📌 Project Overview
This project simulates a **Quantum Secure Banking System** that detects fraud using **Quantum Key Distribution (QKD)**.  
It demonstrates how quantum communication can secure banking transactions and detect eavesdropping through **Quantum Bit Error Rate (QBER)**.

The system is implemented as a **desktop GUI application using Tkinter** and quantum circuits simulated with **Qiskit**.

---

## ⚛ Key Concept
The project is based on the **BB84 Quantum Key Distribution Protocol**.

Process:
1. Bank encodes secret bits into qubits  
2. Customer measures qubits in random bases  
3. Matching bases generate a shared secret key  
4. If an attacker intercepts the qubits, the quantum state changes  
5. Increased QBER indicates possible fraud

---

## 🚀 Features
- Secure banking transaction simulation  
- Quantum fraud detection using QBER  
- Attacker (Eve) simulation  
- Secret key generation  
- Transaction approval or fraud detection  
- Desktop GUI interface using Tkinter  

---

## ⚙ Technologies Used
- Python  
- Tkinter  
- Qiskit  
- Qiskit Aer Simulator  

---

## ▶ How to Run

### Install dependencies:

pip install qiskit qiskit-aer
### Run the application:

python Quantum Fraud Prevention Using QKD in Tkinter.py
### Output  

The system displays:

 - Generated secret quantum key

 - Quantum Bit Error Rate (QBER)

 - Transaction status (Approved / Fraud Detected)


