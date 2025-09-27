import fitz # PyMuPDF

def extract(pdf_path):
    """
    Extracts text from a PDF and splits it into meaningful paragraphs (chunks).
    """
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text("text")
    
    # Split the text into chunks based on paragraphs (double newlines)
    # This is a much better strategy for prose/Q&A documents.
    chunks = full_text.split('\n\n')
    
    # Clean up the chunks: remove extra whitespace and filter out empty chunks
    cleaned_chunks = [chunk.strip().replace('\n', ' ') for chunk in chunks if chunk.strip()]
    
    return cleaned_chunks