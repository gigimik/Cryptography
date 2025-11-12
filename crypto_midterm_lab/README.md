# Applied Cryptography – Midterm Lab (Weeks 1–4)
**Author:** Grigol Mikadze  
**Environment:** Python 3.13.2  |  OpenSSL (Git Bash on Windows 11)

---

##  Overview
This repository documents the entire Applied Cryptography midterm lab (Weeks 1–4).  
It demonstrates AES encryption/decryption, ECC key signing, SHA-256 & HMAC hashing,  
and a Diffie-Hellman key-exchange simulation in Python.

>  **Tip:** Keep terminal outputs and screenshots in your GitHub submission.

---

##  Files
- `secret.txt` – input for AES encryption  
- `ecc.txt` – input for ECC signing  
- `data.txt` – input for SHA-256 and HMAC  
- `data_modified.txt` – modified version used in Task 3C  
- `task3_results.txt`, `task3_outputs.json` – Python outputs for Task 3  
- `task4_results.txt` – Python DH simulation results  
- `lab.sh` – Bash script with OpenSSL commands for Tasks 1–3  
- `hash_hmac_dh.py` – Python script for Tasks 3 & 4  

---

##  How to Run

### Prerequisites
- **OpenSSL 1.1+**
- **Python 3.9+** (recommended 3.13)

###  Run Python Script (Tasks 3 & 4)
Computes hashes/HMAC and simulates Diffie-Hellman.
```bash
python3 hash_hmac_dh.py
