<template>
  <OpenStreetMap></OpenStreetMap>
</template>

<script setup>
import { ref } from "vue";
import OpenStreetMap from "src/components/OpenStreetMap.vue";


defineOptions({
  name: "IndexPage",
});

const props = defineProps({
  whatToShow: Object,
});

const featureSelected = (event) => {
  console.log(event);
};
</script>
