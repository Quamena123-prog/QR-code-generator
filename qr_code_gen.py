import qrcode
import qrcode.constants

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000")
    img.save(file_name)

# Input text to generate QR code for
text = "https://example.com"
# File name to save QR code image
file_name = "qr_code.png"

# Generate QR code
generate_qr_code(text, file_name)
print(f"QR code was saved as {file_name}")
