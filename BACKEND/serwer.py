import datetime
from fastapi import FastAPI, Form
from typing import Annotated, List
from post_handler import createOgloszenie, modifyOgloszenie, usunOgloszenie, createPrzejazd, modifyPrzejazd, usunPrzejazd
from get_handler import get_all_events

app = FastAPI()

from fastapi import FastAPI, Form
from typing import Annotated, Dict
from datetime import datetime

@app.post("/api/post-add-event/")
async def add_event(id: Annotated[int, Form()], type: Annotated[str, Form()], startDateTime: Annotated[datetime, Form()], 
                    endDateTime: Annotated[datetime, Form()], recurrence: Annotated[str, Form()], name: Annotated[str, Form()], 
                    description: Annotated[str, Form()], location: Annotated[str, Form()], link: Annotated[str, Form()], 
                    creator: Annotated[str, Form()], longitude: Annotated[str, Form()], latitude: Annotated[str, Form()]):
    wynik = createOgloszenie(id, type, startDateTime, endDateTime, recurrence, name, description, location, link, creator, longitude,latitude)
    return wynik

@app.post("/api/post-update-event/")
async def update_event(event_id: Annotated[int, Form()], type: Annotated[str, Form()], startDateTime: Annotated[datetime, Form()], 
                       endDateTime: Annotated[datetime, Form()], recurrence: Annotated[str, Form()], name: Annotated[str, Form()], 
                       description: Annotated[str, Form()], location: Annotated[str, Form()], link: Annotated[str, Form()], 
                       creator: Annotated[str, Form()], longitude: Annotated[str, Form()], latitude: Annotated[str, Form()]):
    wynik = modifyOgloszenie(event_id, type, startDateTime, endDateTime, recurrence, name, description, location, link, creator, longitude,latitude)
    return wynik

@app.post("/api/post-remove-event/")
async def remove_event(event_id: Annotated[int, Form()]):
    result = usunOgloszenie(event_id)
    return result

@app.post("/api/post-add-przejazd/")
async def add_przejazd(id: Annotated[int, Form()], DateTime: Annotated[datetime, Form()], name: Annotated[str, Form()],
                       description: Annotated[str, Form()], startLocation: Annotated[str, Form()], endLocation: Annotated[str, Form()],
                       creator: Annotated[str, Form()], passengerNum: Annotated[int, Form()]):
    result = createPrzejazd(id, DateTime, name, description, startLocation, endLocation, creator, passengerNum)
    return result

@app.post("/api/post-modify-przejazd/")
async def modify_przejazd(id: Annotated[int, Form()], DateTime: Annotated[datetime, Form()], name: Annotated[str, Form()],
                          description: Annotated[str, Form()], startLocation: Annotated[str, Form()], endLocation: Annotated[str, Form()],
                          creator: Annotated[str, Form()], passengerNum: Annotated[int, Form()]):
    result = modifyPrzejazd(id, DateTime, name, description, startLocation, endLocation, creator, passengerNum)
    return result

@app.post("/api/post-remove-przejazd/")
async def remove_przejazd(id: Annotated[int, Form()]):
    result = usunPrzejazd(id)
    return result

@app.get("/api/get-all-events/")
async def get_events(typ: Annotated[list[str], Form()]):
    return get_all_events(typ)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)