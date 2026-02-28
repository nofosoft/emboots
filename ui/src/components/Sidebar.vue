<template>
  <div>
    <div class="navbar">
      <div class="navbar-start">
        <button class="btn btn-ghost btn-circle">
          <img :src="EmbootsLogo" alt="Emboots Logo" class="p-2" />
        </button>
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
import EmbootsLogo from "@/assets/emboots_logo.png";
import { Icon } from "@iconify/vue";
</script>

<style scoped></style>
