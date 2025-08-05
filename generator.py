import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Load Excel file with correct column names
excel_path = 'hackathon_teams.xlsx'
df = pd.read_excel(excel_path, engine='openpyxl')

# Ensure output base directory exists
output_dir = 'output/IDCARDS'
os.makedirs(output_dir, exist_ok=True)
qr_dir = 'Unique Code'  # Path to QR codes

# Choose fonts (update with correct TTF path for your system)
font_path = 'arial.ttf'    # Or use any other supported TTF
font_regular = ImageFont.truetype(font_path, 28)
font_college = ImageFont.truetype(font_path, 25)

# All member tuples (label, unique code column, usn column)
members = [
    ("Leader Name", "Leader Unique Code", "Leader USN"),
    ("Member 2 Name", "Member 2 Unique Code", "Member 2 USN"),
    ("Member 3 Name", "Member 3 Unique Code", "Member 3 USN"),
    ("Member 4 Name", "Member 4 Unique Code", "Member 4 USN"),
]

for idx, row in df.iterrows():

    for name_col, code_col, usn_col in members:
        member_name = str(row.get(name_col, '')).strip()
        unique_code = str(row.get(code_col, '')).strip()
        member_usn = str(row.get(usn_col, '')).strip()

        if not unique_code or unique_code.lower() == 'nan':
            continue  # Skip if code is missing

        # Open the template and prepare to draw
        card = Image.open('idcard_template.jpg').convert('RGBA')
        draw = ImageDraw.Draw(card)
        draw.text((188, 395), member_name, font=font_regular, fill="black")
        draw.text((167, 465), member_usn, font=font_regular, fill="black")
        draw.text((190, 545), str(row['College']), font=font_college, fill="black")
        draw.text((165, 620), str(row['Team Name']), font=font_regular, fill="black")

        # Paste the QR at the specified coordinates, if it exists
        qr_path = os.path.join(qr_dir, f'{unique_code}.png')
        if os.path.exists(qr_path):
            qr_img = Image.open(qr_path).convert("RGBA")
            qr_img = qr_img.resize((200, 200), Image.LANCZOS)
            card.paste(qr_img, (40, 670), qr_img)
            # Print the unique code below the QR code image
            draw.text((56, 855), unique_code, font=font_regular, fill="black")
        else:
            print(f"Warning: QR code not found for {unique_code} at {qr_path}")

        # Save card directly in output_dir, named by Unique Code
        save_path = os.path.join(output_dir, f"{unique_code}.png")
        card.save(save_path)

print("All ID cards with integrated QR codes generated and saved in subfolders of Output- IDCARDS.")
