<template>
  <ol-map
    :loadTilesWhileAnimating="true"
    :loadTilesWhileInteracting="true"
    style="height: 400px"
  >
    <ol-view
      ref="view"
      :center="center"
      :rotation="rotation"
      :zoom="zoom"
      :projection="projection"
    />
    <ol-tile-layer>
      <ol-source-osm />
    </ol-tile-layer>

    <ol-interaction-clusterselect
      @select="featureSelected"
      :pointRadius="20"
      :featureStyle="featureStyle"
    >
      <!-- style of the marked selected from the cluster items after first click on the cluster itself -->
      <ol-style>
        <ol-style-icon :src="markerIcon" :scale="0.05"></ol-style-icon>
      </ol-style>
    </ol-interaction-clusterselect>

    <ol-animated-clusterlayer :animationDuration="500" :distance="40">
      <ol-source-vector ref="vectorsource">
        <ol-feature v-for="index in points.length" :key="index">
          <ol-geom-point :coordinates="points[index - 1]"></ol-geom-point>
        </ol-feature>
      </ol-source-vector>

      <ol-style :overrideStyleFunction="overrideStyleFunction">
        <ol-style-stroke color="red" :width="2"></ol-style-stroke>
        <ol-style-fill color="rgba(255,255,255,0.1)"></ol-style-fill>

        <ol-style-circle :radius="20">
          <ol-style-stroke
            color="black"
            :width="15"
            :lineDash="[]"
            lineCap="butt"
          ></ol-style-stroke>
          <ol-style-fill color="black"></ol-style-fill>
        </ol-style-circle>

        <ol-style-text>
          <ol-style-fill color="white"></ol-style-fill>
        </ol-style-text>
      </ol-style>
    </ol-animated-clusterlayer>

  </ol-map>

</template>

<script setup>
import axios from "axios";
import { watch } from "vue";
import { ref, inject } from "vue";
import { Style, Stroke, Circle, Fill } from "ol/style";
import markerIcon from "../assets/location-pin.svg";
import SidebarCheck from "../components/SidebarCheck.vue";

const center = ref([20.89958, 52.25318]);
const projection = ref("EPSG:4326");
const zoom = ref(15);
const rotation = ref(0);

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

watch(
  () => props.whatToShow,
  (newValue, oldValue) => {
    console.log("request sent");
    // axios
    //   .post("lesson", {
    //     faculty: "wcy",
    //     studies: "poli",
    //     semester: newValue.semester.id,
    //     project: newValue.project.id,
    //     lesson: newValue.lesson.id,
    //     token: "iedtrfuhgnsiuojhngf9pios",
    //   })
    //   .then((res) => {
    //     res.forEach((b) => {});
    //   })
    //   .catch((err) => {
    //     console.error(err);
    //   });
  }
);
const featureStyle = () => {
  return [
    new Style({
      stroke: new Stroke({
        color: "#ab34c4",
        width: 2,
        lineDash: [5, 5],
      }),
      image: new Circle({
        radius: 5,
        stroke: new Stroke({
          color: "#ab34c4",
          width: 1,
        }),
        fill: new Fill({
          color: "#ab34c444",
        }),
      }),
    }),
  ];
};

const overrideStyleFunction = (feature, style) => {
  const clusteredFeatures = feature.get("features");
  const size = clusteredFeatures.length;

  const color = size > 20 ? "192,0,0" : size > 8 ? "255,128,0" : "0,128,0";
  const radius = Math.max(8, Math.min(size, 20));
  const dash = (2 * Math.PI * radius) / 6;
  const calculatedDash = [0, dash, dash, dash, dash, dash, dash];

  style.getImage().getStroke().setLineDash(dash);
  style
    .getImage()
    .getStroke()
    .setColor("rgba(" + color + ",0.5)");
  style.getImage().getStroke().setLineDash(calculatedDash);
  style
    .getImage()
    .getFill()
    .setColor("rgba(" + color + ",1)");

  style.getImage().setRadius(radius);

  style.getText().setText(size.toString());
  return style;
};

const featureSelected = (event) => {
  console.log(event);
};
</script>
