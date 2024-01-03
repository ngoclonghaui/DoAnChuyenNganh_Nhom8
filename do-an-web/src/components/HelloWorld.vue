<template>
  <v-card-text
    style="
      align-items: center;
      font-size: 35px;
      text-align: center;
       background: linear-gradient(90deg, #d8bfd8, #ffffe0);
    "
  >
    Test Dataset
  </v-card-text>
  <v-container
    fluid
    class="fill-height"
    style="
      background: linear-gradient(45deg, #d8bfd8, #ffffe0);
      margin: 0;
      height: 100vh;
    "
  >
    <image-carousel></image-carousel>
  </v-container>
</template>

<script setup>
import ImageCarousel from "./ImageCarousel.vue";

//
</script>
