from fastapi import Query
from typing import List
from fastapi import UploadFile
from pymongo import MongoClient
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

def get_message(nazwa_przedmiotu: str, nazwa_projektu: str):
    messages = pobierzListeWiadomosci(nazwa_przedmiotu, nazwa_projektu)
    if not messages:
        messages = dummy_messages  # Użyj przykładowych danych, jeśli brak wyników
    return {"messages": messages}

def get_all_projects():
    projects = pobierzListeProjektow()
    if not projects:
        projects = dummy_projects  # Użyj przykładowych danych, jeśli brak wyników
    return {"projects": projects}