<template>
  <div class="h-screen unselectable">
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
          <p class="text-black font-kanit text-[1rem] text-center">No problem! Please enter your password address to receive a link for password reset.</p>
        </div>
        <form action="">
          <div class="relative">
            <label for="password" class="text-yellow font-kanit font-semibold text-xl">Password*</label><br>
            <div class="absolute top-10 left-1" v-if="showPasswordIcon">
              <img src="https://www.svgrepo.com/show/473879/lock-line.svg" alt="Password Icon" class="w-4 h-4">
            </div>
            <input type="password" id="password" name="password" class="w-80 h-10 rounded mb-3 placeholder:text-black focus:outline-none"
              :style="{ 'padding-left': showPasswordIcon ? '24px' : '8px' }" placeholder="Your password" v-model="passwordInput" @input="togglePasswordIconVisibility">
          </div>
          <div class="relative">
            <label for="password" class="text-yellow font-kanit font-semibold text-xl">Confirm password*</label><br>
            <div class="absolute top-10 left-1" v-if="showPasswordIcon">
              <img src="https://www.svgrepo.com/show/473879/lock-line.svg" alt="Password Icon" class="w-4 h-4">
            </div>
            <input type="password" id="password" name="password" class="w-80 h-10 rounded mb-3 placeholder:text-black focus:outline-none"
              :style="{ 'padding-left': showConfirmPasswordIcon ? '24px' : '8px' }" placeholder="Your password" v-model="confirmPasswordInput" @input="toggleConfirmPasswordIconVisibility">
          </div>
          <div class="flex justify-between mt-4">
            <button @click="goBack" class="font-kanit text-xl px-8 py-2 rounded border-4 border-solid border-black hover:bg-yhover hover:rounded-xl transition-all duration-200 ease-linear">Cancel</button>
            <input type="button" value="Submit" class="bg-black text-yellow text-xl px-8 py-2 rounded font-kanit font-semibold hover:bg-[#141414] hover:rounded-xl transition-all duration-200 ease-linear" @click="submitForm">
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
        passwordInput: "",
        confirmPasswordInput: ""
      };
    },
    computed: {
      showPasswordIcon() {
        return this.passwordInput.trim() === "";
      },
      showConfirmPasswordIcon() {
        return this.confirmPasswordInput.trim() === "";
      },
    },
    methods: {
      togglePasswordIconVisibility() {},
      toggleConfirmPasswordIconVisibility() {},
      goBack() {
        this.$router.go(-1);
      },
      submitForm() {
        if (this.passwordInput !== this.confirmPasswordInput) {
          alert("New password and confirm password do not match.");
          return;
        }

        const token = new URLSearchParams(window.location.search).get("token");

        fetch("http://127.0.0.1:8000/update-password", {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
            Authorization: token,
          },
          body: JSON.stringify({
            new_password: this.passwordInput,
            confirm_password: this.confirmPasswordInput,
          }),
        })
          .then((response) => {
            if (!response.ok) {
              return response.json().then((errorData) => {
                alert(errorData.detail);
                throw new Error(`Error: ${errorData.detail}`);
              });
            }
            return response.json();
          })
          .then((data) => {
            alert("Password updated successfully!");
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      },
    },
  };
</script>