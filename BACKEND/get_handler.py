from fastapi import Query
from typing import List
from fastapi import UploadFile
from pymongo import MongoClient


def pobierzListePlikow(nazwa_przedmiotu: str, nazwa_projektu: str):

    # Tworzenie zapytania do bazy danych
    query = {
        "nazwa_projektu": nazwa_projektu,
        "nazwa_przedmiotu": nazwa_przedmiotu
    }

    # Pobieranie listy plików z bazy danych
    result = collection.find(query)

    # Tworzenie listy plików
    files = []
    for item in result:
        files.append(item["file"])

    return files

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