<template>
  <div class="flex w-screen h-screen">
    <div v-if="isSm">
      <Sidenav />
    </div>
    <div v-else>
      <div v-if="ui.isPopupMaximized" class="absolute z-1 w-75 shrink-0">
        <Sidenav />
      </div>
      <div v-else></div>
    </div>
    <div class="flex flex-col bg-base-200 w-full overflow-x-auto">
      <Navbar />
      <Breadcrumbs />
      <div class="flex flex-col w-full overflow-x-auto">
        <RouterView />
        <Footers />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
import { useUIStore } from "@/stores/ui";
import Breadcrumbs from "./components/Breadcrumbs.vue";
import Sidenav from "./components/Sidenav.vue";
import { useBreakpoint } from "./composables/useBreakpoint";
import { onMounted, watch } from "vue";
import Footers from "./components/Footers.vue";

const ui = useUIStore();

const { isSm, isMd, isLg } = useBreakpoint();

onMounted(() => {
  if (isSm.value == false) {
    ui.setMaximized();
  } else {
    ui.setMinimized();
    ui.setPopupMinimized();
  }
});

watch(isSm, () => {
  console.log("isSm: ", isSm.value);
  if (isSm.value == false) {
    ui.setMaximized();
  } else {
    ui.setMinimized();
    ui.setPopupMinimized();
  }
});

watch(isMd, () => {
  console.log("isMd: ", isMd.value);
});

watch(isLg, () => {
  console.log("isLg: ", isLg.value);
});
</script>

<style scoped></style>
