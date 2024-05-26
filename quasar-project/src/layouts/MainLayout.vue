<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated v-show="!enableCoords && !isRemoveDialogShow">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> WATEventor </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!------------------SIDEBAR----------------------->
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <div class="q-pa-lg">
        <h5>Opcje</h5>
        <q-list bordered class="prounded-borders">
          <q-expansion-item
            expand-separator
            icon="event"
            label="Typ wydarzenia"
          >
            <q-option-group
              v-model="group"
              :options="options"
              @update:model-value="fetchPoints"
              color="primary"
              class="q-pa-sm"
              type="checkbox"
            />
          </q-expansion-item>
        </q-list>
        <q-expansion-item
          expand-separator
          icon="place"
          label="Dodawanie punktów"
        >
          <div class="q-pa-sm">
            <q-btn
              color="primary"
              text-color="white"
              label="Dodaj"
              @click="addDialogShow()"
            />
            <q-btn
              color="primary"
              text-color="white"
              label="Usuń"
              @click="removeDialogShow()"
            />
          </div>
        </q-expansion-item>
        <q-expansion-item
          class="q-pa-sm"
          expand-separator
          icon="local_shipping"
          label="Przejazdy"
        >
          <div class="q-pa-md" style="max-width: 300px">
            <q-input filled v-model="objToSend.date">
              <template v-slot:prepend>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy
                    cover
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-date v-model="date" mask="YYYY-MM-DD HH:mm">
                      <div class="row items-center justify-end">
                        <q-btn
                          v-close-popup
                          label="Close"
                          color="primary"
                          flat
                        />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>

              <template v-slot:append>
                <q-icon name="access_time" class="cursor-pointer">
                  <q-popup-proxy
                    cover
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-time v-model="date" mask="YYYY-MM-DD HH:mm" format24h>
                      <div class="row items-center justify-end">
                        <q-btn
                          v-close-popup
                          label="Close"
                          color="primary"
                          flat
                        />
                        <q-btn
                          v-close-popup
                          label="Okay"
                          color="primary"
                          flat
                        />
                      </div>
                    </q-time>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
          </div>
          <q-btn
            color="primary"
            text-color="white"
            label="Pokaż"
            @click="driveShow()"
          />
        </q-expansion-item>
      </div>
      <!-------------Formularz nowego punkt--------------------->
      <q-dialog v-model="isAddDialogShow">
        <q-card>
          <q-card-section>
            <h5>Dodaj Punkt</h5>
            <div>
              <q-input v-model="objToSend.name" label="Nazwa"></q-input>
              <q-input v-model="objToSend.description" label="Opis"></q-input>
              <q-input v-model="objToSend.author" label="Autor"></q-input>
              <q-input
                v-model="objToSend.link"
                label="Link do szczegółów"
              ></q-input>

              <q-input
                v-model="objToSend.location"
                label="Nazwa lokalizacji"
              ></q-input>
              <q-input
                disable
                v-model="objToSend.cordinats[0]"
                label="Współrzedne (Długość)"
              ></q-input>
              <q-input
                disable
                v-model="objToSend.cordinats[1]"
                label="Współrzedne (Szerokość)"
              ></q-input>
              <q-btn @click="enablePointingCoors" color="primary"
                >Ustaw punkt</q-btn
              >
              <div class="q-pa-md" style="max-width: 300px">
                <q-input filled v-model="objToSend.date">
                  <template v-slot:prepend>
                    <q-icon name="event" class="cursor-pointer">
                      <q-popup-proxy
                        cover
                        transition-show="scale"
                        transition-hide="scale"
                      >
                        <q-date
                          v-model="objToSend.date"
                          mask="YYYY-MM-DD HH:mm"
                        >
                          <div class="row items-center justify-end">
                            <q-btn
                              v-close-popup
                              label="Close"
                              color="primary"
                              flat
                            />
                          </div>
                        </q-date>
                      </q-popup-proxy>
                    </q-icon>
                  </template>

                  <template v-slot:append>
                    <q-icon name="access_time" class="cursor-pointer">
                      <q-popup-proxy
                        cover
                        transition-show="scale"
                        transition-hide="scale"
                      >
                        <q-time
                          v-model="objToSend.date"
                          mask="YYYY-MM-DD HH:mm"
                          format24h
                        >
                          <div class="row items-center justify-end">
                            <q-btn
                              v-close-popup
                              label="Close"
                              color="primary"
                              flat
                            />
                          </div>
                        </q-time>
                      </q-popup-proxy>
                    </q-icon>
                  </template>
                </q-input>
              </div>

              <q-checkbox
                v-model="objToSend.isRecursive"
                label="Czy jest powtarzalne?"
              ></q-checkbox>
              <q-item>
                <q-item-section v-if="objToSend.isRecursive">
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="poniedziałek"
                    label="poniedziałek"
                  ></q-radio>
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="wtorek"
                    label="wtorek"
                  ></q-radio>
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="sroda"
                    label="sroda"
                  ></q-radio>
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="czwartek"
                    label="czwartek"
                  ></q-radio>
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="piatek"
                    label="piatek"
                  ></q-radio>
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="sobota"
                    label="sobota"
                  ></q-radio>
                  <q-radio
                    v-model="objToSend.recursiveWeekDay"
                    val="niedziela"
                    label="niedziela"
                  ></q-radio>
                </q-item-section>
              </q-item>
              <q-btn @click="sendNewEvent()" color="primary">Dodaj</q-btn>
            </div>
          </q-card-section>
        </q-card>
      </q-dialog>

      <q-dialog v-model="isEditDialogShow" no-esc-dismiss no-backdrop-dismiss>
        <!--    Dodac v-for który wyswielti wszystkie rzeczy dodane-->
        <q-list>
          <q-card>
            <q-card-section>
              <q-item>Test</q-item>
              <q-btn @click="editDialogHide()"></q-btn>
            </q-card-section>
          </q-card>
        </q-list>
      </q-dialog>
      <q-dialog v-model="isDriveShow" no-esc-dismiss no-backdrop-dismiss>
        <q-card>
          <q-card-section>
            <q-list>
              <q-item v-for="przejazd in przejazdy" :key="przejazd.id">
                <q-item-section>
                  <q-item-label>{{ przejazd.name }}</q-item-label>
                  <q-item-label caption
                    >Data: {{ formatDate(przejazd.DateTime) }}</q-item-label
                  >
                  <q-item-label caption
                    >Opis: {{ przejazd.description }}</q-item-label
                  >
                  <q-item-label caption
                    >Początek trasy: {{ przejazd.startLocation }}</q-item-label
                  >
                  <q-item-label caption
                    >Koniec trasy: {{ przejazd.endLocation }}</q-item-label
                  >
                  <q-item-label caption
                    >Organizator: {{ przejazd.creator }}</q-item-label
                  >
                  <q-item-label caption
                    >Liczba pasażerów: {{ przejazd.passengerNum }}</q-item-label
                  >
                </q-item-section>
              </q-item>
            </q-list>
            <q-btn @click="driveHide()">Zamknij</q-btn>
          </q-card-section>
        </q-card>
      </q-dialog>
    </q-drawer>
    <q-banner
      v-show="isRemoveDialogShow"
      inline-actions
      rounded
      class="bg-red text-white"
    >
      Usunięto punkt z mapy!
    </q-banner>
    <q-banner
      v-show="enableCoords"
      inline-actions
      rounded
      class="bg-orange text-white"
    >
      Wskaż punkt na mapie
    </q-banner>
    <!-----------------------MAP----------------------->
    <q-page-container>
      <ol-map
        :loadTilesWhileAnimating="true"
        :loadTilesWhileInteracting="true"
        :style="{
          height: '90vh',
          zIndex: -1,
        }"
        @click.prevent="manageClick($event)"
      >
        <ol-view
          ref="view"
          :center="center"
          :rotation="rotation"
          :zoom="zoom"
          :projection="projection"
        />

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
        <ol-interaction-clusterselect
          :pointRadius="2"
          :featureStyle="featureStyle"
        >
          <!-- style of the marked selected from the cluster items after first click on the cluster itself -->
          <ol-style>
            <ol-style-icon :src="markerIcon" :scale="0.05"></ol-style-icon>
          </ol-style>
        </ol-interaction-clusterselect>

        <ol-animated-clusterlayer :animationDuration="50" :distance="40">
          <ol-source-vector ref="vectorsource">
            <ol-feature v-for="point in points" :key="point._id">
              <ol-geom-point
                :coordinates="[
                  parseFloat(point.longitude),
                  parseFloat(point.latitude),
                ]"
              ></ol-geom-point>
            </ol-feature>
          </ol-source-vector>

          <ol-style :overrideStyleFunction="overrideStyleFunction">
            <ol-style-stroke color="red" :width="2"></ol-style-stroke>
            <ol-style-fill color="rgba(255,255,255,0.1)"></ol-style-fill>

            <ol-style-circle :radius="20">
              <ol-style-stroke
                color="black"
                :width="15"
                :lineDash="[]"
                lineCap="butt"
              ></ol-style-stroke>
              <ol-style-fill color="black"></ol-style-fill>
            </ol-style-circle>

            <ol-style-text>
              <ol-style-fill color="white"></ol-style-fill>
            </ol-style-text>
          </ol-style>
        </ol-animated-clusterlayer>
      </ol-map>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue";
