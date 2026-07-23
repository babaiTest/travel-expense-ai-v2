from fastapi import APIRouter, UploadFile, File, Form
from typing import List,Annotated
import json

from app.services import storage_service #, travel_processing_service
from app.services.travel_processing_service import TravelProcessingService
from app.repositories.travel_repository import TravelRepository

travel_processing_service = TravelProcessingService()
travel_repository = TravelRepository()
router = APIRouter()

# @router.post("/debug-files")
# async def debug_files(
#     files: List[UploadFile] = File(...)
# ):
#     return {
#         "count": len(files),
#         "names": [f.filename for f in files]
#     }

@router.post("/validate-expense")
async def validate_expense_api(
    user_id: str = Form(...),
    travel_id: str = Form(...),
    expense_lines: str = Form(...),
    files: List[UploadFile] = File(...)
):
    try:

        # ------------------------------------------
        # Create Travel collection if it does not exist
        travel_repository.create_travel(
            user_id=user_id,
            travel_id=travel_id
        )

        # ------------------------------------------
        # Convert expense lines JSON string to object
        # ------------------------------------------
        expense_data = json.loads(expense_lines)

        # ------------------------------------------
        # Upload all documents to Azure Blob Storage
        # Step 1: Upload documents
        # ------------------------------------------
        uploaded_documents = await storage_service.upload_documents(
            user_id=user_id,
            travel_id=travel_id,
            files=files
        )

        # Step 2: Process travel
        result = travel_processing_service.process_travel(        
        user_id=user_id,
        travel_id=travel_id,
        expense_lines=expense_lines
    )

        # ------------------------------------------
        # Temporary response
        # ------------------------------------------
        return {
            "success": True,
            "result": result
        }

    except Exception as ex:
        return {
            "success": False,
            "error": str(ex)
        }