from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Baza"]
ogloszenia = db["Ogloszenia"]
przejazdy = db["Przejazdy"]

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

def createPrzejazd(id: int, DateTime: datetime, name: str, description: str, startLocation: str, endLocation: str, creator: str, passengerNum: int):
    przejazd_dict = {
        "id": id,
        "DateTime": DateTime,
        "name": name,
        "description": description,
        "startLocation": startLocation,
        "endLocation": endLocation,
        "creator": creator,
        "passengerNum": passengerNum
    }
    wynik = przejazdy.insert_one(przejazd_dict)
    if wynik.inserted_id:
        return "Poprawnie dodano przejazd"
    else:
        return "Nie udało się dodać przejazdu"

def modifyPrzejazd(id: int, DateTime: datetime, name: str, description: str, startLocation: str, endLocation: str, creator: str, passengerNum: int):
    przejazd_do_zmiany = przejazdy.find_one({"id": id})
    if przejazd_do_zmiany:
        przejazd_dict = {
            "id": id,
            "DateTime": DateTime,
            "name": name,
            "description": description,
            "startLocation": startLocation,
            "endLocation": endLocation,
            "creator": creator,
            "passengerNum": passengerNum
        }
        przejazdy.delete_one({"id": id})
        wynik = przejazdy.insert_one(przejazd_dict)
        if wynik.inserted_id:
            return "Udało się zmodyfikować przejazd"
        else:
            return "Nie udało się zmodyfikować przejazdu"
    else:
        return "Nie znaleziono przejazdu o podanym id"

def usunPrzejazd(id: int):
    wynik = przejazdy.delete_one({"id": id})
    if wynik.deleted_count > 0:
        return "Udało się usunąć przejazd"
    else:
        return "Nie udało się usunąć przejazdu"