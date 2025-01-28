from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],  
)


with open("data.json") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks = [entry["marks"] for entry in data if entry["name"] in name]
    return {"marks": marks}


