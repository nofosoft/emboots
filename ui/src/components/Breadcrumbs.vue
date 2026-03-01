<template>
  <div>
    <div class="flex w-full px-2 breadcrumbs text-xs">
      <ul>
        <li v-for="(crumb, index) in breadcrumbs" :key="index" class="gap-1">
          <Icon icon="foundation:page-filled" style="font-size: 14px" />
          <RouterLink v-if="index !== breadcrumbs.length - 1" :to="crumb.path">
            {{ crumb.title }}
          </RouterLink>
          <span v-else>
            {{ crumb.title }}
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
import { useUIStore } from "@/stores/ui";
import { computed } from "vue";
import { useRoute } from "vue-router";
const ui = useUIStore();
const route = useRoute();

const breadcrumbs = computed(() => {
  return route.matched
    .filter((r) => r.meta && r.meta.title)
    .map((r) => ({
      title: r.meta.title as string,
      path: r.path.startsWith("/") ? r.path : `/${r.path}`,
    }));
});
</script>

<style scoped></style>
