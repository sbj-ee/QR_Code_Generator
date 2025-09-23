import qrcode
import argparse
from PIL import Image

def create_qr_code(text, module_size):
    # Calculate pixels for 2cm x 2cm at 300 DPI (standard for printing)
    cm_to_pixels = 300 / 2.54  # 300 DPI / 2.54 cm per inch
    target_size = int(2 * cm_to_pixels)  # 2cm in pixels

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=module_size,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Resize image to 2cm x 2cm
    img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
    img.save("qrcode.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a 2cm x 2cm QR code from text")
    parser.add_argument("text", type=str, help="Text to encode in QR code")
    parser.add_argument("module_size", type=int, help="Size of each QR code module in pixels")
    args = parser.parse_args()
    create_qr_code(args.text, args.module_size)
