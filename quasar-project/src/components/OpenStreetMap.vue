<template>
  <div></div>
</template>

<script setup>
import { ref, inject, onMounted } from "vue";
import { Style, Stroke, Circle, Fill } from "ol/style";
import markerIcon from "../assets/location-pin.svg";
import axios from "axios";

defineOptions({
  name: "OpenStreetMap",
});

const emit = defineEmits(["gotLocation"]);
</script>
