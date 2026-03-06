<template>
  <div>
    <div class="max-w-3xl mx-auto p-6">
      <!-- HEADER ARTIKEL -->
      <h1 class="text-2xl font-semibold mb-2">
        {{ meta.title }}
      </h1>
      <div class="text-sm opacity-60 mb-6">
        {{ formattedDate }} • {{ meta.category }} • {{ meta.author }} •
        {{ meta.readingTime }}
      </div>

      <!-- CONTENT -->
      <article class="prose lg:prose-xl max-w-none">
        <div v-html="html"></div>
      </article>

      <!-- FOOTER -->
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import { renderMarkdown } from "@/composables/useMarkdown";
import fm from "front-matter";
import { useHead } from "@vueuse/head";

const route = useRoute();

const html = ref("");
const meta = ref<any>({});

const formattedDate = computed(() => {
  if (!meta.value.date) return "";

  return (
    new Date(meta.value.date).toLocaleString("id-ID", {
      timeZone: "Asia/Jakarta",
      year: "numeric",
      month: "long",
      day: "numeric",
    }) + " WIB"
  );
});

// Load markdown post
const loadPost = async () => {
  const modules = import.meta.glob("/src/contents/posts/*.md", {
    query: "?raw",
    import: "default",
  });

  const path = `/src/contents/posts/${route.params.slug}.md`;

  if (modules[path]) {
    const raw: any = await modules[path]();
    const { attributes, body } = fm(raw);
    meta.value = attributes;
    html.value = renderMarkdown(body);
  }
};

onMounted(loadPost);

// update head reactively
const headMeta = computed(() => {
  if (!meta.value.title) return {};

  return {
    title: meta.value.title,
    meta: [
      { name: "description", content: meta.value.description },
      { name: "keywords", content: meta.value.keywords },
      { property: "og:title", content: meta.value.title },
      { property: "og:description", content: meta.value.description },
      { property: "og:type", content: "article" },
      { property: "og:url", content: window.location.href },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: meta.value.title },
      { name: "twitter:description", content: meta.value.description },
    ],
    link: [{ rel: "canonical", href: window.location.href }],
    script: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Article",
          headline: meta.value.title,
          datePublished: meta.value.date,
          author: { "@type": "Person", name: meta.value.author },
          description: meta.value.description,
        }),
      },
    ],
  };
});

// panggil useHead satu kali di setup, reactive mengikuti headMeta
useHead(headMeta);
</script>

<style scoped></style>
