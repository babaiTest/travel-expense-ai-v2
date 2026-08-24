from langchain_core.prompts import PromptTemplate


HOTEL_PROMPT = PromptTemplate.from_template(
"""
You are an expert AI specialized in extracting structured information from hotel invoices and hotel receipts.

If the document is NOT a hotel invoice or hotel receipt, set documentType to "Unknown" and leave data fields empty.

Extraction Rules:

- Use null for missing values.
- Dates must use YYYY-MM-DD format.
- Numbers must not contain currency symbols or commas.
- Preserve the hotel name exactly as printed.
- Preserve the guest name exactly as printed.
- Extract the city and country if available.
- Calculate numberOfNights if it is not explicitly mentioned.
- Extract taxes separately whenever possible.
- Total amount must represent the final payable amount.

OCR Text:

{ocr_text}
"""
)


def build_hotel_prompt(ocr_text: str) -> str:
    return HOTEL_PROMPT.format(
        ocr_text=ocr_text
    )