from fastapi import Query
from typing import List

# Przykładowe dane (dummy data)
dummy_files = [
    {"id": 1, "nazwa": "plik1.txt", "format": "txt"},
    {"id": 2, "nazwa": "plik2.pdf", "format": "pdf"},
    {"id": 3, "nazwa": "plik3.jpg", "format": "jpg"}
]

dummy_messages = [
    {"id": 1, "tresc": "Wiadomość 1", "data": "2023-05-20"},
    {"id": 2, "tresc": "Wiadomość 2", "data": "2023-05-21"},
    {"id": 3, "tresc": "Wiadomość 3", "data": "2023-05-22"}
]

dummy_projects = [
    {"id": 1, "nazwa": "Projekt 1"},
    {"id": 2, "nazwa": "Projekt 2"},
    {"id": 3, "nazwa": "Projekt 3"}
]

def pobierzListePlikow(nazwa_przedmiotu: str, nazwa_projektu: str) -> List[dict]:
    # Logika pobierania listy plików z bazy danych
    # Zwróć listę plików lub pustą listę, jeśli brak wyników
    return []

def pobierzListeWiadomosci(nazwa_przedmiotu: str, nazwa_projektu: str) -> List[dict]:
    # Logika pobierania listy wiadomości z bazy danych
    # Zwróć listę wiadomości lub pustą listę, jeśli brak wyników
    return []

def pobierzListeProjektow() -> List[dict]:
    # Logika pobierania listy projektów z bazy danych
    # Zwróć listę projektów lub pustą listę, jeśli brak wyników
    return []

def get_files(nazwa_przedmiotu: str, nazwa_projektu: str):
    files = pobierzListePlikow(nazwa_przedmiotu, nazwa_projektu)
    if not files:
        files = dummy_files  # Użyj przykładowych danych, jeśli brak wyników
    return {"files": files}

def get_message(nazwa_przedmiotu: str, nazwa_projektu: str):
    messages = pobierzListeWiadomosci(nazwa_przedmiotu, nazwa_projektu)
    if not messages:
        messages = dummy_messages  # Użyj przykładowych danych, jeśli brak wyników
    return {"messages": messages}

def get_all_projects():
    projects = pobierzListeProjektow()
    if not projects:
        projects = dummy_projects  # Użyj przykładowych danych, jeśli brak wyników
    return {"projects": projects}