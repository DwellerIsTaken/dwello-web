<template>
  <div class="main h-screen unselectable">
    <div class="h-full w-full my-auto flex items-center justify-center">
      <div class="min-w-[35rem] h-[40rem] flex flex-col items-center justify-center border-4 border-solid border-black shadow-2xl">
        <img
          class="mb-10"
          src="/src/assets/dummy-logo.svg"
          alt="Discord Logo"
          width="400"
          height="500"
        />
        <h1 class="text-black font-kanit text-[3rem]">Forgot Password?</h1>
        <div class="max-w-xs">
          <p class="text-black font-kanit text-[1rem] text-center">No problem! Please enter your email address to receive a link for password reset.</p>
        </div>
        <form action="/action_page.php">
          <div class="relative">
            <label for="email" class="text-yellow font-kanit font-semibold text-xl">Email*</label><br>
            <div class="absolute top-10 left-1" v-if="showEmailIcon">
              <img src="https://www.svgrepo.com/show/473860/email.svg" alt="Email Icon" class="w-4 h-4">
            </div>
            <input type="text" id="email" name="email" class="w-80 h-10 rounded mb-3 placeholder:text-black focus:outline-none"
              :style="{ 'padding-left': showEmailIcon ? '24px' : '8px' }" placeholder="Your email" v-model="emailInput" @input="toggleEmailIconVisibility">
          </div>
          <div class="flex justify-between mt-4">
            <button @click="goBack" class="font-kanit text-xl px-8 py-2 rounded border-4 border-solid border-black hover:bg-yhover hover:rounded-xl transition-all duration-200 ease-linear">Cancel</button>
            <input type="submit" value="Submit" class="bg-black text-yellow text-xl px-8 py-2 rounded font-kanit font-semibold hover:bg-[#141414] hover:rounded-xl transition-all duration-200 ease-linear">
          </div>
        </form> 
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        emailInput: "",
      };
    },
    computed: {
      showEmailIcon() {
        return this.emailInput.trim() === "";
      },
    },
    methods: {
      toggleEmailIconVisibility() {},
      goBack() {
        this.$router.go(-1);
      }
    },
  };
</script>