from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from post_handler import wyslanieWiadmosciPost
#from get_handler import 

app = FastAPI()


@app.post("/api/post-sendMessage/")
async def send_message(nazwa_projektu: str = Form(...), nazwa_przedmiotu: str = Form(...), files: List[UploadFile] = File(...)):
    result = wyslanieWiadmosciPost(nazwa_projektu, nazwa_przedmiotu, files)
    return {"message": result}

@app.post("/api/post-projectName/")
async def add_project_name(nazwa: str):
    result = dodajNazweProjektu(nazwa)
    return {"message": result}

@app.post("/api/post-przedmiotName/")
async def add_przedmiot_name(nazwa: str, nazwa_projektu: str):
    result = dodajNazwePrzedmiotu(nazwa, nazwa_projektu)
    return {"message": result}

@app.get("/api/get-files/")
async def get_files(nazwa_przedmiotu: str, nazwa_projektu: str):
    files = pobierzListePlikow(nazwa_przedmiotu, nazwa_projektu)
    return {"files": files}

@app.get("/api/get-messege/")
async def get_message(nazwa_przedmiotu: str, nazwa_projektu: str):
    messages = pobierzListeWiadomosci(nazwa_przedmiotu, nazwa_projektu)
    return {"messages": messages}

@app.get("/api/get-all-projects/")
async def get_all_projects():
    projects = pobierzListeProjektow()
    return {"projects": projects}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)