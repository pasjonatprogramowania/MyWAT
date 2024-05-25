<template>
  <div></div>
  <!--TU ZAWARTOŚCI NOTATEK-->
</template>

<script setup>
import axios from "axios";
import PDF from "pdf-vue3";
defineOptions({
  name: "IndexPage",
});
const props = defineProps({
  semester: Number,
  project: Number,
  lesson: Number,
});
</script>
