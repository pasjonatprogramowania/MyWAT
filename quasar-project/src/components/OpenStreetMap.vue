<template>
  <ol-map
    :loadTilesWhileAnimating="true"
    :loadTilesWhileInteracting="true"
    :style="{
      height: '90vh',
      zIndex: -1,
    }"
    @click.prevent="manageClick($event)"
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

    <ol-interaction-clusterselect :pointRadius="2" :featureStyle="featureStyle">
      <!-- style of the marked selected from the cluster items after first click on the cluster itself -->
      <ol-style>
        <ol-style-icon :src="markerIcon" :scale="0.05"></ol-style-icon>
      </ol-style>
    </ol-interaction-clusterselect>

    <ol-animated-clusterlayer :animationDuration="50" :distance="40">
      <ol-source-vector ref="vectorsource">
        <ol-feature v-for="index in points.length" :key="index">
          <ol-geom-point
            :coordinates="[points[index - 1].x, points[index - 1].y]"
          ></ol-geom-point>
        </ol-feature>
      </ol-source-vector>

      <!-- <ol-geolocation
        :projection="projection"
        @change:position="geoLocChange"
      /> -->

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
import { ref, inject, onMounted } from "vue";
import { Style, Stroke, Circle, Fill } from "ol/style";
import markerIcon from "../assets/location-pin.svg";

defineOptions({
  name: "OpenStreetMap",
});

const emit = defineEmits(["gotLocation"]);

const center = ref([20.89958, 52.25318]);
const projection = ref("EPSG:4326");
const zoom = ref(15);
const view = ref();
const rotation = ref(0);
const position = ref([]);

const points = ref([
  {
    x: 21,
    y: 52,
  },
  {
    x: 21,
    y: 52,
  },
  {
    x: 21,
    y: 52,
  },
]);
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

const geoLocChange = (event) => {
  console.log("AAAAA", event);
  position.value = event.target.getPosition();
  view.value?.setCenter(event.target?.getPosition());
};

let getCoords = ref(false);

const manageClick = (event) => {
  if (localStorage.getItem("getLocation") == "true") {
    getCoords.value = false;
    console.log("works!", event.coordinate);
    emit("gotLocation", { coordinates: event.coordinate });
  }
};
</script>
