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
      <SidebarCheck></SidebarCheck>
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

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

function updateRequest(newReq) {
  this.req = newReq;
}

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
</script>
