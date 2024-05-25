from fastapi import Query
from typing import List
from fastapi import UploadFile
from pymongo import MongoClient
import json
from bson import json_util

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['Ogloszenia']

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

from bson import json_util
import json

def get_all_events():
    events = collection.find()
    eventy = []
    for event in events:
        event['_id'] = str(event['_id'])
        eventy.append(event)
    return json.dumps(eventy, default=json_util.default)