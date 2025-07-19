# CrypTag 🔐📲

**CrypTag** is a QR Code Encryption Tool built with Flask that lets you:
- Encrypt secret messages using AES encryption
- Convert encrypted data into QR codes
- Decode QR codes using a password to retrieve the original message

---

## 🚀 Features
- AES-256 Encryption using password
- QR Code Generation and Decoding
- Password-protected secure decryption
- Simple Flask-based Web UI

---

## 🛠️ Tech Stack
- Flask (Web App)
- PyCryptodome (AES Encryption)
- qrcode (QR Code Generator)
- pyzbar + opencv (QR Code Reader)
- HTML + CSS (Frontend)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/cryptag.git
cd cryptag
pip install -r requirements.txt
python app.py
