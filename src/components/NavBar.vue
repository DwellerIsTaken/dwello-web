<script setup>
  const navItems = [
    { name: "Home", href: "/" },
    { name: "About", href: "/about" },
    { name: "Support", href: "/support" },
    { name: "Login", href: "/login" },
  ];
</script>

<template>
  <div class="flex mt-3 unselectable">
    <div class="w-1/3 flex items-center justify-start">
      <h1 class="text-7xl">Dwello<span class="text-4xl align-top leading-10">®</span></h1>
    </div>
    <nav class="w-2/3 flex justify-between items-center overflow-hidden">
      <ul v-for="(item, index) in navItems" :key="index">
        <li>
          <a
            class="text-5xl font-extrabold relative underline-btn"
            aria-current="page"
            :href="item.href"
            >{{ item.name }}
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<style scoped>
  .underline-btn {
    @apply transition-colors duration-300 ease-in-out;
  }

  .underline-btn::before {
    /* not figured out yet */
    content: '';
    position: absolute;
    width: 0;
    height: 0.1em;
    bottom: 0;
    right: 0;
    margin-bottom: -0.35rem;
    background-color: #000000;
    transition: width 0.4s ease-in-out;
  }

  .underline-btn:hover::before {
    @apply w-full left-0;
  }
</style>