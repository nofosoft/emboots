<template>
  <div>
    <ul class="menu w-full">
      <li>
        <a class="rounded-full hover:rounded-full">
          <Icon icon="sidekickicons:sidebar-left" style="font-size: 24px" />
          Item 2
        </a>
      </li>
      <li>
        <a class="rounded-full hover:rounded-full">
          <Icon icon="sidekickicons:sidebar-left" style="font-size: 24px" />
          Item 1
        </a>
      </li>
      <li>
        <a class="rounded-full hover:rounded-full">
          <Icon icon="sidekickicons:sidebar-left" style="font-size: 24px" />
          Item 3
        </a>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
</script>

<style scoped></style>
