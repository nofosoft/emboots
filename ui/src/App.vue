<template>
  <div class="flex w-full">
    <div
      class="flex flex-col h-screen bg-base-300"
      :class="[ui.isMaximized ? 'w-1/6' : null]"
    >
      <Sidebar />
      <Sidemenu class="flex-1 overflow-y-auto" />
      <Sideprofile />
    </div>
    <div class="bg-base-200" :class="[ui.isMaximized ? 'w-5/6' : 'w-full']">
      <Navbar />
      <Breadcrumbs />
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
import { useUIStore } from "@/stores/ui";
import Breadcrumbs from "./components/Breadcrumbs.vue";

const ui = useUIStore();
</script>

<style scoped></style>
