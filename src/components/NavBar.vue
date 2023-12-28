<script setup>
  const navItems = [
    { name: "Home", href: "/" },
    { name: "About", href: "/about" },
    { name: "Support", href: "/support" },
    { name: "Login", href: "/login" },
  ];
</script>

<template>
  <div class="navbar-container unselectable">
    <div class="logo">
      <h1>Dwello<span class="small-r">®</span></h1>
    </div>
    <nav class="navbar">
      <ul v-for="(item, index) in navItems" :key="index">
        <li class="nav-item">
          <a
            class="nav-link underline-btn"
            aria-current="page"
            :href="item.href"
            >{{ item.name }}</a
          >
        </li>
      </ul>
    </nav>
  </div>
</template>
