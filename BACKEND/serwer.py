from fastapi import FastAPI, File, Query, UploadFile, Form
from typing import Annotated
from pydantic import BaseModel
from post_handler import wyslanieWiadmosciPost, dodajNazweProjektu, dodajNazwePrzedmiotu
from get_handler import get_files, get_message, get_all_projects

app = FastAPI()

@app.post("/api/post-sendMessage/")
async def upload_files(
    nazwa_projektu: Annotated[str, Form()],
    nazwa_przedmiotu: Annotated[str, Form()],
    files: list[UploadFile]
):
    wyslanieWiadmosciPost(nazwa_projektu, nazwa_przedmiotu, files)
    return 0

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
async def get_files_endpoint(
    nazwa_przedmiotu: str = Query(...),
    nazwa_projektu: str = Query(...)
):
    return get_files(nazwa_przedmiotu, nazwa_projektu)

@app.get("/api/get-message/")
async def get_message_endpoint(
    nazwa_przedmiotu: str = Query(...),
    nazwa_projektu: str = Query(...)
):
    return get_message(nazwa_przedmiotu, nazwa_projektu)

@app.get("/api/get-all-projects/")
async def get_all_projects_endpoint():
    return get_all_projects()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)