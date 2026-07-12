from fastapi import APIRouter, UploadFile, File, Form
from typing import List,Annotated
import json

from app.services import storage_service

router = APIRouter()

@router.post("/debug-files")
async def debug_files(
    files: List[UploadFile] = File(...)
):
    return {
        "count": len(files),
        "names": [f.filename for f in files]
    }

@router.post("/validate-expense")
async def validate_expense_api(
    user_id: str = Form(...),
    travel_id: str = Form(...),
    expense_lines: str = Form(...),
    files: List[UploadFile] = File(...)
):
    try:

        # ------------------------------------------
        # Convert expense lines JSON string to object
        # ------------------------------------------
        expense_data = json.loads(expense_lines)

        # ------------------------------------------
        # Upload all documents to Azure Blob Storage
        # ------------------------------------------
        uploaded_documents = await storage_service.upload_documents(
            user_id=user_id,
            travel_id=travel_id,
            files=files
        )

        # ------------------------------------------
        # Temporary response
        # ------------------------------------------
        return {
            "message": "Documents uploaded successfully.",
            "user_id": user_id,
            "travel_id": travel_id,
            "total_expenses": len(expense_data),
            "total_documents": len(uploaded_documents),
            "documents": uploaded_documents
        }

    except Exception as ex:
        return {
            "success": False,
            "error": str(ex)
        }