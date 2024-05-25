from fastapi import FastAPI, File, Query, UploadFile, Form
from typing import Annotated, List
from pydantic import BaseModel
from pymongo import MongoClient
from post_handler import wyslanieWiadmosciPost, dodajNazweProjektu, dodajNazwePrzedmiotu
from get_handler import pobierzNotatki, pobierzListeWiadomosci, pobierzListeProjektow

app = FastAPI()

@app.post("/api/post-add-event/")
async def add_event():
    pass

@app.post("/api/post-update-event/")
async def update_event():
    pass

@app.post("/api/post-remove-event/")
async def remove_event():
    pass

@app.get("/api/get-all-event/")
async def get_all_events():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)