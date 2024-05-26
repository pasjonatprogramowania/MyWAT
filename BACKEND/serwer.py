from pymongo import MongoClient
import json
from bson import json_util
from fastapi import FastAPI, Form, Query, HTTPException
from typing import Annotated, List, Union
from post_handler import createOgloszenie, modifyOgloszenie, usunOgloszenie, createPrzejazd, modifyPrzejazd, usunPrzejazd
from get_handler import get_all_events, get_all_przejazdy
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Konfiguracja połączenia z bazą danych MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Baza']
events_collection = db['Ogloszenia']
przejazdy_collection = db['Przejazdy']

app = FastAPI()

# Konfiguracja CORS
origins = [
    "http://localhost:9000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/post-add-event/")
async def add_event(id: Annotated[int, Form()],
                    type: Annotated[str, Form()],
                    startDateTime: Annotated[datetime, Form()],
                    endDateTime: Annotated[datetime, Form()],
                    recurrence: Annotated[str, Form()],
                    name: Annotated[str, Form()],
                    description: Annotated[str, Form()],
                    location: Annotated[str, Form()],
                    link: Annotated[str, Form()],
                    creator: Annotated[str, Form()],
                    longitude: Annotated[str, Form()],
                    latitude: Annotated[str, Form()]):
    try:
        wynik = createOgloszenie(id, type, startDateTime, endDateTime, recurrence, name, description, location, link, creator, longitude, latitude)
        return wynik
    except Exception as e:
        logger.error(f"Błąd podczas dodawania ogłoszenia: {str(e)}")
        logger.debug(f"Parametry żądania: id={id}, type={type}, startDateTime={startDateTime}, endDateTime={endDateTime}, recurrence={recurrence}, name={name}, description={description}, location={location}, link={link}, creator={creator}, longitude={longitude}, latitude={latitude}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@app.post("/api/post-update-event/")
async def update_event(event_id: Annotated[int, Form()],
                       type: Annotated[str, Form()],
                       startDateTime: Annotated[datetime, Form()],
                       endDateTime: Annotated[datetime, Form()],
                       recurrence: Annotated[str, Form()],
                       name: Annotated[str, Form()],
                       description: Annotated[str, Form()],
                       location: Annotated[str, Form()],
                       link: Annotated[str, Form()],
                       creator: Annotated[str, Form()],
                       longitude: Annotated[str, Form()],
                       latitude: Annotated[str, Form()]):
    try:
        wynik = modifyOgloszenie(event_id, type, startDateTime, endDateTime, recurrence, name, description, location, link, creator, longitude, latitude)
        return wynik
    except Exception as e:
        logger.error(f"Błąd podczas modyfikacji ogłoszenia: {str(e)}")
        logger.debug(f"Parametry żądania: event_id={event_id}, type={type}, startDateTime={startDateTime}, endDateTime={endDateTime}, recurrence={recurrence}, name={name}, description={description}, location={location}, link={link}, creator={creator}, longitude={longitude}, latitude={latitude}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@app.post("/api/post-remove-event/")
async def remove_event(event_id: Annotated[int, Form()]):
    try:
        result = usunOgloszenie(event_id)
        return result
    except Exception as e:
        logger.error(f"Błąd podczas usuwania ogłoszenia: {str(e)}")
        logger.debug(f"Parametry żądania: event_id={event_id}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@app.post("/api/post-add-przejazd/")
async def add_przejazd(id: Annotated[int, Form()],
                       DateTime: Annotated[datetime, Form()],
                       name: Annotated[str, Form()],
                       description: Annotated[str, Form()],
                       startLocation: Annotated[str, Form()],
                       endLocation: Annotated[str, Form()],
                       creator: Annotated[str, Form()],
                       passengerNum: Annotated[int, Form()]):
    try:
        result = createPrzejazd(id, DateTime, name, description, startLocation, endLocation, creator, passengerNum)
        return result
    except Exception as e:
        logger.error(f"Błąd podczas dodawania przejazdu: {str(e)}")
        logger.debug(f"Parametry żądania: id={id}, DateTime={DateTime}, name={name}, description={description}, startLocation={startLocation}, endLocation={endLocation}, creator={creator}, passengerNum={passengerNum}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@app.post("/api/post-modify-przejazd/")
async def modify_przejazd(id: Annotated[int, Form()],
                          DateTime: Annotated[datetime, Form()],
                          name: Annotated[str, Form()],
                          description: Annotated[str, Form()],
                          startLocation: Annotated[str, Form()],
                          endLocation: Annotated[str, Form()],
                          creator: Annotated[str, Form()],
                          passengerNum: Annotated[int, Form()]):
    try:
        result = modifyPrzejazd(id, DateTime, name, description, startLocation, endLocation, creator, passengerNum)
        return result
    except Exception as e:
        logger.error(f"Błąd podczas modyfikacji przejazdu: {str(e)}")
        logger.debug(f"Parametry żądania: id={id}, DateTime={DateTime}, name={name}, description={description}, startLocation={startLocation}, endLocation={endLocation}, creator={creator}, passengerNum={passengerNum}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@app.post("/api/post-remove-przejazd/")
async def remove_przejazd(id: Annotated[int, Form()]):
    try:
        result = usunPrzejazd(id)
        return result
    except Exception as e:
        logger.error(f"Błąd podczas usuwania przejazdu: {str(e)}")
        logger.debug(f"Parametry żądania: id={id}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@app.get("/api/get-all-events/")
async def get_events(typ: Annotated[Union[List[str], None], Query()] = None):
    try:
        if typ is None:
            typ = []
        return get_all_events(typ)
    except Exception as e:
        logger.error(f"Błąd podczas pobierania ogłoszeń: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/api/get-all-przejazdy/")
async def get_przejazdy():
    try:
        return get_all_przejazdy()
    except Exception as e:
        logger.error(f"Błąd podczas pobierania przejazdów: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)