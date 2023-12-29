<script setup>
  const linkDictionary = {
    "google": {redirect: "#", icon: "https://www.svgrepo.com/show/475656/google-color.svg"},
    "discord": {redirect: "#", icon: "https://www.svgrepo.com/show/331368/discord-v2.svg"},
    "facebook": {redirect: "#", icon: "https://www.svgrepo.com/show/135817/facebook.svg"},
  };
  const emailIcon = "https://www.svgrepo.com/show/473860/email.svg";
  const passwordIcon = "https://www.svgrepo.com/show/473879/lock-line.svg";

  const defaultWidth = "w-96";
</script>

<template>
  <div class="main unselectable">
    <div class="left-center">
      <!--<h1 class="text-[20rem]">Dwello<span class="text-[10rem] align-top leading-loose">®</span></h1>-->
      <img
        src="/src/assets/dummy-logo.svg"
        alt="Discord Logo"
        width="900"
        height="500"
      />
    </div>
    <div class="right-center h-screen">
      <div class="h-screen w-[50vw] bg-black flex flex-col items-center justify-center overflow-hidden">
        <h1 class="text-yellow font-kanit text-[11rem]">Login</h1>
        <form action="/action_page.php">
          <div class="relative">
            <label for="email" class="text-yellow font-kanit font-semibold text-3xl">Email</label><br>
            <div class="absolute top-[3.25rem] left-1" v-if="showEmailIcon">
              <img :src="emailIcon" alt="Email Icon" class="w-4 h-4">
            </div>
            <input type="text" id="email" name="email" class="h-12 rounded mb-3 placeholder:text-black placeholder:text-lg focus:outline-none" :class="defaultWidth"
              :style="{ 'padding-left': showEmailIcon ? '24px' : '8px' }" placeholder="Email" v-model="emailInput" @input="toggleEmailIconVisibility">
          </div>
          <div class="relative mb-1">
            <label for="psswd" class="text-yellow font-kanit font-semibold text-3xl">Password</label><br>
            <div class="absolute top-[3.25rem] left-1" v-if="showPasswordIcon">
              <img :src="passwordIcon" alt="Password Icon" class="w-4 h-4">
            </div>
            <input type="text" id="psswd" name="psswd" class="h-12 rounded placeholder:text-black placeholder:text-lg focus:outline-none" :class="defaultWidth"
            :style="{ 'padding-left': showPasswordIcon ? '24px' : '8px' }" placeholder="Password" v-model="passwordInput" @input="togglePasswordIconVisibility"><br>
          </div>
          <a href="/send-password" class="text-yellow text-lg hover:text-yhover">Forgot password?</a>
          <div class="text-center mt-5">
            <input type="submit" value="Submit" class="bg-yellow text-black text-xl px-10 py-3 rounded font-kanit font-semibold hover:bg-yhover">
          </div>
        </form> 
        <div class="relative inline-flex items-center justify-center w-full py-10">
            <hr class="h-px my-8 bg-yellow border-0 " :class="defaultWidth">
            <span class="absolute px-3 text-yellow bg-black font-kanit text-2xl">OR</span>
        </div>
        <a v-for="(link, provider) in linkDictionary" :key="provider" :href="link.redirect">
          <button class="px-4 py-2 text-lg border flex gap-7 items-center justify-center border-slate-200 rounded text-slate-200 hover:border-slate-400 hover:text-slate-400 mb-4" :class="defaultWidth">
            <img class="w-6 h-6 absolute -ml-72" :src="link.icon" loading="lazy" :alt="`${provider} logo`">
            <span>Continue with {{ provider.charAt(0).toUpperCase() + provider.slice(1) }}</span>
          </button>
        </a>
        <a href="/signup" class="mt-[6rem] text-yellow text-xl hover:text-yhover">Create your Account →</a>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        emailInput: "",
        passwordInput: "",
      };
    },
    computed: {
      showEmailIcon() {
        return this.emailInput.trim() === "";
      },
      showPasswordIcon() {
        return this.passwordInput.trim() === "";
      },
    },
    methods: {
      toggleEmailIconVisibility() {},
      togglePasswordIconVisibility() {},
    },
  };
</script>