from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import json

router = APIRouter(prefix="/history")


@router.get("/check-expense-history")
async def expense_history_api(travelId: str):
    try:        

        return {
            "message": "API working",
            "travelId": travelId
        }

    except Exception as e:
        return {"error": str(e)}

@router.get("/check-user-history") 
async def user_history_api(userId: str ):
    try:        

        return {
            "message": "API working",
            "userId": userId
        }
    except Exception as e:
        return {"error": str(e)}   
    
