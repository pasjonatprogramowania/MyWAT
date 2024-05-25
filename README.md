# MyWAT

MyWAT to aplikacja internetowa zbudowana przy użyciu frameworka FastAPI w języku Python. Aplikacja ta służy jako interaktywna mapa uczelni, na której zainteresowani oraz uczelniani użytkownicy mogą umieszczać punkty zainteresowania, takie jak koła zainteresowań, sympozja, targi pracy itp.

## Endpointy

Aplikacja udostępnia następujące endpointy:

### POST

- `/api/post-add-event/`: Endpoint służący do dodawania nowego wydarzenia. Przyjmuje dane wydarzenia, takie jak identyfikator, typ, data i godzina rozpoczęcia, data i godzina zakończenia, cykl powtarzania, nazwa, opis, lokalizacja, link, twórca oraz współrzędne geograficzne (długość i szerokość geograficzna). Dane te są przekazywane w formularzu HTML.

- `/api/post-update-event/`: Endpoint służący do aktualizacji istniejącego wydarzenia. Przyjmuje identyfikator wydarzenia oraz zaktualizowane dane wydarzenia, takie jak typ, data i godzina rozpoczęcia, data i godzina zakończenia, cykl powtarzania, nazwa, opis, lokalizacja, link, twórca oraz współrzędne geograficzne. Dane te są przekazywane w formularzu HTML.

- `/api/post-remove-event/`: Endpoint służący do usuwania wydarzenia. Przyjmuje identyfikator wydarzenia, który ma zostać usunięty.

### GET

- `/api/get-all-events/`: Endpoint służący do pobierania wszystkich wydarzeń z bazy danych. Zwraca dane wydarzeń w formacie JSON.

## Baza danych

Aplikacja korzysta z bazy danych MongoDB i wykorzystuje bibliotekę PyMongo do komunikacji z bazą danych. Dane wydarzeń są przechowywane w kolekcji "Ogloszenia" w bazie danych "Baza".

## Struktura aplikacji

Aplikacja składa się z następujących plików:

- `serwer.py`: Główny plik aplikacji, w którym zdefiniowane są endpointy FastAPI oraz uruchamiany jest serwer.

- `get_handler.py`: Plik zawierający funkcję `get_all_events()`, która pobiera wszystkie wydarzenia z bazy danych i zwraca je w formacie JSON.

- `post_handler.py`: Plik zawierający funkcje obsługujące żądania POST, takie jak `createOgloszenie()` do dodawania nowego wydarzenia, `modifyOgloszenie()` do aktualizacji istniejącego wydarzenia oraz `usunOgloszenie()` do usuwania wydarzenia.

## Uruchomienie aplikacji

Aby uruchomić aplikację, należy wykonać plik `serwer.py`. Serwer zostanie uruchomiony na lokalnym adresie `127.0.0.1` i porcie `8080`.

Aplikacja MyWAT umożliwia użytkownikom interakcję z interaktywną mapą uczelni, dodawanie, aktualizowanie i usuwanie punktów zainteresowania. Dane są przechowywane w bazie danych MongoDB, a komunikacja odbywa się za pomocą endpointów FastAPI.