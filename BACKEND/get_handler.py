from pymongo import MongoClient
from typing import list
import os

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['wiadomosci']

def pobierzListePlikow(nazwa_przedmiotu: str, nazwa_projektu: str):
    # Pobieranie listy plików z bazy danych
    query = {
        'nazwa_projektu': nazwa_projektu,
        'nazwa_przedmiotu': nazwa_przedmiotu
    }
    message = collection.find_one(query)
    if message:
        notatki = message['notatki']
        file_list = [notatka['content'] for notatka in notatki]
        return {"files": file_list}
    else:
        return {"files": []}

def pobierzListeWiadomosci(nazwa_przedmiotu: str, nazwa_projektu: str):
    pass

def pobierzListeProjektow():
    pass

@app.get("/api/get-files/")
async def get_files(NazwaPrzedmiotu: str, NazwaProjektu: str):
    collection = db["wiadomosci"]
    notatki = collection.find({"nazwa_przedmiotu": NazwaPrzedmiotu, "nazwa_projektu": NazwaProjektu})
    return list(notatki)

@app.get("/api/get-message/")
async def get_message(NazwaPrzedmiotu: str, NazwaProjektu: str):
    collection = db["wiadomosci"]
    notatki = collection.find({"nazwa_przedmiotu": NazwaPrzedmiotu, "nazwa_projektu": NazwaProjektu, "format": "text"})
    return list(notatki)

@app.get("/api/get-all-projects-id/")
async def get_all_projects_id():
    collection = db["wiadomosci"]
    przedmioty = collection.distinct("nazwa_przedmiotu")
    return list(przedmioty)

@app.get("/api/get-project-id/")
async def get_project_id(NazwaPrzedmiotu: str):
    collection = db["wiadomosci"]
    projekty = collection.distinct("nazwa_projektu", {"nazwa_przedmiotu": NazwaPrzedmiotu})
    return list(projekty)

@app.get("/api/get-user-id/")
async def get_user_id():
    collection = db["Uzykownik"]
    users = collection.find({}, {"_id": 1, "nazwa_użytkownika": 1})
    return list(users)