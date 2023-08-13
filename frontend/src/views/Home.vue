<template>
  <body>
    <h1>Home Page</h1>

    <PdfViewerSideBySide v-if="pdfOneSrc" :pdfSrc="pdfOneSrc" />
    <input
      type="file"
      @change.prevent="selectFile($event)"
      accept=".docx, .pdf"
    />
  </body>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import PdfViewerSideBySide from "../components/PdfViewerSideBySide.vue";

const pdfOneSrc = ref(null); // Will hold the Blob URL of the selected PDF

const selectFile = async (event) => {
  const input = document.createElement("input");
  input.type = "file";
  input.accept = ".docx, .pdf";
  console.log("here - - ");

  const file = event.target.files[0];

  if (!file) {
    console.error("No file selected");
    return;
  }

  // Convert the selected file into a Blob URL
  pdfOneSrc.value = URL.createObjectURL(file);
  console.log(pdfOneSrc.value);

  sendFileToServer(file);
};

const sendFileToServer = async (file) => {
  const path = "http://127.0.0.1:3000/analyze";

  const formData = new FormData();
  formData.append("file", file);

  console.log(`path: ${path} \t formData: ${formData}`);

  try {
    const response = await axios.post(path, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      withCredentials: true,
    });

    console.log(response.data);
    // Do something with the response
  } catch (error) {
    console.error("An error occurred:", error);
  }
};
</script>
