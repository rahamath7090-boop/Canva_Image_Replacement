import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from feature_extractor import FeatureExtractor


INDEX_FILE = "models/image_index.pkl"


extractor = FeatureExtractor()


def search_similar_images(query_image, top_k=5):

    with open(INDEX_FILE, "rb") as f:
        index = pickle.load(f)

    query_feature = extractor.extract(query_image)

    database_features = np.array(index["features"])

    scores = cosine_similarity(
        [query_feature],
        database_features
    )[0]

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for idx in top_indices:

        results.append({
            "path": index["paths"][idx],
            "score": float(scores[idx])
        })

    return results
if __name__ == "__main__":

    query = "queries/query_mountain.jpeg"

    results = search_similar_images(query)

    for result in results:

        print(
            result["path"],
            "Similarity:",
            round(result["score"], 4)
        )