<template>
  <div>
    <div class="navbar justify-center">
      <div v-if="ui.isMaximized" class="navbar-start">
        <img :src="Emboots" alt="Emboots Logo" class="p-1" />
      </div>
      <div :class="[ui.isMaximized ? 'navbar-end' : 'navbar-center']">
        <button
          v-if="!ui.isMaximized"
          @click="ui.toggleMaximized()"
          class="btn btn-ghost btn-circle group relative overflow-hidden"
        >
          <img
            :src="EmbootsLogo"
            alt="Emboots Logo"
            class="transition-all duration-300 group-hover:opacity-0 group-hover:scale-75"
          />
          <Icon
            icon="sidekickicons:sidebar-left"
            class="absolute text-2xl opacity-0 scale-75 transition-all duration-300 group-hover:opacity-100 group-hover:scale-100"
          />
        </button>
        <button
          v-else
          @click="ui.toggleMaximized()"
          class="btn btn-ghost btn-circle"
        >
          <Icon icon="sidekickicons:sidebar-left" class="text-2xl" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Emboots from "@/assets/emboots_light.png";
import EmbootsLogo from "@/assets/emboots_logo.png";
import { Icon } from "@iconify/vue";
import { useUIStore } from "@/stores/ui";

const ui = useUIStore();
</script>

<style scoped></style>
