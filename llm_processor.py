import os, json, re
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import ValidationError
from models import Declaration, Invoice

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def classify_text(input_text: str) -> str:
    """Use LLM (OpenAI) to detect type"""
    prompt = load_prompt("prompt_detect.txt").replace("{input_text}", input_text)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a document classifier. Reply with only one word: Invoice or Declaration."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()

def clean_json(raw_text: str) -> str:
    """Remove code fences and extra text around JSON"""
    # If fenced with ```json ... ```
    match = re.search(r"```json\s*(.*?)```", raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # If fenced with just ```
    match = re.search(r"```(.*?)```", raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()

# def extract_structured(input_text: str) -> dict:
#     """Send text to the right prompt and validate with Pydantic"""
#     doc_type = classify_text(input_text)

#     if doc_type.lower() == "declaration":
#         prompt = load_prompt("prompt_declaration.txt").replace("{input_text}", input_text)

#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "Return ONLY valid JSON. Do not add explanations or code fences."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0
#         )

#         raw_json = response.choices[0].message.content.strip()
#         raw_json = clean_json(raw_json)

#         try:
#             data = json.loads(raw_json)
#             return Declaration(**data).model_dump()
#         except (json.JSONDecodeError, ValidationError) as e:
#             raise ValueError(f"Failed to validate Declaration: {e}\nRaw output:\n{raw_json}")

#     elif doc_type.lower() == "invoice":
#         prompt = load_prompt("prompt_invoice.txt").replace("{input_text}", input_text)

#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "Return ONLY valid JSON. Do not add explanations or code fences."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0
#         )

#         raw_json = response.choices[0].message.content.strip()
#         raw_json = clean_json(raw_json)

#         try:
#             data = json.loads(raw_json)
#             return Invoice(**data).model_dump()
#         except (json.JSONDecodeError, ValidationError) as e:
#             raise ValueError(f"Failed to validate Invoice: {e}\nRaw output:\n{raw_json}")

#     else:
#         raise ValueError(f"Unknown document type: {doc_type}")

def extract_structured(input_text: str, prompt_template: str = None) -> dict:
    """
    Send text + optional prompt template to LLM and validate with Pydantic.
    If no prompt_template is given, it will load from file automatically
    depending on document type.
    """
    doc_type = classify_text(input_text)

    if doc_type.lower() == "declaration":
        prompt = (
            prompt_template or load_prompt("prompt_declaration.txt")
        ).replace("{input_text}", input_text)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON. Do not add explanations or code fences."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        raw_json = response.choices[0].message.content.strip()
        raw_json = clean_json(raw_json)

        try:
            data = json.loads(raw_json)
            return Declaration(**data).model_dump()
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Failed to validate Declaration: {e}\nRaw output:\n{raw_json}")

    elif doc_type.lower() == "invoice":
        prompt = (
            prompt_template or load_prompt("prompt_invoice.txt")
        ).replace("{input_text}", input_text)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON. Do not add explanations or code fences."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        raw_json = response.choices[0].message.content.strip()
        raw_json = clean_json(raw_json)

        try:
            data = json.loads(raw_json)
            return Invoice(**data).model_dump()
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Failed to validate Invoice: {e}\nRaw output:\n{raw_json}")

    else:
        raise ValueError(f"Unknown document type: {doc_type}")
