<template>
  <footer
    class="footer sm:footer-horizontal bodered border-t border-gray-300 bg-base-200 text-base-content p-10"
  >
    <nav>
      <h6 class="footer-title">INFO</h6>
      <a class="link link-hover">About us</a>
      <a class="link link-hover">Jobs</a>
    </nav>
    <nav>
      <h6 class="footer-title">LEGAL</h6>
      <a class="link link-hover">Terms of use</a>
      <a class="link link-hover">Privacy policy</a>
      <a class="link link-hover">Cookie policy</a>
    </nav>
    <nav>
      <h6 class="footer-title">SERVICES</h6>
      <a class="link link-hover">Forum</a>
      <a class="link link-hover">Kelas Private</a>
      <a class="link link-hover">Hardware Design</a>
      <a class="link link-hover">Firmware Design</a>
      <a class="link link-hover">Blog</a>
    </nav>
    <form>
      <h6 class="footer-title">Contact & Newsletter</h6>
      <fieldset class="w-80">
        <label>Enter your email address</label>
        <div class="join">
          <input
            type="text"
            placeholder="username@site.com"
            class="input input-bordered join-item"
          />
          <button class="btn btn-primary join-item">Subscribe</button>
        </div>
      </fieldset>
    </form>
  </footer>
</template>

<script setup lang="ts"></script>
<style></style>
