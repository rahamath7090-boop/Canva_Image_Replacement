import os
import pickle
from feature_extractor import FeatureExtractor
from preprocessing import get_image_files


DATA_FOLDER = "data"
INDEX_FILE = "models/image_index.pkl"


extractor = FeatureExtractor()

image_files = get_image_files(DATA_FOLDER)

features = []
paths = []

print("Building image index...")

for i, image_path in enumerate(image_files):

    try:

        feature = extractor.extract(image_path)

        features.append(feature)
        paths.append(image_path)

        print(f"Processed {i + 1}/{len(image_files)}")

    except Exception as e:

        print("Error:", image_path, e)


index = {
    "features": features,
    "paths": paths
}


os.makedirs("models", exist_ok=True)

with open(INDEX_FILE, "wb") as f:
    pickle.dump(index, f)


print("\nIndex created successfully!")
print("Total images:", len(paths))