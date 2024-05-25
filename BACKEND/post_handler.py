from datetime import datetime
from pymongo import MongoClient
from fastapi import UploadFile, HTTPException
from typing import List
import os
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client["Baza"]
ogloszenia = db["Ogloszenia"]

def createOgloszenie(id: int, type: str, startDateTime: datetime, endDateTime: datetime, recurrence: str,
                     name: str, description: str, location: str, link: str, creator: str, longitude: str, latitude: str):
    event_dict = {
        "id": id,
        "type": type,
        "startDateTime": startDateTime,
        "endDateTime": endDateTime,
        "recurrence": recurrence,
        "name": name,
        "description": description,
        "location": location,
        "link": link,
        "creator": creator,
        "longitude": longitude,
        "latitude": latitude
    }
    wynik = ogloszenia.insert_one(event_dict)
    if wynik.inserted_id:
        return "Poprawnie dodano rekord"
    else:
        return "Nie udało się"

def modifyOgloszenie(event_id: int, type: str, startDateTime: datetime, endDateTime: datetime, recurrence: str,
                     name: str, description: str, location: str, link: str, creator: str, longitude: str, latitude: str):
    event_do_zmiany = ogloszenia.find_one({"id": event_id})
    if event_do_zmiany:
        event_dict = {
            "id": event_id,
            "type": type,
            "startDateTime": startDateTime,
            "endDateTime": endDateTime,
            "recurrence": recurrence,
            "name": name,
            "description": description,
            "location": location,
            "link": link,
            "creator": creator,
            "longitude": longitude,
            "latitude": latitude
        }
        ogloszenia.delete_one({"id": event_id})
        wynik = ogloszenia.insert_one(event_dict)
        if wynik.inserted_id:
            return "Udało się zmodyfikować rekord"
        else:
            return "Nie udało się"
    else:
        return "Nie znaleziono rekordu o podanym id"

def usunOgloszenie(event_id: int):
    wynik = ogloszenia.delete_one({"id": event_id})
    if wynik.deleted_count > 0:
        return "Udało się usunąć rekord"
    else:
        return "Nie udało się"