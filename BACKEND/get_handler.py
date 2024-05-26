from pymongo import MongoClient
import json
from bson import json_util

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
events_collection = db['Ogloszenia']
przejazdy_collection = db['Przejazdy']


from bson import json_util
import json

def get_all_events(typ: list[str]):
    events = events_collection.find({"type": {"$in": typ}})
    eventy = []
    for event in events:
        event['_id'] = str(event['_id'])
        eventy.append(event)
    return json.dumps(eventy, default=json_util.default)

def get_all_przejazdy():
    przejazdy = przejazdy_collection.find()
    przejazdyy = []
    for przejazd in przejazdy:
        przejazd['_id'] = str(przejazd['_id'])
        przejazdyy.append(przejazd)
    return json.dumps(przejazdyy, default=json_util.default)