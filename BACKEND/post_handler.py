import datetime
from pymongo import MongoClient
from fastapi import UploadFile, HTTPException
from typing import List
import os
import json

client = MongoClient("mongodb://localhost:27017")
db = client["Baza"]
notatki = db["Notatka"]


