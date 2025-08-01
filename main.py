# main.py

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from crow import run_crow_chain
from dotenv import load_dotenv
import os

# 🔐 Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI(title="Crow AI Suite API")

class QueryInput(BaseModel):
    query: str

@app.post("/crow")
async def crow_response(input_data: QueryInput, x_api_key: str = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

    result = run_crow_chain(input_data.query)
    return {"response": result}
