from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from get_handler import test_event, get_all_events_handler

app = FastAPI()

class EventFilter(BaseModel):
    type: str = None
    startDateTime: str = None
    endDateTime: str = None
    recurrence: str = None
    name: str = None
    description: str = None
    location: str = None
    link: str = None
    creator: str = None
    coordinates: List[float] = None

@app.get("/api/get-all-events/")
async def get_all_events(filter: EventFilter = None):
    events = await get_all_events_handler(filter)
    return events

@app.get("/api/test/get-all-event/")
async def test_get_all_events():
    return test_event

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)