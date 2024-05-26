# MyWAT

MyWAT to aplikacja internetowa zbudowana przy użyciu frameworka FastAPI w języku Python. Aplikacja ta służy jako interaktywna mapa uczelni, na której zainteresowani oraz uczelniani użytkownicy mogą umieszczać punkty zainteresowania, takie jak koła zainteresowań, sympozja, targi pracy itp.

## Endpointy

Aplikacja udostępnia następujące endpointy(Cała dokumentacja znajduje sie w `/docs`):


### POST

- `/api/post-add-event/`: Endpoint służący do dodawania nowego wydarzenia. Przyjmuje dane wydarzenia, takie jak identyfikator, typ, data i godzina rozpoczęcia, data i godzina zakończenia, cykl powtarzania, nazwa, opis, lokalizacja, link, twórca oraz współrzędne geograficzne (długość i szerokość geograficzna). Dane te są przekazywane w formularzu HTML.

- `/api/post-update-event/`: Endpoint służący do aktualizacji istniejącego wydarzenia. Przyjmuje identyfikator wydarzenia oraz zaktualizowane dane wydarzenia, takie jak typ, data i godzina rozpoczęcia, data i godzina zakończenia, cykl powtarzania, nazwa, opis, lokalizacja, link, twórca oraz współrzędne geograficzne. Dane te są przekazywane w formularzu HTML.

- `/api/post-remove-event/`: Endpoint służący do usuwania wydarzenia. Przyjmuje identyfikator wydarzenia, który ma zostać usunięty.

- `/api/post-add-przejazd/`: Endpoint służący do dodawania przejazdów
- `/api/post-modify-przejazd/`: endpoint do modyfikacji przejazdów
- `/api/post-remove-przejazd/`: endpoint do usuwania przejazdów

### GET

- `/api/get-all-events/`: Endpoint służący do pobierania wszystkich wydarzeń z bazy danych. Zwraca dane wydarzeń w formacie JSON.

- `/api/get-all-przejazdy/`: Endpoint służący do pobierania wszystkich przejazdów.
## Baza danych

Aplikacja korzysta z bazy danych MongoDB i wykorzystuje bibliotekę PyMongo do komunikacji z bazą danych. Dane wydarzeń są przechowywane w kolekcji "Ogloszenia" w bazie danych "Baza".

Struktura wydarzenia (event) w bazie danych:

{
 "id": <int>,
 "type": <str>,
 "startDateTime": <datetime>,
 "endDateTime": <datetime>,
 "recurrence": <str>,
 "name": <str>,
 "description": <str>,
 "location": <str>,
 "link": <str>,
 "creator": <str>,
 "longitude": <str>,
 "latitude": <str>
}

Pusta struktura przejazdu:
{
 "id": <int>,
 "DateTime": <datetime>,
 "name": <str>,
 "description": <str>,
 "startLocation": <str>,
 "endLocation": <str>,
 "creator": <str>,
 "passengerNum": <int>
}

## Struktura aplikacji

Aplikacja składa się z następujących plików i folderów:

### BACKEND
- get_handler.py
- post_handler.py
- serwer.py

- `.git/`: Folder zawierający informacje i konfigurację systemu kontroli wersji Git.

- `BACKEND/`: Folder zawierający pliki związane z backendem aplikacji.
 - `get_handler.py`: Plik zawierający funkcję `get_all_events()`, która pobiera wszystkie wydarzenia z bazy danych i zwraca je w formacie JSON.
 - `post_handler.py`: Plik zawierający funkcje obsługujące żądania POST, takie jak `createOgloszenie()` do dodawania nowego wydarzenia, `modifyOgloszenie()` do aktualizacji istniejącego wydarzenia oraz `usunOgloszenie()` do usuwania wydarzenia.
 - `serwer.py`: Główny plik aplikacji, w którym zdefiniowane są endpointy FastAPI oraz uruchamiany jest serwer.

- `quasar-project/`: Folder zawierający pliki związane z frontendem aplikacji, zbudowanym przy użyciu frameworka Quasar.

### FRONTEND


### Struktura Pliku



Kod źródłowy aplikacji Vue jest podzielony na kilka głównych sekcji:

1. **Layout i Nagłówek**
2. **Sidebar**
3. **Formularz dodawania punktów**
4. **Formularz edycji punktów**
5. **Formularz przejazdów**
6. **Interakcje z Mapą**
7. **Skrypty i opcje**

