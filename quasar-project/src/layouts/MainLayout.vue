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
      <q-list>
        <q-item
          clickable
          tag="a"
          target="_blank"
          v-for="s in semesters"
          :key="s.id"
          @click.stop="s.expanded = !s.expanded"
        >
          <q-item-section>
            <q-item-label>{{ s.title }}</q-item-label>
            <q-list v-show="s.expanded">
              <!-- <q-item-label header> Essential Links </q-item-label> -->

              <q-item
                clickable
                tag="a"
                target="_blank"
                v-for="p in s.projects"
                :key="p.id"
                @click.stop="p.expanded = !p.expanded"
              >
                <q-item-section>
                  <q-item-label>{{ p.shortcut }}</q-item-label>
                  <q-item-label caption>{{ p.title }}</q-item-label>
                  <q-list v-show="p.expanded">
                    <q-item
                      clickable
                      tag="a"
                      target="_blank"
                      v-for="l in p.lessons"
                      :key="l.id"
                      @click.stop="
                        updateRequest({
                          semester: s.id,
                          project: p.id,
                          lesson: l.id,
                        })
                      "
                    >
                      <q-item-section>
                        <q-item-label>{{ l.title }}</q-item-label>
                      </q-item-section>
                    </q-item>
                  </q-list>
                </q-item-section>
              </q-item>
            </q-list>
          </q-item-section>
        </q-item>
      </q-list>
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
