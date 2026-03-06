<template>
  <div
    class="flex flex-col h-screen bg-base-200 bodered border-r border-gray-300 text-gray-600"
    :class="[ui.isMaximized ? 'w-75 shrink-0' : null]"
  >
    <Sidebar />
    <Sidemenu class="flex-1 overflow-y-auto" />
    <Sideprofile />
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
import { useUIStore } from "@/stores/ui";
import Sidebar from "./Sidebar.vue";
import Sidemenu from "./Sidemenu.vue";
import Sideprofile from "./Sideprofile.vue";

const ui = useUIStore();
</script>

<style scoped></style>
