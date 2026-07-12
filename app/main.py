from fastapi import FastAPI, UploadFile, File, Form
from typing import List
import json
from app.routes import expense_routes, history_routes

app = FastAPI()
# @app.get("/")
# def root():
#     return {"message": "Travel Expense AI v2 running 🚀"}

# 🔥 Register routes
app.include_router(expense_routes.router)
app.include_router(history_routes.router)