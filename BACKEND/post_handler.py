from pymongo import MongoClient
from fastapi import UploadFile
from typing import List
import os

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['wiadomosci']

async def wyslanieWiadmosciPost(nazwa_projektu: str, nazwa_przedmiotu: str, files: List[UploadFile]):
        for file in files:
                message_data = {
                'nazwa_projektu': nazwa_projektu,
                'nazwa_przedmiotu': nazwa_przedmiotu,
                'files': file
            }
                collection.insert_one(message_data)
        return "Wiadomość została wysłana i zapisana w bazie danych."