Analizujmy każdą z tych sekcji po kolei, aby zrozumieć jak aplikacja funkcjonuje.

### Layout i Nagłówek



#### Komponent Layoutu



Komponent `q-layout` definiuje wygląd i układ aplikacji. Tworzy podstawowy szkielet struktury oraz umożliwia organizowanie elementów na stronie.



```html

<q-layout view="lHh Lpr lFf">
  <q-header elevated v-show="!enableCoords && !isRemoveDialogShow">
    <q-toolbar>
      <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />
      <q-toolbar-title> WATEventor </q-toolbar-title>
    </q-toolbar>
  </q-header>

```



#### Nagłówek Aplikacji



- **`q-header`**: Nagłówek jest widoczny tylko wtedy, gdy `enableCoords` i `isRemoveDialogShow` są ustawione na `false`. Oznacza to, że nagłówek znika podczas wybierania punktu na mapie lub gdy wyświetlany jest komunikat o usunięciu punktu.

- **`toggleLeftDrawer`**: Kliknięcie przycisku menu wywołuje funkcję `toggleLeftDrawer`, która otwiera lub zamyka boczny panel (Sidebar).



### Sidebar



#### Panel Boczny



Panel boczny (`q-drawer`) zawiera opcje zarządzania aplikacją:



```html

<q-drawer v-model="leftDrawerOpen" show-if-above bordered>
  <div class="q-pa-lg">
    <h5>Opcje</h5>
    <q-list bordered class="prounded-borders">
      <q-expansion-item expand-separator icon="event" label="Typ wydarzenia">
        <q-option-group v-model="group" :options="options" color="primary" class="q-pa-sm" type="checkbox" />
      </q-expansion-item>

```



- **`v-model="leftDrawerOpen"`**: Zmienna sterująca widocznością sidebaru.

- **`q-expansion-item`**: Rozwijane elementy, które zawierają różne opcje zarządzania aplikacją. W tym przypadku są to opcje filtrowania "Typ wydarzenia" oraz "Dodawanie punktów".



#### Opcje Filtracji i Dodawania Punktów



- **`q-option-group`**: Grupuje opcje, w tym przypadku typy wydarzeń.

- **Dodawanie i usuwanie punktów**:

  ```html

  <q-expansion-item expand-separator icon="place" label="Dodawanie punktów">
    <div class="q-pa-sm">
      <q-btn color="primary" text-color="white" label="Dodaj" @click="addDialogShow()" />
      <q-btn color="primary" text-color="white" label="Usuń" @click="removeDialogShow()" />
    </div>
  </q-expansion-item>

  ```



### Formularz Dodawania Punktów



Formularz otwierany w dialogu (`q-dialog`), umożliwiający użytkownikowi dodanie nowego punktu na mapie.


```html

<q-dialog v-model="isAddDialogShow">
  <q-card>
    <q-card-section>
      <h5>Dodaj Punkt</h5>
      <div>
        <q-input v-model="objToSend.name" label="Nazwa"></q-input>
        <q-input v-model="objToSend.description" label="Opis"></q-input>
        <q-input v-model="objToSend.author" label="Autor"></q-input>
        <q-input v-model="objToSend.link" label="Link do szczegółów"></q-input>
        <q-input v-model="objToSend.location" label="Nazwa lokalizacji"></q-input>
        <q-input disable v-model="objToSend.cordinats[0]" label="Współrzedne (Długość)"></q-input>
        <q-input disable v-model="objToSend.cordinats[1]" label="Współrzedne (Szerokość)"></q-input>
        <q-btn @click="enablePointingCoors" color="primary">Ustaw punkt</q-btn>
      </div>
      <q-btn @click="sendNewEvent()" color="primary">Dodaj</q-btn>
    </q-card-section>
  </q-card>
</q-dialog>

```


- **`v-model=“isAddDialogShow”`**: Steruje widocznością dialogu.
- **Pola formularza**: `q-input` dla wprowadzenia nazwy, opisu, autora, linku i innych szczegółów punktu.
- **Współrzędne punktu** są ustawiane ręcznie za pomocą klikania na mapę.

### Formularz Przejazdów

Formularz przejazdów wyświetla wszystkie dane punktu takie jak nazwa, data, opis oraz trasy przejazdu.

