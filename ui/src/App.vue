<template>
  <div class="flex w-full">
    <div class="flex flex-col h-screen w-1/6 bg-base-300">
      <Sidebar />
      <Sidemenu class="flex-1 overflow-y-auto" />
      <Sideprofile />
    </div>
    <div class="w-5/6 bg-base-200">
      <Navbar />
      <RouterView />
    </div>
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
import Sidebar from "./components/Sidebar.vue";
import Sidemenu from "./components/Sidemenu.vue";
import Sideprofile from "./components/Sideprofile.vue";
</script>

<style scoped></style>
