<template>
  <div class="flex w-screen h-screen">
    <div
      class="flex flex-col h-screen bg-base-200"
      :class="[ui.isMaximized ? 'w-75 shrink-0' : null]"
    >
      <Sidebar />
      <Sidemenu class="flex-1 overflow-y-auto" />
      <Sideprofile />
    </div>
    <div class="flex flex-col bg-base-200 w-full overflow-x-auto">
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
