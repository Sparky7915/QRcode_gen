import qrcode
from PIL import Image
import pandas as pd

# Load Excel file
df = pd.read_excel("student_teams_with_codes.xlsx", engine="openpyxl")

# Change 'Unique Code' to the actual column name if different
unique_codes = df["Unique Code"].astype(str).tolist()

logo = Image.open("logo.jpg")
box_size = 80  # Adjust as needed
logo = logo.resize((box_size, box_size), Image.LANCZOS)

import os

output_dir = "qrcode"
os.makedirs(output_dir, exist_ok=True)

for code in unique_codes:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    pos = ((img.size[0] - box_size) // 2, (img.size[1] - box_size) // 2)
    img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
    output_path = os.path.join(output_dir, f"{code}_with_logo.png")
    img.save(output_path)
    print(f"QR code with logo generated and saved as '{output_path}'.")