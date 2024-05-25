<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> Lekturer </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <SidebarCheck @addPoint="console.log('add')"></SidebarCheck>
    </q-drawer>

    <q-page-container>
      <index-page :what-to-show="req" />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import IndexPage from "src/pages/IndexPage.vue";
import axios from "axios";
import { ref } from "vue";
import SidebarCheck from "components/SidebarCheck.vue";

defineOptions({
  name: "MainLayout",
});

const leftDrawerOpen = ref(false);

localStorage.setItem(
  "event",
  JSON.stringify({
    types: [],
    points: [],
    date: Date,
  })
);

localStorage.setItem("getLocation", "false");
localStorage.setItem("getData", "false");
localStorage.setItem("getTypes", "false");

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

const sendNewEvent = () => {
  axios
    .post("add-event", {
      types: newEvent.value.types,
      beginDate: newEvent.value.date,
      endDate: Date("12-11-2023"),
      frequency: "week",
      title: "rfejiorfe",
      description: "iedtrfuhgnsiuojhngf9pios",
      coordinates: newEvent.value.points,
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
</script>
