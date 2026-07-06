import os
import pickle
import pandas as pd
import faiss

from sentence_transformers import SentenceTransformer

DATA_PATH = "data/emails.csv"
INDEX_PATH = "embeddings/faiss.index"
META_PATH = "embeddings/metadata.pkl"

os.makedirs("embeddings", exist_ok=True)

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

emails = df["customer_email"].tolist()
responses = df["human_response"].tolist()

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    emails,
    convert_to_numpy=True
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, INDEX_PATH)

with open(META_PATH, "wb") as f:
    pickle.dump(
        {
            "emails": emails,
            "responses": responses
        },
        f
    )

print("Index created successfully!")
print(f"Stored {len(emails)} emails.")