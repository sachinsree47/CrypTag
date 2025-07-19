import qrcode
import uuid
from PIL import Image
from pyzbar.pyzbar import decode

def generate_qr(data):
    qr = qrcode.make(data)
    filename = f"static/{uuid.uuid4().hex}.png"
    qr.save(filename)
    return filename

def decode_qr(image_path):
    image = Image.open(image_path)
    decoded_objs = decode(image)
    if decoded_objs:
        return decoded_objs[0].data.decode('utf-8')
    else:
        return "Could not decode QR"
