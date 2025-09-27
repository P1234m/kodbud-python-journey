# --- Standard Library Imports ---
import os

# --- Your Custom Module Imports ---
from .pdf_parser import extract
from .embedding import embed_chunks, build_index, model
from .retriever import retrieve
from .model import get_hf_answer  # <-- Uses lazy-loaded Hugging Face model

# --------------------------------------------------------------------------
# This setup part runs once when the Django server starts.
# It loads all PDFs, creates embeddings, and builds the search index.
# --------------------------------------------------------------------------

print("Loading PDFs and building index for the chatbot...")

# 1. List all your PDF files here.
#    Make sure these files are inside the 'chatbot' app folder.
pdf_files = [
    "gst.pdf",
    "services-booklet.pdf"
]

all_chunks = []
for pdf_path in pdf_files:
    print(f"Extracting text from: {pdf_path}")
    try:
        chunks = extract(pdf_path)
        all_chunks.extend(chunks)
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

# 2. Embed and index the combined chunks from all PDFs
embeddings = embed_chunks(all_chunks)
index = build_index(embeddings)

print(f"Index built from {len(pdf_files)} documents. Chatbot is ready.")
print("-" * 50)

# --------------------------------------------------------------------------
# This function is called every time a user sends a message.
# --------------------------------------------------------------------------

def answer_query(query: str) -> str:
    """
    Handles a user query by retrieving relevant context from all documents 
    and generating an answer using the local Hugging Face model.
    """
    relevant_chunks = retrieve(query, model, index, all_chunks)
    answer = get_hf_answer(query, relevant_chunks)
    return answer