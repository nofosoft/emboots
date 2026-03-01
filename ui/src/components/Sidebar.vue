<template>
  <div>
    <div class="navbar">
      <div class="navbar-start">
        <img :src="EmbootsLogo" alt="Emboots Logo" class="p-1" />
      </div>
      <div class="navbar-center"></div>
      <div class="navbar-end">
        <button class="btn btn-ghost btn-circle">
          <Icon icon="sidekickicons:sidebar-left" style="font-size: 24px" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import EmbootsLogo from "@/assets/emboots_light.png";
import { Icon } from "@iconify/vue";
</script>

<style scoped></style>
