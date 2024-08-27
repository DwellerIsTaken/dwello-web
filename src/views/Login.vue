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
        <form ref="LoginForm">
          <div class="relative">
            <label for="email" class="text-yellow font-kanit font-semibold text-3xl">Email</label><br>
            <div class="absolute top-[3.25rem] left-1" v-if="showEmailIcon">
              <img :src="emailIcon" alt="Email Icon" class="w-4 h-4">
            </div>
            <input type="email" id="email" name="email" class="h-12 rounded mb-3 placeholder:text-black placeholder:text-lg focus:outline-none" :class="defaultWidth"
              :style="{ 'padding-left': showEmailIcon ? '24px' : '8px' }" placeholder="Email" required v-model="formData.email" @input="toggleEmailIconVisibility">
          </div>
          <div class="relative mb-1">
            <label for="psswd" class="text-yellow font-kanit font-semibold text-3xl">Password</label><br>
            <div class="absolute top-[3.25rem] left-1" v-if="showPasswordIcon">
              <img :src="passwordIcon" alt="Password Icon" class="w-4 h-4">
            </div>
            <input type="text" id="psswd" name="psswd" class="h-12 rounded placeholder:text-black placeholder:text-lg focus:outline-none" :class="defaultWidth"
            :style="{ 'padding-left': showPasswordIcon ? '24px' : '8px' }" placeholder="Password" required v-model="formData.password" @input="togglePasswordIconVisibility"><br>
          </div>
          <a href="/send-password" class="text-yellow text-lg hover:text-yhover">Forgot password?</a>
          <div class="text-center mt-5">
            <input type="button" value="Submit" class="bg-yellow text-black text-xl px-10 py-3 rounded font-kanit font-semibold hover:bg-yhover" @click="submitForm">
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
      formData: {
        email: '',
        password: '',
      },
    };
  },
  computed: {
    showEmailIcon() {
      return this.formData.email.trim() === "";
    },
    showPasswordIcon() {
      return this.formData.password.trim() === "";
    },
  },
  methods: {
    submitForm() {
      const form = this.$refs.LoginForm;
      const formElements = form.elements;

      // Reset custom validity and remove red borders
      for (const element of formElements) {
        element.setCustomValidity('');
        element.style.border = '';
      }

      if (form.checkValidity()) {
        fetch('http://127.0.0.1:8000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.formData),
        })
        .then(response => {
          if (!response.ok) {
            // Handle non-successful response codes here
            if (response.status === 422) {
              // Handle 422 Unprocessable Entity
              return response.json().then(errorData => {
                // Tell them that email form is incorrect
                throw new Error(`Validation error: ${JSON.stringify(errorData)}`);
              });
            } else {
              // Handle other non-successful response codes
              throw new Error(`Server error: ${response.status}`);
            }
          }
          return response.json();
        })
        .then(data => {
          this.$router.push('/');
          localStorage.setItem("token", JSON.stringify(data));
          console.log(data);
          console.log(localStorage.getItem("token"));
        })
        .catch(error => console.error('Error:', error));

      } else {
        for (const element of formElements) {
          if (!element.checkValidity()) {
            // Some styling here or whatever
            element.setCustomValidity('Please fill in this field');
            element.style.border = '2px solid red';
          }
        }
      }
    },
  },
};
</script>

<!--
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
      submitForm() {
        // Send data to the server

        const form = this.$refs.LoginForm;
        const formElements = form.elements;

        // Reset custom validity and remove red borders
        for (const element of formElements) {
          element.setCustomValidity('');
          element.style.border = '';
        }

        // Check if the form is valid before submitting
        if (form.checkValidity()) {
          console.log("yo");
          fetch('http://127.0.0.1:8000/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              email: this.emailInput,
              password: this.passwordInput,
            }),
          })
          .then(response => response.json())
          .then(data => {
            localStorage.setItem("token", JSON.stringify(data));
            console.log(data);
            console.log(localStorage.getItem("token"));
          })
          .catch(error => console.error('Error:', error));

          console.log("posted");
        } else {
          // Highlight invalid fields with red borders
          for (const element of formElements) {
            if (!element.checkValidity()) {
              // Some styling here or whatever
              element.setCustomValidity('Please fill in this field');
              element.style.border = '0.1em solid red';
            }
          }
        }
      },
    },
  };
-->