from flask import Flask, render_template, request
from utils.crypto import encrypt_message, decrypt_message
from utils.qr_tools import generate_qr, decode_qr
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt')
def encrypt_page():
    return render_template('encrypt.html')

@app.route('/decrypt')
def decrypt_page():
    return render_template('decrypt.html')


@app.route('/generate', methods=['POST'])
def generate():
    message = request.form['message']
    password = request.form['password']
    
    # Encrypt the message
    encrypted = encrypt_message(message, password)
    
    # Generate QR code with encrypted data
    qr_path = generate_qr(encrypted)
    
    return render_template('result.html', qr_path=qr_path)

@app.route('/decode', methods=['POST'])
def decode():
    file = request.files['qrfile']
    password = request.form['password']
    
    # Save uploaded QR file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Decode QR and decrypt message
    encrypted_data = decode_qr(filepath)
    try:
        decrypted = decrypt_message(encrypted_data, password)
    except Exception:
        decrypted = "Invalid password or QR content!"
    
    return render_template('result.html', decrypted=decrypted)

# ✅ This part runs the app!
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
