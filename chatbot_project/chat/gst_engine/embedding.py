from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

#load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    return model.encode(chunks,convert_to_numpy=True)

def build_index(embeddings):
    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index