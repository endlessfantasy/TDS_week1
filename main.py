from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

#test
with open("data.json") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: Optional[List[str]] = Query(None)):
    if not name:
        raise HTTPException(status_code=400, detail="The 'name' query parameter is required.")
    

    name_to_marks = {entry["name"]: entry["marks"] for entry in data}

    marks = [name_to_marks[n] for n in name if n in name_to_marks]
    
    return {"marks": marks}