import { Style, Stroke, Circle, Fill } from "ol/style";

////////////////SIDEBAR//////////////////////////////
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
const server = "https://thick-icons-sip.loca.lt/api";

var przejazdy = [];

async function driveShow() {
  try {
    const response = await fetch(server + "/get-all-przejazdy/");
    const dataString = await response.text();
    const decodedString = JSON.parse(dataString);
    const data = JSON.parse(decodedString);

    if (Array.isArray(data)) {
      przejazdy = data.map((przejazd) => ({
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
      przejazdy = []; // Przypisz pustą tablicę, jeśli dane są niepoprawne
    }

    console.log(przejazdy);
  } catch (error) {
    console.error("Błąd podczas pobierania danych:", error);
  }
  isDriveShow.value = true;
}

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 19).replace("T", " ");
}
function driveHide() {
  isDriveShow.value = false;
}
function addDialogShow() {
  isAddDialogShow.value = true;
}
function addDialogHide() {
  isAddDialogShow.value = false;
}
function removeDialogShow() {
  isRemoveDialogShow.value = true;
  leftDrawerOpen.value = false;
  setTimeout(() => {
    isRemoveDialogShow.value = false;
    leftDrawerOpen.value = true;
  }, 2000);
  objToSend.value.cordinats = [];
}

function enablePointingCoors() {
  enableCoords.value = true;
  leftDrawerOpen.value = false;
  isAddDialogShow.value = false;
}

function disablePointingCoors() {
  enableCoords.value = false;
  leftDrawerOpen.value = true;
  isAddDialogShow.value = true;
}

const options = ref([
  {
    label: "Koła zainteresowań ",
    value: "kz",
  },
  {
    label: "Imprezy eventy watowe",
    value: "iw",
  },
  {
    label: "Ogłoszenia",
    value: "ogloszenia",
  },
]);
////////////////MAP///////////////////////////
onMounted(() => {
  fetchPoints();
});
defineOptions({
  name: "MainLayout",
});

const center = ref([20.89958, 52.25318]);
const projection = ref("EPSG:4326");
const zoom = ref(15);
const view = ref();
const rotation = ref(0);
const position = ref([]);
const markerIcon = "/src/assets/location-pin.svg";

const points = ref([]);

const featureStyle = () => {
  return [
    new Style({
      stroke: new Stroke({
        color: "#ab34c4",
        width: 2,
        lineDash: [5, 5],
      }),
      image: new Circle({
        radius: 5,
        stroke: new Stroke({
          color: "#ab34c4",
          width: 1,
        }),
        fill: new Fill({
          color: "#ab34c444",
        }),
      }),
    }),
  ];
};

const fetchPoints = async () => {
  try {
    const params = {
      typ: [],
    };
    for (const g of group.value) {
      params[`typ`] = params[`typ`] ? [...params[`typ`], g] : [g];
    }
    console.log(params);

    const response = await axios.get(server + "/get-all-events/", {
      params,
    });

    const data = JSON.parse(response.data);
    console.log(data);
    points.value = data.filter((point) => point.longitude && point.latitude);
  } catch (error) {
    console.error("Error fetching points:", error);
  }
};

const overrideStyleFunction = (feature, style) => {
  const clusteredFeatures = feature.get("features");
  const size = clusteredFeatures.length;

  const color = size > 20 ? "192,0,0" : size > 8 ? "255,128,0" : "0,128,0";
  const radius = Math.max(8, Math.min(size, 20));
  const dash = (2 * Math.PI * radius) / 6;
  const calculatedDash = [0, dash, dash, dash, dash, dash, dash];

  style.getImage().getStroke().setLineDash(dash);
  style
    .getImage()
    .getStroke()
    .setColor("rgba(" + color + ",0.5)");
  style.getImage().getStroke().setLineDash(calculatedDash);
  style
    .getImage()
    .getFill()
    .setColor("rgba(" + color + ",1)");

  style.getImage().setRadius(radius);

  style.getText().setText(size.toString());
  return style;
};

const geoLocChange = (event) => {
  console.log("AAAAA", event);
  position.value = event.target.getPosition();
  view.value?.setCenter(event.target?.getPosition());
};

const manageClick = (event) => {
  if (enableCoords.value) {
    console.log("Clicked coordinates:", event.coordinate);
    objToSend.value.cordinats = event.coordinate;
    setTimeout(() => {
      disablePointingCoors();
    }, 500);
  }
};
///////////////////////////POINT FORM/////////////////////////////////////
const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

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
    author: "",
  };
}

const sendNewEvent = () => {
  addDialogHide();
  const formData = new FormData();
  formData.append("id", "423");
  formData.append("type", group.value[0]);

  // Convert startDateTime and endDateTime to the desired format
  const startDateTime = new Date(objToSend.value.date)
    .toISOString()
    .slice(0, 19)
    .replace("T", " ");
  const endDateTime = new Date(objToSend.value.date)
    .toISOString()
    .slice(0, 19)
    .replace("T", " ");
  console.log(group.value);
  formData.append("type", group.value[0]);
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

  // Send the form data to the endpoint using axios
  axios
    .post(server + "/post-add-event/", formData)
    .then((response) => {
      console.log("Form data sent successfully:", response.data);
      // Clear the form
      clearForm();
      fetchPoints();
    })
    .catch((error) => {
      console.error("Error sending form data:", error);
    });
};
</script>
