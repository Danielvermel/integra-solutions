<template>
  <body>
    <h1>Home Page</h1>
    <input type="file" @change="analyzeFile" accept=".docx, .pdf" />
  </body>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const analyzeFile = async (event) => {
  const file = event.target.files[0]; // Get the first selected file

  if (!file) {
    console.error("No file selected");
    return;
  }

  const path = "http://127.0.0.1:3000/analyze";

  const formData = new FormData();
  formData.append("file", file);

  console.log(`path: ${path} \t formData: ${formData}`);

  try {
    const response = await axios.post(path, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      xhrFields: {
        withCredentials: true,
      },
    });

    console.log(response.data);
    // Do something with the response
  } catch (error) {
    console.error("An error occurred:", error);
  }
};
</script>
