import datetime
from pymongo import MongoClient
from fastapi import UploadFile, HTTPException
from typing import List
import os

client = MongoClient("mongodb://localhost:27017")
db = client["Baza"]
notatki = db["Notatka"]

def wyslanieWiadmosciPost(nazwa_projektu: str, nazwa_przedmiotu: str, files: List[UploadFile]):
    for file in files:
        # Zapisywanie pliku na serwerze
        file_path = f"DB/{file.filename}"
        with open(file_path, "wb") as buffer:
            contents = file.file.read()
            buffer.write(contents)

        notatka = {
            'ID': file.filename,
            'nazwa_projektu': nazwa_projektu,
            'nazwa_przedmiotu': nazwa_przedmiotu,
            'nazwa_uzytkownika': 'Uzytkownik',
            'data': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'content': file_path,
            'format': file.content_type
        }
        result = notatki.insert_one(notatka)
    # Zwracanie wyniku
    if result.inserted_id:
        return {"message": "Pliki zostały pomyślnie przesłane i zapisane w bazie danych"}
    else:
        return {"message": "Wystąpił błąd podczas zapisywania plików w bazie danych"}

def dodajNazweProjektu(nazwa: str):
    pass

def dodajNazwePrzedmiotu(nazwa: str, nazwa_projektu: str):
    pass