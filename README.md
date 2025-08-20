# Agentic Document Extraction

A powerful document processing pipeline that extracts structured information from various document types using OCR and AI.

## Features

- **Multi-format Support**: Process PDFs, images, and scanned documents
- **Document Classification**: Automatically detect document types (invoices, receipts, contracts, IDs)
- **Structured Data Extraction**: Extract relevant fields using AI-powered extraction
- **Validation & Confidence Scoring**: Validate extracted data and provide confidence scores
- **Visualization**: Visualize extracted information with bounding boxes
- **REST API**: Easy integration with other services

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agentic-doc-extraction.git
   cd agentic-doc-extraction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR (required for text extraction):
   - **Windows**: Download and install from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
### Web Interface

Start the web interface:
```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.


## Configuration

Create a `.env` file in the project root with your API keys:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama3-70b-8192
TESSERACT_CMD=/usr/bin/tesseract  # Path to Tesseract executable
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
