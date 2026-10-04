from PIL import Image, ImageDraw, ImageFont
import os

# --------------------------------------------------
# CREATE DESIGNS FOLDER
# --------------------------------------------------

os.makedirs("designs", exist_ok=True)


# --------------------------------------------------
# FUNCTION TO CREATE A DESIGN
# --------------------------------------------------

def create_design(title, subtitle, filename):

    width = 1080
    height = 1080

    # Create white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # --------------------------------------------------
    # LOAD FONTS
    # --------------------------------------------------

    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        subtitle_font = ImageFont.truetype("arial.ttf", 32)
        area_font = ImageFont.truetype("arial.ttf", 40)

    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        area_font = ImageFont.load_default()

    # --------------------------------------------------
    # TITLE
    # --------------------------------------------------

    draw.text(
        (width // 2, 80),
        title,
        fill="black",
        anchor="mm",
        font=title_font
    )

    # --------------------------------------------------
    # IMAGE AREA
    # --------------------------------------------------

    x1 = 150
    y1 = 220
    x2 = 930
    y2 = 700

    # Draw image placeholder
    draw.rectangle(
        [x1, y1, x2, y2],
        outline="black",
        width=5
    )

    # Image area text
    draw.text(
        ((x1 + x2) // 2, (y1 + y2) // 2),
        "IMAGE AREA",
        fill="gray",
        anchor="mm",
        font=area_font
    )

    # --------------------------------------------------
    # SUBTITLE
    # --------------------------------------------------

    draw.text(
        (width // 2, 800),
        subtitle,
        fill="black",
        anchor="mm",
        font=subtitle_font
    )

    # --------------------------------------------------
    # SAVE DESIGN
    # --------------------------------------------------

    image.save(filename)

    print("Created:", filename)


# ==================================================
# CREATE 5 CANVA-STYLE DESIGNS
# ==================================================

# 1. Travel Design
create_design(
    "TRAVEL ADVENTURE",
    "Explore Beautiful Destinations",
    "designs/travel_design.png"
)


# 2. Technology Design
create_design(
    "SMART TECHNOLOGY",
    "Modern Digital Solutions",
    "designs/technology_design.png"
)


# 3. Coffee Design
create_design(
    "COFFEE TIME",
    "Enjoy Every Sip",
    "designs/coffee_design.png"
)


# 4. Product Design
create_design(
    "NEW PRODUCT",
    "Discover Innovation",
    "designs/product_design.png"
)


# 5. Flower Design
create_design(
    "FLOWER BEAUTY",
    "Beautiful Flowers for Every Moment",
    "designs/flower_design.png"
)


# ==================================================
# COMPLETION MESSAGE
# ==================================================

print()
print("======================================")
print("All 5 designs created successfully!")
print("======================================")