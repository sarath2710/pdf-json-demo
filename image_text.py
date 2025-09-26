import os
import requests
import tempfile
from pdf2image import convert_from_path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("RAPIDAPI_KEY")

def image_to_text_pil(pil_img):
    """Send a PIL image to the OCR API and return extracted text."""
    url = "https://ocr-extract-text.p.rapidapi.com/ocr"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "ocr-extract-text.p.rapidapi.com"
    }

    # Save PIL image to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
        pil_img.save(tmp, format="JPEG")
        tmp.seek(0)
        files = {"image": tmp}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def pdf_to_text(pdf_path):
    """Convert a PDF into text (page by page)."""
    images = convert_from_path(pdf_path)
    results = []

    for i, img in enumerate(images, start=1):
        try:
            text_result = image_to_text_pil(img)
            results.append({"page": i, "text": text_result})
        except Exception as e:
            results.append({"page": i, "error": str(e)})
    
    return results

# -----------------------------------------
# import requests
# import tempfile
# from pdf2image import convert_from_path

# API_KEY = "503334657amshf38c9cb4228b0e4p11ae04jsn8c9251e4a377"

# def image_to_text_pil(pil_img):
#     """Send a PIL image to the OCR API and return extracted text."""
#     url = "https://ocr-extract-text.p.rapidapi.com/ocr"

#     headers = {
#         "X-RapidAPI-Key": API_KEY,
#         "X-RapidAPI-Host": "ocr-extract-text.p.rapidapi.com"
#     }

#     # Save PIL image to a temporary file
#     with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
#         pil_img.save(tmp, format="JPEG")
#         tmp.seek(0)
#         files = {"image": tmp}
#         response = requests.post(url, headers=headers, files=files)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error {response.status_code}: {response.text}")


# def pdf_to_text(pdf_path):
#     """Convert a PDF into text (page by page)."""
#     images = convert_from_path(pdf_path)
#     results = []

#     for i, img in enumerate(images, start=1):
#         try:
#             text_result = image_to_text_pil(img)
#             results.append({"page": i, "text": text_result})
#         except Exception as e:
#             results.append({"page": i, "error": str(e)})
    
#     return results
