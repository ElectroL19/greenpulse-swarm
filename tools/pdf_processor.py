import os
from google import genai 
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

def process_agricultural_pdf(pdf_path):
    # Initialize the March 2026 Client
    client = genai.Client() 
    
    # Extract text from PDF
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Analyze the PDF text
    # Change from 'gemini-3-flash' to 'gemini-3-flash-preview'
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=f"Extract pest and disease risks from this text: {text[:8000]}"
    )
    
    return response.text