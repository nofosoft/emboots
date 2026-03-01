import { ref } from "vue";
import { defineStore } from "pinia";

export const useUIStore = defineStore("ui", () => {
  const isMaximized = ref(false);

  const toggleMaximized = () => {
    isMaximized.value = !isMaximized.value;
  };

  return {
    isMaximized,
    toggleMaximized,
  };
});
