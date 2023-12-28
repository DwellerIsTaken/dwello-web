<script setup>
  const linksData = {
    CompanyLinks: [
      { name: "About Us", href: "/" },
      { name: "Our Team", href: "/about" },
      { name: "Careers", href: "/support" },
      { name: "Contact Us", href: "/login" },
    ],
    ProductLinks: [
      { name: "Product", href: "/" },
      { name: "Product", href: "/" },
      { name: "Product", href: "/" },
      { name: "Product", href: "/" },
    ],
    ResourceLinks: [
      { name: "Blog", href: "/" },
      { name: "FAQs", href: "/about" },
      { name: "Support", href: "/support" },
    ],
  };
</script>

<template>
  <div class="main footer unselectable">
    <div class="main-left"></div>
    <div class="center">
      <div class="slogan"><h1>DwelloBot®</h1></div>
      <div class="about-columns">
        <div class="bottom-column" style="width: 27em;">
          <p class="slogan-text">
            In a world marked by constant change, adaptability becomes a cornerstone of success.
            Embrace innovation and challenge the status quo.
            Navigate the complexities with curiosity and resilience.
            Strive for a balance between ambition and mindfulness.
            In every endeavor, foster connections, for genuine relationships fortify the human experience.
          </p>
        </div>
        <div v-for="(links, category) in linksData" :key="category" class="bottom-column">
          <ul v-for="(link, index) in links" :key="index">
            <li class="footer-column-item">
              <a class="footer-link" :href="link.href">{{ link.name }}</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="main-right"></div>
  </div>
</template>

<style scoped>

</style>

<!--
  FIRST FOOTER CSS

  .footer {
    background-color: #161F27;
    color: #f7d938;

    z-index: -1;
    position: fixed;
    bottom: 0;
  }

  .slogan {
    width: 100%;
    margin-top: 1em;
    border-bottom: 2px solid #333333;
}

.slogan h1 {
    font-size: 5em;
}

.slogan-text {
    font-size: 1em;
}

.about-columns {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 50px 0;
    max-width: 1000px;
    max-height: 200px;
}

.bottom-column {
    position: relative;
    height: 100%;
    margin-right: 4em;
}

.bottom-column:last-child {
    margin-right: 0;
}

.bottom-column h3 {
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 10px;
    color: black;
}

.bottom-column ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.footer-link {
    display: block;
    margin-bottom: 5px;
    color: #f7d938;
    text-decoration: none;
    font-size: 25px;
    font-weight: 600;
    transition: color 0.5s ease;
}

.footer-link:hover {
    color: #ccc;
    cursor: pointer;
}

-->
