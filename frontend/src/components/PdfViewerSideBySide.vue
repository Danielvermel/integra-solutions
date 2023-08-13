<template>
  <div class="pdf-viewer-container">
    <div class="row m-3">
      <div class="col-6 border pdf-scroll">
        <vue-pdf-embed :source="pdfOneSrc" />
      </div>
      <div class="col-6 border pdf-scroll">
        <vue-pdf-embed :source="pdfTwoSrc" />
      </div>
    </div>
  </div>
</template>

<script setup>
import VuePdfEmbed from "vue-pdf-embed";

const props = defineProps(["pdfOneSrc", "pdfTwoSrc"]);
</script>

<style scoped>
.pdf-viewer-container {
}

.pdf-scroll {
  max-height: 500px; /* Set the maximum height for the scrolling area */
  overflow: auto;
}
</style>
