import os
import pandas as pd
import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    logo = Image.open(logo_path)
    qr_width, qr_height = img_qr.size
    logo_size = int(qr_width * 0.2)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    img_qr.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
    img_qr.save(save_path)

def main():
    excel_path = 'hackathon_teams.xlsx'
    logo_path = 'logo.jpg'
    output_folder = 'Unique Code'
    os.makedirs(output_folder, exist_ok=True)
    df = pd.read_excel(excel_path, engine='openpyxl')
    member_columns = ['Leader Unique Code', 'Member 2 Unique Code', 'Member 3 Unique Code', 'Member 4 Unique Code']
    for idx, row in df.iterrows():
        for col in member_columns:
            unique_code = str(row.get(col, '')).strip()
            if unique_code and unique_code.lower() != 'nan':
                save_path = os.path.join(output_folder, f"{unique_code}.png")
                generate_qr_with_logo(unique_code, logo_path, save_path)

if __name__ == "__main__":
    main()