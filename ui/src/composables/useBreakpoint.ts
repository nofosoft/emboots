import { ref, onMounted, onUnmounted } from "vue";

export function useBreakpoint() {
  const isSm = ref(false);
  const isMd = ref(false);
  const isLg = ref(false);
  const isXl = ref(false);

  let smQuery: MediaQueryList;
  let mdQuery: MediaQueryList;
  let lgQuery: MediaQueryList;
  let xlQuery: MediaQueryList;

  const update = () => {
    isSm.value = smQuery.matches;
    isMd.value = mdQuery.matches;
    isLg.value = lgQuery.matches;
    isXl.value = xlQuery.matches;
  };

  onMounted(() => {
    smQuery = window.matchMedia("(min-width: 640px)");
    mdQuery = window.matchMedia("(min-width: 768px)");
    lgQuery = window.matchMedia("(min-width: 1024px)");
    xlQuery = window.matchMedia("(min-width: 1280px)");

    update();

    smQuery.addEventListener("change", update);
    mdQuery.addEventListener("change", update);
    lgQuery.addEventListener("change", update);
    xlQuery.addEventListener("change", update);
  });

  onUnmounted(() => {
    smQuery.removeEventListener("change", update);
    mdQuery.removeEventListener("change", update);
    lgQuery.removeEventListener("change", update);
    xlQuery.removeEventListener("change", update);
  });

  return {
    isSm,
    isMd,
    isLg,
    isXl,
  };
}
