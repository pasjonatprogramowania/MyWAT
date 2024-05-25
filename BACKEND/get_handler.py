from fastapi import Query
from typing import List
from fastapi import UploadFile
from pymongo import MongoClient
# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['Notatka']

def pobierzNotatki(nazwa_przedmiotu: str, nazwa_projektu: str):
    Notatki = []
    cursor = collection.find(
        {
            'nazwa_przedmiotu': nazwa_przedmiotu,
            'nazwa_projektu': nazwa_projektu
        }
    )
    for notatka in cursor:
        print(notatka)
        Notatki.append(notatka)
    
    if Notatki:
        return {"notatki": Notatki}
    else:
        return {"notatki": []}
def pobierzListeWiadomosci():
    pass
def pobierzListeProjektow():
    pass