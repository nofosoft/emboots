import { ref } from "vue";
import { defineStore } from "pinia";

export const useUIStore = defineStore("ui", () => {
  const isMaximized = ref(false);
  const isPopupMaximized = ref(false);

  const toggleMaximized = () => {
    isMaximized.value = !isMaximized.value;
  };

  const setMaximized = () => {
    isMaximized.value = true;
  };

  const setMinimized = () => {
    isMaximized.value = false;
  };

  const setPopupMaximized = () => {
    isPopupMaximized.value = true;
  };

  const setPopupMinimized = () => {
    isPopupMaximized.value = false;
  };

  return {
    isMaximized,
    isPopupMaximized,
    toggleMaximized,
    setMaximized,
    setMinimized,
    setPopupMaximized,
    setPopupMinimized,
  };
});
