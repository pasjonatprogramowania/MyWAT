from pymongo import MongoClient
import json
from bson import json_util

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
collection = db['Ogloszenia']

from bson import json_util
import json

def get_all_events(typ: list[str]):
    events = collection.find({"type": {"$in": typ}})
    eventy = []
    for event in events:
        event['_id'] = str(event['_id'])
        eventy.append(event)
    return json.dumps(eventy, default=json_util.default)