<template>
  <q-expansion-item label="Oferty" icon="key">
    <q-list bordered separator>
      <q-item
        v-for="itm in items"
        :key="itm.id"
        clickable
        v-ripple
        @click="
          item = itm;
          showOfferDialog = true;
        "
      >
        <q-item-section>
          <q-item-label>
            {{ removeHTMLTags(itm.title.rendered) }}
          </q-item-label>
          <q-item-label caption>{{ itm.date }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-expansion-item>
  <q-dialog v-model="showOfferDialog" no-esc-dismiss>
    <!--    Dodac v-for który wyswielti wszystkie rzeczy dodane-->
    <q-list>
      <q-card>
        <q-card-section>
          <div class="text-h6">{{ removeHTMLTags(item.title.rendered) }}</div>
          {{ removeHTMLTags(item.content.rendered) }}
        </q-card-section>
      </q-card>
    </q-list>
  </q-dialog>
</template>
<script setup>
import { ref, onMounted } from "vue";

import axios from "axios";

const items = ref([]);
const item = ref();

const showOfferDialog = ref(false);

const removeHTMLTags = (text) => {
  const t = text
    .replace(/<[^>]*>/g, "")
    .split(";")
    .join(" ");
  return t;
};

// Function to format date

const formatDate = (dateString) => {
  const options = { year: "numeric", month: "long", day: "numeric" };

  return new Date(dateString).toLocaleDateString("pl-PL", options);
};

// Function to fetch data from API

const fetchData = () => {
  axios

    .get("https://kariera.wat.edu.pl/wp-json/wp/v2/posts")

    .then((response) => {
      const data = response.data;
      items.value = data;
    })
    .catch((error) => {
      console.error("There was an error fetching the data!", error);
    });
};

// Fetch data when component is mounted

onMounted(() => {
  fetchData();
});
</script>
