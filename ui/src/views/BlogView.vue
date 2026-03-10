<template>
  <main class="p-4">
    <div
      v-if="paginatedPosts.length === 0"
      class="text-gray-500 text-center py-12"
    >
      Loading posts...
    </div>

    <div v-else class="space-y-6 grid grid-cols-1 md:grid-cols-2 gap-1">
      <div
        v-for="post in paginatedPosts"
        :key="post.slug"
        class="flex flex-col p-4 m-2 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200"
      >
        <RouterLink
          :to="`/blog/${post.slug}`"
          class="text-2xl font-semibold text-primary hover:underline"
        >
          {{ post.title }}
        </RouterLink>

        <div class="mt-2 text-sm text-gray-500 flex flex-wrap gap-2">
          <span>{{ post.date ? formatDate(post.date) : "" }}</span>
          <span v-if="post.readingTime">• {{ post.readingTime }}</span>
          <span v-if="post.category">• {{ post.category }}</span>
          <span v-if="post.author">• {{ post.author }}</span>
        </div>

        <p class="mt-4 text-gray-700">
          {{ post.preview }}
          <RouterLink
            :to="`/blog/${post.slug}`"
            class="text-primary font-medium hover:underline ml-1"
          >
            Read more
          </RouterLink>
        </p>
      </div>
    </div>

    <div class="flex w-full justify-end mt-8 gap-2">
      <button
        class="btn btn-circle"
        :disabled="currentPage === 1"
        @click="currentPage--"
      >
        <Icon icon="icon-park-outline:left" class="text-2xl" />
        <!-- Prev -->
      </button>

      <button
        v-for="page in totalPages"
        :key="page"
        @click="currentPage = page"
        class="btn btn-circle"
        :class="page === currentPage ? 'bg-primary text-white' : ''"
      >
        {{ page }}
      </button>

      <button
        class="btn btn-circle"
        :disabled="currentPage === totalPages"
        @click="currentPage++"
      >
        <Icon icon="icon-park-outline:right" class="text-2xl" />
        <!-- Next -->
      </button>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import fm from "front-matter";
import { Icon } from "@iconify/vue";

const currentPage = ref(1);
const postsPerPage = 4;

const paginatedPosts = computed(() => {
  const start = (currentPage.value - 1) * postsPerPage;
  const end = start + postsPerPage;
  return posts.value.slice(start, end);
});

const totalPages = computed(() => {
  return Math.ceil(posts.value.length / postsPerPage);
});

// reactive array untuk posts
const posts = ref<any[]>([]);

// helper untuk format date
const formatDate = (dateStr: string) => {
  return new Date(dateStr).toLocaleDateString("id-ID", {
    timeZone: "Asia/Jakarta",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
};

// ambil 100 kata pertama
const getPreview = (content: string, wordCount = 100) => {
  // 1. hapus heading (#, ##, ### ...)
  let text = content.replace(/^#+\s+/gm, "");

  // 2. hapus bold (**text** atau __text__)
  text = text.replace(/(\*\*|__)(.*?)\1/g, "$2");

  // 3. hapus italic (*text* atau _text_)
  text = text.replace(/(\*|_)(.*?)\1/g, "$2");

  // 4. hapus inline code (`code`)
  text = text.replace(/`(.*?)`/g, "$1");

  // 5. hapus code block (```...```)
  text = text.replace(/```[\s\S]*?```/g, "");

  // 6. hapus link [text](url) → text
  text = text.replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");

  // 7. hapus gambar ![alt](url) → alt
  text = text.replace(/!\[([^\]]*)\]\([^)]+\)/g, "$1");

  const words = text.split(/\s+/).slice(0, wordCount);
  return words.join(" ") + (words.length >= wordCount ? "…" : "");
};

// load semua markdown secara dinamis
const loadPosts = async () => {
  try {
    const res = await fetch("/posts/index.json");
    const slugs: string[] = await res.json();

    const promises = slugs.map(async (slug) => {
      const res = await fetch(`/posts/${slug}.md`);
      const raw = await res.text();

      const { attributes, body } = fm(raw);

      const attrs = attributes as Record<string, any>;

      // fallback slug
      if (!attrs.slug) {
        attrs.slug = slug;
      }

      // preview artikel
      attrs.preview = getPreview(body, 50);

      return attrs;
    });

    posts.value = await Promise.all(promises);

    // urutkan berdasarkan date terbaru (jika date ada)
    posts.value.sort((a, b) => {
      if (!a.date) return 1;
      if (!b.date) return -1;
      return a.date > b.date ? -1 : 1;
    });
  } catch (err) {
    console.error("Failed to load posts:", err);
  }
};

// panggil saat component mount
onMounted(loadPosts);
</script>

<style scoped>
/* optional: batasi paragraf preview */
</style>
