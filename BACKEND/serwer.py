from fastapi import FastAPI, File, Query, UploadFile, Form
from typing import Annotated, List
from pydantic import BaseModel
from pymongo import MongoClient
from post_handler import wyslanieWiadmosciPost, dodajNazweProjektu, dodajNazwePrzedmiotu
from get_handler import pobierzNotatki, pobierzListeWiadomosci, pobierzListeProjektow

app = FastAPI()

@app.post("/api/post-sendMessage/")
async def upload_files(
    nazwa_projektu: Annotated[str, Form()],
    nazwa_przedmiotu: Annotated[str, Form()],
    files: Annotated[List[UploadFile], File()]
):
    return wyslanieWiadmosciPost(nazwa_projektu, nazwa_przedmiotu, files)

@app.post("/api/post-projectName/")
async def add_project_name(nazwa: Annotated[str, Form()]):
    result = dodajNazweProjektu(nazwa)
    return {"message": result}

@app.post("/api/post-przedmiotName/")
async def add_przedmiot_name(
    nazwa: Annotated[str, Form()],
    nazwa_projektu: Annotated[str, Form()]
):
    result = dodajNazwePrzedmiotu(nazwa, nazwa_projektu)
    return {"message": result}

@app.get("/api/get-files/")
async def get_files(
    nazwa_przedmiotu: Annotated[str, Form()],
    nazwa_projektu: Annotated[str, Form()]
):
    files = pobierzNotatki(nazwa_przedmiotu, nazwa_projektu)
    return {"files": files}

@app.get("/api/get-messege/")
async def get_message(
    nazwa_przedmiotu: Annotated[str, Form()],
    nazwa_projektu: Annotated[str, Form()]
):
    messages = pobierzListeWiadomosci(nazwa_przedmiotu, nazwa_projektu)
    return {"messages": messages}

@app.get("/api/get-all-projects/")
async def get_all_projects():
    projects = pobierzListeProjektow()
    return {"projects": projects}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)