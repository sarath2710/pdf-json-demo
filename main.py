from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import shutil
from image_text import pdf_to_text
from llm_processor import extract_structured

app = FastAPI()

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # Extract text from PDF
        results = pdf_to_text(tmp_path)

        # Combine OCR text into one string
        all_text = "\n".join(
            page.get("text", {}).get("text", "") if isinstance(page.get("text"), dict) else str(page.get("text"))
            for page in results
        )

        # Pass to LLM for structured output
        structured = extract_structured(all_text)

        return JSONResponse(content={"structured_data": structured})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
# ---------------------------------------------------------------------------------------------

# from image_text import pdf_to_text
# from llm_processor import extract_structured

# def main():
#     pdf_path = r"D:\SynkCode\pdf-json-demo\Xerox.pdf"
#     results = pdf_to_text(pdf_path)

#     # Combine OCR text into one string
#     all_text = "\n".join(
#         page.get("text", {}).get("text", "") if isinstance(page.get("text"), dict) else str(page.get("text"))
#         for page in results
#     )

#     print("DEBUG: Extracted text length =", len(all_text))

#     structured = extract_structured(all_text)

#     print("\n=== Final Structured JSON ===")
#     print(structured)

# if __name__ == "__main__":
#     main()


# --------------------------------------------------------------------------------

# from image_text import pdf_to_text

# def main():
#     pdf_path = "D:\SynkCode\pdf-json-demo\Y16722-6 (00000003) (1)_250922_185144.pdf"   # 👈 put your PDF file path here
#     results = pdf_to_text(pdf_path)

#     # Print results page by page
#     for page in results:
#         print(f"\n=== Page {page['page']} ===")
#         print(page.get("text") or page.get("error"))

# if __name__ == "__main__":
#     main()
