<template>
  <OpenStreetMap
    @gotLocation="actualizeCoors"
    :getCoords="getCoors"
  ></OpenStreetMap>
  <q-dialog
    :show="showLocatePrompt"
    :style="{
      position: 'absolute',
      top: 0,
      left: '50%',
      transform: 'translateX(-50%)',
    }"
  >
    <q-card>
      <q-card-section>
        <div class="text-h6">Alert</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        Wskaż lokalizację swojego wydarzenia
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="OK" color="primary" v-close-popup />
      </q-card-actions>
    </q-card>
  </q-dialog>

  <q-form @submit="sendNewEvent" @reset="onReset" class="q-gutter-md">
    <q-input
      filled
      v-model="name"
      label="Your name *"
      hint="Name and surname"
      lazy-rules
      :rules="[(val) => (val && val.length > 0) || 'Please type something']"
    />

    <q-input
      filled
      type="number"
      v-model="age"
      label="Your age *"
      lazy-rules
      :rules="[
        (val) => (val !== null && val !== '') || 'Please type your age',
        (val) => (val > 0 && val < 100) || 'Please type a real age',
      ]"
    />

    <q-toggle v-model="accept" label="I accept the license and terms" />

    <div>
      <q-btn label="Submit" type="submit" color="primary" />
      <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
    </div>
  </q-form>

  <q-btn
    round
    color="deep-orange"
    icon="edit_location"
    :style="{
      position: 'absolute',
      right: 0,
      bottom: 0,
    }"
    @click="getCoors = true"
  />
  <q-btn
    round
    color="black"
    icon="my_location"
    :style="{
      position: 'absolute',
      right: 0,
      top: '50px',
    }"
  />
</template>

<script setup>
import axios from "axios";
import OpenStreetMap from "../components/OpenStreetMap.vue";

defineOptions({
  name: "IndexPage",
});

let getCoors = ref(false);

const props = defineProps({
  whatToShow: Object,
});

let coors;
let showForm = ref(false);
const actualizeCoors = (e) => {
  coors = e.coordinates;
  showForm.value = true;
};

const sendNewEvent = () => {
  axios
    .post("add-event", {
      type: "wcy",
      beginDate: Date("11-11-2023"),
      endDate: Date("12-11-2023"),
      frequency: "week",
      title: "rfejiorfe",
      description: "iedtrfuhgnsiuojhngf9pios",
      coordinates: coors,
      author: "me",
      placeName: "Sztab",
    })
    .then((res) => {
      res.forEach((b) => {});
    })
    .catch((err) => {
      console.error(err);
    });
};

let showLocatePrompt = ref(false);

const addNewEvent = () => {
  showLocatePrompt.value = true;
};
</script>
