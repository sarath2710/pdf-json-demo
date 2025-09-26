
# PDF to JSON Extractor

This project extracts text from PDF documents, processes them with AI models, and converts them into **structured JSON** using **Pydantic models**.

## Features

* Extract text from PDFs using **OCR (RapidAPI)**
* Use **OpenAI API** to classify and convert text into structured JSON
* Validate extracted data with **Pydantic schemas**

---

## API Keys Setup

You need two API keys. Create a `.env` file in the project root and add:

```ini
# RapidAPI OCR Service (for text extraction from images/PDF)
RAPIDAPI_KEY=your_rapidapi_key_here  
# API Reference: https://rapidapi.com/restyler/api/ocr-extract-text/

# OpenAI API (for LLM processing)
OPENAI_API_KEY=your_openai_api_key_here
```
pdf-json-demo/
* main.py               # Entry point: orchestrates PDF → OCR → LLM → JSON
* image_text.py         # Handles converting PDF pages to images, sending to OCR
* llm_processor.py      # Contains logic to call LLM (OpenAI) for classification & JSON extraction
* models.py              # Pydantic schemas (Invoice, Declaration, nested models)
* prompt_detect.txt     # LLM prompt to detect whether doc is invoice or declaration
* prompt_invoice.txt     # LLM prompt + examples for invoice extraction
* prompt_declaration.txt # LLM prompt + examples for declaration extraction
* requirements.txt       # List of Python dependencies
* .env                    # Environment file holding API keys (not committed)

---

##  Usage

### Run main script

```bash
python main.py
```

1. Extract text from the PDF.
2. Send it to OpenAI API for processing.
3. Validate against Pydantic models.
4. Output structured JSON.

---

## Example Output

```json
{
  "document_header": {
    "authority": "UNITED ARAB EMIRATES Federal Customs Authority",
    "office": "DUBAI CUSTOMS",
    "page": "Page 1 of 1"
  },
  "port_type": "SEA",
  "dec_type": "IMPORT",
  "dec_date": "17/09/2024",
  "dec_no": "101-25367688-24",
  "customs_declaration": {
    "net_weight": "318 kg",
    "consignee_code": "41111514795",
    "gross_weight": "318 kg"
  }
}
```

---

## ⚠️ Notes

* Make sure you have **Poppler** installed for `pdf2image` (required for PDF to image conversion).
* `.env` file should never be committed to version control.

