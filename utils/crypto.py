from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64

def derive_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()  # 32 bytes for AES-256

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_message(message, password):
    key = derive_key(password)
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(message)
    encrypted = cipher.encrypt(padded.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_message(encrypted_data, password):
    key = derive_key(password)
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(encrypted_data)
    decrypted = cipher.decrypt(decoded).decode('utf-8')
    return decrypted.strip()
