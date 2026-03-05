<template>
  <div>
    <div
      class="card w-86 shadow-md text-gray-600 rounded-2xl"
      :style="backgroundStyle"
    >
      <div class="card-body backdrop-blur-md bg-base-200/70 rounded-2xl">
        <span v-if="badge" class="badge badge-xs badge-warning font-bold">
          {{ badge }}
        </span>

        <div class="flex justify-between">
          <h2 class="text-3xl font-bold">
            {{ title }}
          </h2>
          <div class="flex items-end"></div>
        </div>

        <ul class="mt-6 flex flex-col gap-2 text-xs">
          <li
            v-for="(feature, index) in features"
            :key="index"
            class="flex items-center gap-1"
          >
            <Icon icon="mdi:check-bold" style="font-size: 24px" />
            <span>{{ feature }}</span>
          </li>
        </ul>

        <div class="mt-6">
          <button class="btn btn-neutral btn-block">
            {{ buttonText }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
import { computed } from "vue";

interface Props {
  title: string;
  badge?: string;
  features: string[];
  buttonText?: string;
  backgroundImage?: string; // contoh: '@/assets/bg1.jpg'
}

const props = withDefaults(defineProps<Props>(), {
  buttonText: "Join Now",
  backgroundImage: "",
});

const backgroundStyle = computed(() => {
  if (!props.backgroundImage) return {};

  return {
    backgroundImage: `url(${new URL(props.backgroundImage, import.meta.url).href})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };
});
</script>

<style scoped></style>
