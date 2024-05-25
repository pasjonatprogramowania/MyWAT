import PSPDFKit from "pspdfkit";

export default {
  name: "PSPDFKit",
  /**
   * The component receives the `pdfFile` prop, which is of type `String` and is required.
   */
  props: {
    wordFile: {
      type: String,
      required: true,
    },
  },
  /**
   * We wait until the template has been rendered to load the document into the library.
   */
  mounted() {
    this.loadPSPDFKit().then((instance) => {
      this.$emit("loaded", instance);
    });
  },
  /**
   * We watch for `wordFile` prop changes and trigger unloading and loading when there's a new document to load.
   */
  watch: {
    wordFile(val) {
      if (val) {
        this.loadPSPDFKit();
      }
    },
  },
  /**
   * Our component has the `loadPSPDFKit` method. This unloads and cleans up the component and triggers document loading.
   */
  methods: {
    async loadPSPDFKit() {
      PSPDFKit.unload(".doc-container");
      return PSPDFKit.load({
        // To access the `pdfFile` from props, use `this` keyword.
        document: this.wordFile,
        container: ".doc-container",
      });
    },
  },

  /**
   * Clean up when the component is unmounted so it's ready to load another document (not needed in this example).
   */
  beforeUnmount() {
    PSPDFKit.unload(".doc-container");
  },
};
