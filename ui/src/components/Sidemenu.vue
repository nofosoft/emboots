<template>
  <div>
    <ul class="menu w-full">
      <li>
        <RouterLink to="/" class="rounded-full hover:rounded-full">
          <Icon icon="material-symbols:home-rounded" style="font-size: 24px" />
          <span v-if="ui.isMaximized">Home</span>
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/about" class="rounded-full hover:rounded-full">
          <Icon icon="ix:about-filled" style="font-size: 24px" />
          <span v-if="ui.isMaximized">About</span>
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
import { RouterLink } from "vue-router";
import { useUIStore } from "@/stores/ui";

const ui = useUIStore();
</script>

<style scoped></style>
