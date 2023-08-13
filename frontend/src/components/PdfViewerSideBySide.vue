<template>
  <div class="pdf-viewer-container">
    <div class="pdf-viewer">
      Here
      <vue-pdf-embed :source="pdfSrc" class="pdf-viewer-item" />
    </div>
  </div>
</template>

<script setup>
import VuePdfEmbed from "vue-pdf-embed";

const props = defineProps(["pdfSrc"]);
console.log("- - - - - -- -- -- -- ");
console.log(props.pdfSrc);
</script>
<style scoped>
.pdf-viewer-container {
  display: flex;
  gap: 20px; /* Adjust the gap between the PDF viewers */
}

.pdf-viewer {
  flex: 1;
}

.pdf-viewer-item {
  width: 100%;
  height: 500px; /* Adjust the height as needed */
}
</style>