```html

<q-dialog v-model="isDriveShow" no-esc-dismiss no-backdrop-dismiss>
  <q-card>
    <q-card-section>
      <q-list>
        <q-item v-for="przejazd in przejazdy" :key="przejazd.id">
          <q-item-section>
            <q-item-label>{{ przejazd.name }}</q-item-label>
            <q-item-label caption>Data: {{ formatDate(przejazd.DateTime) }}</q-item-label>
            <q-item-label caption>Opis: {{ przejazd.description }}</q-item-label>
            <q-item-label caption>Początek trasy: {{ przejazd.startLocation }}</q-item-label>
            <q-item-label caption>Koniec trasy: {{ przejazd.endLocation }}</q-item-label>
            <q-item-label caption>Organizator: {{ przejazd.creator }}</q-item-label>
            <q-item-label caption>Liczba pasażerów: {{ przejazd.passengerNum }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
      <q-btn @click="driveHide()">Zamknij</q-btn>
    </q-card-section>
  </q-card>
</q-dialog>

```

### Interakcje z Mapą

#### Ustawienia Mapa i Widok

Główne komponenty mapy są zdefiniowane przy użyciu `ol-map`, `ol-view`, `ol-tile-layer`, `ol-vector-layer`.


```html

<q-page-container>
  <ol-map :loadTilesWhileAnimating="true" :loadTilesWhileInteracting="true" :style="{ height: '90vh', zIndex: -1, }" @click.prevent="manageClick($event)">
    <ol-view ref="view" :center="center" :rotation="rotation" :zoom="zoom" :projection="projection" />
    <ol-tile-layer>
      <ol-source-osm />
    </ol-tile-layer>
    <ol-vector-layer>
      <ol-source-vector>
        <ol-feature>
          <ol-geom-point :coordinates="objToSend.cordinats"></ol-geom-point>
          <ol-style>
            <ol-style-circle :radius="7">
              <ol-style-fill color="white"></ol-style-fill>
              <ol-style-stroke color="red" :width="3"></ol-style-stroke>
            </ol-style-circle>
          </ol-style>
        </ol-feature>
      </ol-source-vector>
    </ol-vector-layer>
  </ol-map>
</q-page-container>

```

- **`ol-view`** definiuje widok mapy, takie jak centralny punkt, powiększenie i rotacja.
- **Warstwa wektorowa** (`ol-vector-layer`) i źródło wektorowe (`ol-source-vector`) pozwalają na dodawanie i stylizowanie punktów na mapie.
- **Stylizacja punktów**: `ol-style-circle` definiuje wygląd punktu, a `ol-style-stroke` i `ol-style-fill` odpowiednio kolor i szerokość konturu.

#### Kluczowe funkcje zarządzania mapą

- **`manageClick`**: Funkcja obsługująca kliknięcie na mapie w celu ustawienia współrzędnych nowego punktu.
- **`fetchPoints`**: Pobiera punkty geograficzne z serwera i aktualizuje warstwę wektorową.

```js

const manageClick = (event) => {
  if (enableCoords.value) {
    objToSend.value.cordinats = event.coordinate;
    setTimeout(() => {
      disablePointingCoors();
    }, 500);
  }
};

const fetchPoints = async () => {
  try {
    const response = await axios.get(server + "/get-all-events/", {
      params: { typ: group },
      paramsSerializer: (params) => new URLSearchParams(params).toString(),
    });
    const data = JSON.parse(response.data);
    points.value = data.filter((point) => point.longitude && point.latitude);
  } catch (error) {
    console.error("Error fetching points:", error);
  }
};
```

### Skrypty i opcje

#### Zmienne deklaracje
Zmienne zmienne stanu i referencje dla danych eventów oraz konfiguracji aplikacji.

```js

const group = ref(["ogloszenia"]);
let isAddDialogShow = ref(false);
let isRemoveDialogShow = ref(false);
let isEditDialogShow = ref(false);
let isDriveShow = ref(false);
let enableCoords = ref(false);
let objToSend = ref({
  name: "",
  description: "",
  link: "",
  location: "",
  cordinats: [],
  date: Date(),
  isRecursive: false,
  recursiveWeekDay: "",
  author: "",
});
const server = "https://itchy-kids-change.loca.lt/api";
var przejazdy = [];

```



