<template>
  <v-app-bar flat style="background-color: bisque">
    <v-app-bar-title
      style="text-transform: uppercase; color: red; text-align: left"
    >
      <router-link to="/" style="text-decoration: none; color: red"
        >dog breed classification
      </router-link>
    </v-app-bar-title>
    <v-btn style="border: 1px solid black">
      <router-link to="/web1" style="text-decoration: none; color: black">
        Classification
      </router-link>
    </v-btn>
  </v-app-bar>
</template>

<script setup>
//
</script>
