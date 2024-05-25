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
import PDF from "pdf-vue3";
import { ref } from "vue";
import SidebarCheck  from "components/SidebarCheck.vue";

defineOptions({
  name: "MainLayout",
});

const props = defineProps({
  allProjects: {
    type: Object,
  },
});

let req = ref({
  semester: 1,
  project: 1,
  lesson: 1,
});

const leftDrawerOpen = ref(false);
const semesters = ref([
  {
    id: 1,
    title: "Semestr IV",
    expanded: false,
    projects: [
      {
        id: 1,
        title: "Modelowanie Matematyczne",
        expanded: false,
        shortcut: "MM",
        lessons: [
          {
            id: 1,
            title: "efwiujr",
          },
          {
            id: 2,
            title: "efrfesrgfwiujr",
          },
        ],
      },
      {
        id: 2,
        title: "Wprowadzenie do Automatyki",
        expanded: false,
        shortcut: "WdA",
        lessons: [
          {
            id: 1,
            title: "hytrfdr",
          },
          {
            id: 2,
            title: "rdszgf",
          },
        ],
      },
    ],
  },
]);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

function updateRequest(newReq) {
  this.req = newReq;
}
</script>
