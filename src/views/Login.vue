<script setup>
  const linkDictionary = {
    "google": {redirect: "#", icon: "https://www.svgrepo.com/show/475656/google-color.svg"},
    "discord": {redirect: "#", icon: "https://www.svgrepo.com/show/331368/discord-v2.svg"},
    "facebook": {redirect: "#", icon: "https://www.svgrepo.com/show/135817/facebook.svg"},
    "email-icon": "https://www.svgrepo.com/show/473860/email.svg",
    "password-icon": "https://www.svgrepo.com/show/473879/lock-line.svg",
  };
</script>

<template>
  <div class="main mt-20 unselectable">
    <div class="col"></div>
    <div class="left-center">
      <h1 class="text-[25rem]">Dwello<span class="text-[10rem] align-top leading-loose">®</span></h1>
    </div>
    <div class="right-center">
      <div class="h-[85dvh] w-[45dvh] bg-black rounded-3xl flex flex-col items-center justify-center overflow-hidden">
        <h1 class="text-yellow font-kanit text-[8rem]">Login</h1>
        <form action="/action_page.php">
          <div class="relative">
            <label for="email" class="text-yellow font-kanit font-semibold text-xl">Email</label><br>
            <div class="absolute top-10 left-1" v-if="showEmailIcon">
              <img :src="linkDictionary['email-icon']" alt="Email Icon" class="w-4 h-4">
            </div>
            <input type="text" id="email" name="email" class="w-80 h-10 rounded mb-3 placeholder:text-black focus:outline-none"
              :style="{ 'padding-left': showEmailIcon ? '24px' : '8px' }" placeholder="Email" v-model="emailInput" @input="toggleEmailIconVisibility">
          </div>
          <div class="relative">
            <label for="psswd" class="text-yellow font-kanit font-semibold text-xl">Password</label><br>
            <div class="absolute top-10 left-1" v-if="showPasswordIcon">
              <img :src="linkDictionary['password-icon']" alt="Password Icon" class="w-4 h-4">
            </div>
            <input type="text" id="psswd" name="psswd" class="w-80 h-10 rounded placeholder:text-black focus:outline-none"
            :style="{ 'padding-left': showPasswordIcon ? '24px' : '8px' }" placeholder="Password" v-model="passwordInput" @input="togglePasswordIconVisibility"><br><br>
          </div>
          <div class="text-center">
            <input type="submit" value="Submit" class="bg-yellow text-black text-xl px-8 py-2 rounded font-kanit font-semibold hover:bg-yhover">
          </div>
        </form> 
        <h1 class="text-yellow font-kanit text-[8rem] py-5">Or</h1>
        <a :href="linkDictionary['discord'].redirect">
          <button class="w-80 mb-4 px-4 py-2 border flex gap-9 border-slate-200 rounded text-slate-200 hover:border-slate-400 hover:text-slate-400">
              <img class="w-6 h-6" :src="linkDictionary['discord'].icon" loading="lazy" alt="google logo">
              <span>Continue with Discord</span>
          </button>
        </a>
        <a :href="linkDictionary['google'].redirect">
          <button class="w-80 mb-4 px-4 py-2 border flex gap-9 border-slate-200 rounded text-slate-200 hover:border-slate-400 hover:text-slate-400">
              <img class="w-6 h-6" :src="linkDictionary['google'].icon" loading="lazy" alt="google logo">
              <span>Continue with Google</span>
          </button>
        </a>
        <a :href="linkDictionary['facebook'].redirect">
          <button class="w-80 px-4 py-2 border flex gap-7 border-slate-200 rounded text-slate-200 hover:border-slate-400 hover:text-slate-400">
              <img class="w-6 h-6" :src="linkDictionary['facebook'].icon" loading="lazy" alt="facebook logo">
              <span>Continue with Facebook</span>
          </button>
        </a>
        <a href="#" class="mt-[7rem] text-yellow text-lg hover:text-yhover">Create your Account →</a>
      </div>
    </div>
    <div class="col"></div>
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
      toggleEmailIconVisibility() {
        // No need to do anything here; the computed property takes care of it
      },
      togglePasswordIconVisibility() {
        // No need to do anything here; the computed property takes care of it
      },
    },
  };
</script>