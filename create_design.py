from PIL import Image, ImageDraw, ImageFont
import os

# --------------------------------------------------
# CREATE TRAVEL DESIGN
# --------------------------------------------------

# Project folder
BASE_DIR = r"C:\Users\User\Desktop\Canva_Image_Replacement"

# Output folder
DESIGN_FOLDER = os.path.join(BASE_DIR, "designs")

# Create designs folder if it doesn't exist
os.makedirs(DESIGN_FOLDER, exist_ok=True)

# --------------------------------------------------
# CREATE CANVAS
# --------------------------------------------------

width = 1000
height = 650

# Create white background
image = Image.new("RGB", (width, height), "white")

draw = ImageDraw.Draw(image)

# --------------------------------------------------
# ADD TITLE
# --------------------------------------------------

try:
    title_font = ImageFont.truetype("arial.ttf", 50)
except:
    title_font = ImageFont.load_default()

title = "TRAVEL ADVENTURE"

# Get title size
bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = bbox[2] - bbox[0]

# Center title
title_x = (width - title_width) // 2

draw.text(
    (title_x, 60),
    title,
    fill="black",
    font=title_font
)

# --------------------------------------------------
# REPLACEABLE IMAGE AREA
# --------------------------------------------------

x1 = 250
y1 = 150
x2 = 750
y2 = 500

# Draw placeholder rectangle
draw.rectangle(
    (x1, y1, x2, y2),
    outline="black",
    width=4
)

# --------------------------------------------------
# PLACEHOLDER TEXT
# --------------------------------------------------

try:
    placeholder_font = ImageFont.truetype("arial.ttf", 30)
except:
    placeholder_font = ImageFont.load_default()

text = "REPLACEABLE IMAGE AREA"

bbox = draw.textbbox(
    (0, 0),
    text,
    font=placeholder_font
)

text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

text_x = x1 + (x2 - x1 - text_width) // 2
text_y = y1 + (y2 - y1 - text_height) // 2

draw.text(
    (text_x, text_y),
    text,
    fill="black",
    font=placeholder_font
)

# --------------------------------------------------
# SAVE DESIGN
# --------------------------------------------------

output_path = os.path.join(
    DESIGN_FOLDER,
    "design_01_travel.png"
)

image.save(output_path)

print("Design created successfully!")
print()
print("Saved at:")
print(output_path)

print()
print("Replaceable image area:")
print("x1 =", x1)
print("y1 =", y1)
print("x2 =", x2)
print("y2 =", y2)