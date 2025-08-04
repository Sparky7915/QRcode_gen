import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Read data from Excel
df = pd.read_excel("student_teams.xlsx")

# Load fonts
font_regular = ImageFont.truetype("arial.ttf", 28)  # Regular
font_college = ImageFont.truetype("arial.ttf", 25)  # for college name

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

for idx, row in df.iterrows():
    # Load and prepare the template
    card = Image.open("idcard_template.jpg").convert("RGBA")
    draw = ImageDraw.Draw(card)

    # Coordinates
    
    x_name = 188
    y_name = 395
    
    x_usn = 167
    y_usn = 465
    
    x_college = 190
    y_college = 545
    
    x_team = 165
    y_team = 620

    # Text color
    text_color = "black"

    # Draw Name
    draw.text((x_name, y_name), str(row['Name']), font=font_regular, fill=text_color, )

    # Draw USN
    draw.text((x_usn, y_usn), str(row['USN']), font=font_regular, fill=text_color)

    # Draw College
    draw.text((x_college, y_college), str(row['College']), font=font_college, fill=text_color)

    # Draw Team Name
    draw.text((x_team, y_team), str(row['Team Name']), font=font_regular, fill=text_color)

    # Save the card
    filename = f"output/ID_{row['USN']}.png"
    card.save(filename)

print("All ID cards with white text generated successfully.")
