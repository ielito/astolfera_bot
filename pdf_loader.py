import fitz  # PyMuPDF

def extract_text_from_pdf(path: str) -> str:
    """Extracts text from a PDF file.

    This function opens a PDF file from the given path, iterates through all
    the pages, extracts the text from each page, and returns the combined
    text as a single string.

    Args:
        path (str): The file path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)