#### Funkcje obsługi zdarzeń i danych

- **`driveShow`**: Pobiera przejazdy z serwera i wyświetla je w dialogu.
- **`formatDate`**: Formatuje datę na czytelny string.
- **`drawHide`, `addDialogShow`, `addDialogHide`, `removeDialogShow`**: Funkcje kontrolujące widoczność odpowiednich dialogów.

```js
async function driveShow() {
    try {
        const response = await fetch(server + "/get-all-przejazdy/");
        const dataString = await response.text();
        const decodedString = JSON.parse(dataString);
        const data = JSON.parse(decodedString);
        if (Array.isArray(data)) {
            przejazdy = data.map(przejazd => ({
                id: przejazd.id,
                DateTime: formatDate(przejazd.DateTime.$date),
                name: przejazd.name,
                description: przejazd.description,
                startLocation: przejazd.startLocation,
                endLocation: przejazd.endLocation,
                creator: przejazd.creator,
                passengerNum: przejazd.passengerNum,
            }));
        } else {
            console.error("Otrzymane dane nie są tablicą:", data);
            przejazdy = [];
        }
    } catch (error) {
        console.error("Błąd podczas pobierania danych:", error);
    }
    isDriveShow.value = true;
}



function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 19).replace("T", " ");
}



function driveHide() { isDriveShow.value = false; }
function addDialogShow() { isAddDialogShow.value = true; }
function addDialogHide() { isAddDialogShow.value = false; }
function removeDialogShow() {
  isRemoveDialogShow.value = true;
  leftDrawerOpen.value = false;
  setTimeout(() => {
    isRemoveDialogShow.value = false;
    leftDrawerOpen.value = true;
  }, 2000);
  objToSend.value.cordinats = [];
}

```

### Reszta funkcji

- **`toggleLeftDrawer`**: Przełącza widoczność bocznego panelu.
- **`clearForm`**: Czyści formularz dodawania punktu.
- **`sendNewEvent`**: Przesyła dane nowego punktu na serwer.

```js

function toggleLeftDrawer() { leftDrawerOpen.value = !leftDrawerOpen.value; }
function clearForm() {
  objToSend.value = {
    name: "",
    description: "",
    link: "",
    location: "",
    cordinats: [],
    date: Date(),
    isRecursive: false,
    recursiveWeekDay: "",
  };
}

const sendNewEvent = () => {
  addDialogHide();
  const formData = new FormData();
  formData.append("id", "423");
  formData.append("type", group.value[0]);
  
  const startDateTime = new Date(objToSend.value.date)
    .toISOString().slice(0, 19).replace("T", " ");
  const endDateTime = new Date(objToSend.value.date)
    .toISOString().slice(0, 19).replace("T", " ");
  
  formData.append("startDateTime", startDateTime);
  formData.append("endDateTime", endDateTime);
  formData.append("recurrence", objToSend.value.isRecursive.toString());
  formData.append("name", objToSend.value.name);
  formData.append("description", objToSend.value.description);
  formData.append("link", objToSend.value.link);
  formData.append("creator", objToSend.value.author);
  formData.append("location", objToSend.value.location);
  formData.append("latitude", objToSend.value.cordinats[1].toString());
  formData.append("longitude", objToSend.value.cordinats[0].toString());
  
  axios.post(server + "/post-add-event/", formData)
    .then(response => {
      console.log("Form data sent successfully:", response.data);
      clearForm();
    })
    .catch(error => {
      console.error("Error sending form data:", error);
    });
};

```

## Technologie

- 🐍 Backend: FastAPI (Python)
- 🌿 Frontend: Quasar Framework (Vue.js)
- 🍃 Baza danych: MongoDB
- 🌐 Mapy: OpenLayers, OpenStreetMap


## Wymagania:
- Python3
- node: "^20 || ^18 || ^16",
- npm: ">= 6.13.4",
- yarn: ">= 1.21.1"
- QuasarCli
- VueCli

## Uruchomienie aplikacji od zera

### Serwer:
```
cd BACKEND
python serwer.py
```

### Aplikacja:
Komendy do instalacji potrzebnych narzędzi
```
npm install -g @vue/cli
npm i -g @quasar/cli
npm install --global yarn
```
Uruchomienie aplikacji
```
cd quasar-project
yarn install
quasar dev
```

