import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX_PATH = os.path.join(BASE_DIR, "embeddings", "faiss.index")
META_PATH = os.path.join(BASE_DIR, "embeddings", "metadata.pkl")


class EmailRetriever:
    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Loading FAISS index...")
        self.index = faiss.read_index(INDEX_PATH)

        print("Loading metadata...")
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)

        self.emails = metadata["emails"]
        self.responses = metadata["responses"]

        print(f"Loaded {len(self.emails)} email-response pairs.\n")

    def retrieve(self, query: str, top_k: int = 3):
        """
        Retrieve the most similar customer emails and responses.
        """

        embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        ).astype(np.float32)

        distances, indices = self.index.search(embedding, top_k)

        results = []

        for distance, idx in zip(distances[0], indices[0]):

            results.append(
                {
                    "customer_email": self.emails[idx],
                    "human_response": self.responses[idx],
                    "distance": float(distance)
                }
            )

        return results


if __name__ == "__main__":

    retriever = EmailRetriever()

    query = input("\nCustomer Email:\n")

    results = retriever.retrieve(query)

    print("\nTop Matches\n")

    for i, item in enumerate(results, start=1):

        print("=" * 60)

        print(f"Match {i}")

        print("Customer Email:")
        print(item["customer_email"])

        print("\nSuggested Human Response:")
        print(item["human_response"])

        print(f"\nDistance : {item['distance']:.4f}")

        print("=" * 60)