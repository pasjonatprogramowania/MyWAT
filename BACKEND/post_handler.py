import datetime
from pymongo import MongoClient
from fastapi import UploadFile, HTTPException
from typing import List
import os

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['wiadomosci']

async def wyslanieWiadmosciPost(nazwa_projektu: str, nazwa_przedmiotu: str, files: list[UploadFile]):
    notatki = []
    for file in files:
        # Zapisywanie pliku na serwerze
        file_path = f"DB/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Tworzenie obiektu Notatka
        notatka = {
            'ID': len(notatki) + 1,
            'nazwa_uzytkownika': 'Uzytkownik',
            'data': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'content': file_path,
            'format': file.content_type
        }
        notatki.append(notatka)

    # Zapisywanie notatek w bazie danych
    message_data = {
        'nazwa_projektu': nazwa_projektu,
        'nazwa_przedmiotu': nazwa_przedmiotu,
        'notatki': notatki
    }
    collection.insert_one(message_data)

    return "Wiadomość została wysłana i zapisana w bazie danych."

def dodajNazweProjektu(nazwa: str):
    pass

def dodajNazwePrzedmiotu(nazwa: str, nazwa_projektu: str):
    pass