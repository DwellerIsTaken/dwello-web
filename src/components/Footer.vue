<script setup>
  const linksData = {
    CompanyLinks: [
      { name: "About Us", href: "/" },
      { name: "Our Team", href: "/about" },
      { name: "Careers", href: "/support" },
      { name: "Contact Us", href: "/login" },
    ],
    SocialLinks: [
      { name: "Discord", href: "/" },
      { name: "GitHub", href: "/" },
      { name: "top.gg", href: "/" },
    ],
    ResourceLinks: [
      { name: "Blog", href: "/" },
      { name: "FAQs", href: "/about" },
      { name: "Support", href: "/support" },
    ],
  };
</script>

<template>
  <div class="w-full h-[60vh] flex flex-row fixed items-center pb-72 z-0 bottom-0 left-0 bg-footer text-yellow unselectable">
    <div class="flex flex-row w-screen mt-52">
      <div class="w-1/3 flex flex-col justify-center items-center border-r-[1px] border-solid border-grey">
        <img
          class="pt-[30rem] pb-40"
          src="/src/assets/dummy-logo.svg"
          alt="Discord Logo"
          width="400"
          height="500"
        />
        <p class="text-lg text-grey font-roboto max-w-80 mb-20">Pioneering network optimization that improves speed, reduces latency and congestion – along with full visibility.</p>
      </div>
      <div class="w-2/3 flex justify-between items-start text-[#EFEFEF]">
        <div v-for="(links, category) in linksData" :key="category"
          class="relative w-1/3 h-full pl-20 pt-52 transition-all duration-1000 bg-footer reveal-gradient before:hover:top-0 before:hover:opacity-0">
          <div v-if="category === 'CompanyLinks'" class="relative mb-48 mt-16">
            <h3 class="text-xl text-grey">Company</h3>
          </div>
          <div v-else-if="category === 'SocialLinks'" class="relative mb-48 mt-16">
            <h3 class="text-xl text-grey">Socials</h3>
          </div>
          <div v-else-if="category === 'ResourceLinks'" class="relative mb-48 mt-16">
            <h3 class="text-xl text-grey">Resorce</h3>
          </div>
          <ul v-for="(link, index) in links" :key="index" class="w-full">
            <li>
              <a class="block mb-1 text-xl font-semibold font-kanit transition-transform transform hover:translate-x-8 duration-300" :href="link.href">{{ link.name }}</a>
            </li>
          </ul>
          <div v-if="category === 'CompanyLinks'">
            <div class="relative mt-[11rem]">
              <a href="#" class="text-grey text-xl font-roboto hover:text-[#EFEFEF] transition-colors duration-300">© 2023 Dwello, All rights reserved</a>
            </div>
          </div>
          <div v-if="category === 'SocialLinks'">
            <div class="relative mt-[13rem]">
              <a href="#" class="text-grey text-xl font-roboto hover:text-[#EFEFEF] transition-colors duration-300">Privacy & Policy</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .reveal-gradient::before {
      content: '';
      position: absolute;
      top: -100%;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(to bottom, rgba(19, 19, 22, 0.5), rgba(28, 28, 33, 0)); /* Adjust the gradient colors as needed */
      opacity: 0;
      transition: top 0.5s ease-in-out, opacity 0.3s ease-in-out; /* Adjust the transition durations and timing functions */
  }
  .reveal-gradient:hover::before {
    top: 0;
    opacity: 1;
  }
  .reveal-gradient:not(:hover)::before {
    top: -100%;
    transition: top 0.4s ease-in-out, opacity 0.4s ease-in-out; /* Adjust the transition durations and timing functions */
  }
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
