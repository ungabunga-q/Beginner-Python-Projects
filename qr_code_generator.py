"""
QR Code Generator
Generates a QR code for a given text (requires 'qrcode' library).
"""
import qrcode

def generate_qr(text):
    img = qrcode.make(text)
    img.save("qrcode.png")
    print("QR code saved as qrcode.png")

if __name__ == "__main__":
    text = input("Enter text for QR code: ")
    generate_qr(text)
