<template>
  <div>
    <div
      :class="[
        'flex',
        'items-center',
        'p-4',
        ui.isMaximized ? 'gap-4' : 'gap-0',
      ]"
    >
      <div>
        <img class="size-8 rounded-full" src="https://picsum.photos/200/300" />
      </div>
      <div v-if="ui.isMaximized">
        <div class="text-xs">Abu Abdirrahman Sabil</div>
        <div class="text-xs font-semibold opacity-60">Guest</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
import { useUIStore } from "@/stores/ui";

const ui = useUIStore();
</script>

<style scoped></style>
