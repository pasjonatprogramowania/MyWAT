from fastapi import Query
from typing import List
from fastapi import UploadFile
from pymongo import MongoClient
import json

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['Punkty']

test_event = json.dumps({
    "type": "Kołka zainteresowań",
    "startDateTime": "2023-06-15T18:00:00",
    "endDateTime": "2023-06-15T20:00:00",
    "recurrence": "weekly",
    "name": "Spotkanie Koła Matematycznego",
    "description": "Cotygodniowe spotkanie Koła Matematycznego, na którym omawiamy ciekawe zagadnienia i rozwiązujemy zadania.",
    "location": "Sala 101, Wydział Matematyki",
    "link": "https://example.com/kolo-matematyczne",
    "creator": "Jan Kowalski",
    "coordinates": [52.2296756, 21.0122287]
})

async def get_all_events_handler(filter=None):
    client = MongoClient("mongodb://localhost:27017")
    query = {}
    if filter:
        if filter.type:
            query["type"] = filter.type
        if filter.startDateTime:
            query["startDateTime"] = filter.startDateTime
        if filter.endDateTime:
            query["endDateTime"] = filter.endDateTime
        if filter.recurrence:
            query["recurrence"] = filter.recurrence
        if filter.name:
            query["name"] = filter.name
        if filter.description:
            query["description"] = filter.description
        if filter.location:
            query["location"] = filter.location
        if filter.link:
            query["link"] = filter.link
        if filter.creator:
            query["creator"] = filter.creator
        if filter.coordinates:
            query["coordinates"] = filter.coordinates

    events = list(collection.find(query))
    client.close()
    return events