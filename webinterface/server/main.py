# start server IN WSL with command: uvicorn server.main:app --reload

import time
from .sender import Sender

from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


raspberry = Sender("ACM0")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://192.168.56.1:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/sand-pattern/{pattern_index}")
def change_pattern(pattern_index: int):
    raspberry.initializeTable()
    time.sleep(1)
    raspberry.testStar()
    print(pattern_index)
    return {"pattern index" : pattern_index}
    