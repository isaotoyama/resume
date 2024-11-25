import fitz  # PyMuPDF

def extract_text_chunks(pdf_path, chunk_size, overlap_size):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    chunks = []

    # Iterate through each page in the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page_text = page.get_text()

        # Split the text from the current page into chunks with overlap
        start = 0
        while start < len(page_text):
            end = start + chunk_size
            chunk = page_text[start:end]

            # Store the page number with the chunk
            chunks.append((page_num + 1, chunk))
            # Move to the next chunk with the overlap
            start += chunk_size - overlap_size
    
    return chunks

# Parameters for extraction
pdf_path = "your_file.pdf"
chunk_size = 1000  # Size of each text chunk in characters
overlap_size = 200  # Overlap size in characters

text_chunks = extract_text_chunks_with_page_numbers(pdf_path, chunk_size, overlap_size)

# Display the chunks with page numbers
for i, (page_number, chunk) in enumerate(text_chunks):
    print(f"Chunk {i + 1} (Page {page_number}):\n{chunk}\n{'-' * 50}")