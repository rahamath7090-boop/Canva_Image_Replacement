from PIL import Image
import os


def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return image


def get_image_files(folder):
    extensions = (".jpg", ".jpeg", ".png", ".webp")

    image_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):
                image_files.append(os.path.join(root, file))

    return image_files