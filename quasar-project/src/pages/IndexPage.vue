<template>
  <OpenStreetMap></OpenStreetMap>
</template>

<script setup>
import { ref } from "vue";
import OpenStreetMap from "src/components/OpenStreetMap.vue";

const points = ref([
  [21, 52],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
  [20.8, 52.3],
]);

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
