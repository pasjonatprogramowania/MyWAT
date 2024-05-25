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

def pobierzListeWiadomosci(nazwa_przedmiotu: str, nazwa_projektu: str):
    pass

def pobierzListeProjektow():
    pass