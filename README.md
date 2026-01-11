# QR Code Generator

Generate print-ready QR codes at 2cm x 2cm size (300 DPI).

## Features

- Creates QR codes optimized for printing
- Configurable module (dot) size
- Outputs PNG at 300 DPI for print quality
- Error correction for damaged code scanning

## Usage

```bash
python create_qr_code.py "text to encode" 10
```

Arguments:
- `text` - The text or URL to encode
- `module_size` - Size of each QR module in pixels

## Example

```bash
# Create QR code for a URL
python create_qr_code.py "https://example.com" 10

# Output: qrcode.png (2cm x 2cm at 300 DPI)
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install qrcode Pillow
```

## Requirements

- Python 3.x
- qrcode
- Pillow
