import OpenLayersMap, {
  Geometries,
  Layers,
  Map,
  Sources,
} from "vue3-openlayers";
export default ({ app, router, store }) => {
  app.use(OpenLayersMap);
};
