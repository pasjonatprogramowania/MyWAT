<template>
  <q-expansion-item label="Oferty" icon="key">
    <q-list bordered separator>
      <q-item v-for="item in items" :key="item.id" clickable v-ripple>
        <q-item-section>
          <q-item-label>{{ item.title.rendered }}</q-item-label>
          <q-item-label caption>{{ item.date }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-expansion-item>
</template>
<script setup>

import { ref, onMounted } from 'vue';

import axios from 'axios';



const items = ref([]);



// Function to remove HTML tags

const removeHTMLTags = (text) => {

  return text.replace(/<[^>]*>/g, '');

};



// Function to format date

const formatDate = (dateString) => {

  const options = {year: 'numeric', month: 'long', day: 'numeric'};

  return new Date(dateString).toLocaleDateString('pl-PL', options);

};



// Function to fetch data from API

const fetchData = () => {

  axios

    .get('https://kariera.wat.edu.pl/wp-json/wp/v2/posts')

    .then(response => {

      const data = response.data.map(post => ({

        ...post,

        content: removeHTMLTags(post.content.rendered)

      }));

      items.value = data;

    })

    .catch(error => {

      console.error('There was an error fetching the data!', error);

    });

};



// Fetch data when component is mounted

onMounted(() => {

  fetchData();

});

</script>
