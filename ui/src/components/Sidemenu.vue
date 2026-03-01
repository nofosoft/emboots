<template>
  <div>
    <ul class="menu w-full">
      <li>
        <RouterLink to="/" class="rounded-full hover:rounded-full">
          <Icon icon="material-symbols:home-rounded" style="font-size: 24px" />
          Home
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/about" class="rounded-full hover:rounded-full">
          <Icon icon="ix:about-filled" style="font-size: 24px" />
          About
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
import { RouterLink } from "vue-router";
</script>

<style scoped></style>
