import qrcode
import argparse

def create_qr_code(text, size):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code from text")
    parser.add_argument("text", type=str, help="Text to encode in QR code")
    parser.add_argument("size", type=int, help="Size of each QR code module in pixels")
    args = parser.parse_args()
    create_qr_code(args.text, args.size)
