<!--<template>
  <main class="min-h-screen bg-blue-100 flex items-center justify-center text-gray-500 text-sm">
      <form
        class="bg-white shadow-lg rounded-md p-5 md:p-10 flex flex-col w-11/12 max-w-lg group"
        novalidate
      >
        <label for="email" class="mb-5">
          <span>Email</span>
          <input
            type="email"
            name="email"
            id="email"
            class="w-full rounded border border-gray-300 bg-inherit p-3 shadow shadow-gray-100 mt-2 appearance-none outline-none text-neutral-800 invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer"
            placeholder=" "
            required
            pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
          />
          <span class="mt-2 hidden text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block">
            Please enter a valid email address
          </span>
        </label>
        <label for="password" class="mb-5">
          <span>Password</span>
          <input
            type="password"
            name="password"
            id="password"
            class="w-full rounded border border-gray-300 bg-inherit p-3 shadow shadow-gray-100 mt-2 appearance-none outline-none text-neutral-800 invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer"
            placeholder=" "
            required
            pattern=".{7,}"
          />
          <span class="mt-2 hidden text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block">
            Your password must be at least 7 characters long
          </span>
        </label>
        <button type="submit" class="mt-5 bg-blue-500 py-3 rounded-md text-white group-invalid:pointer-events-none group-invalid:opacity-50"
        data-twe-ripple-init
        data-twe-ripple-color="light">
          Submit
        </button>
      </form>
    </main>
</template>-->

      
      
<!--<template>
  <main class="min-h-screen bg-blue-100 flex items-center justify-center text-gray-500 text-sm">
    <form
      class="bg-white shadow-lg rounded-md p-5 md:p-10 flex flex-col w-11/12 max-w-lg group"
      novalidate
    >
      <label for="email" class="mb-5 relative">
        <span class="absolute top-1/2 left-3 -translate-y-1/2 text-gray-400 transition-all duration-300 peer-focus:text-blue-500 peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-placeholder-shown:left-5">Email</span>
        <input
          type="email"
          name="email"
          id="email"
          class="w-full rounded border border-gray-300 bg-inherit p-3 shadow shadow-gray-100 mt-2 appearance-none outline-none text-neutral-800 invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer"
          placeholder=" "
          required
          pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
        />
        <span class="mt-2 hidden text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block transition-all duration-300 opacity-0 group-invalid:opacity-100">
          Please enter a valid email address
        </span>
      </label>

      <label for="password" class="mb-5 relative">
        <span class="absolute top-1/2 left-3 -translate-y-1/2 text-gray-400 transition-all duration-300 peer-focus:text-blue-500 peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-placeholder-shown:left-5">Password</span>
        <input
          type="password"
          name="password"
          id="password"
          class="w-full rounded border border-gray-300 bg-inherit p-3 shadow shadow-gray-100 mt-2 appearance-none outline-none text-neutral-800 invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer"
          placeholder=" "
          required
          pattern=".{7,}"
        />
        <span class="mt-2 hidden text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block transition-all duration-300 opacity-0 group-invalid:opacity-100">
          Your password must be at least 7 characters long
        </span>
      </label>

      <button type="submit" class="mt-5 bg-blue-500 py-3 rounded-md text-white group-invalid:pointer-events-none group-invalid:opacity-50 transition-all duration-300 hover:bg-blue-600" data-twe-ripple-init data-twe-ripple-color="light">
        Submit
      </button>
    </form>
  </main>
</template>

<script setup>
  import Field from "../components/InteractiveInputField.vue";

</script>

<template>
  <div class="bg-white w-screen h-screen">
    <div class="py-24 ml-44">
      <Field />
    </div>
    <div class="w-72 ml-44">
      <div class="relative h-10 w-full min-w-[200px]">
        <input
          class="peer h-full w-full rounded-[7px] border border-blue-gray-200 bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-pink-500 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"
          placeholder=" "
        />
        <label class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-400 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-pink-500 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:border-pink-500 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-pink-500 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
          Required
        </label>
      </div>
    </div>
  </div>
</template>-->

<!--<template>
  <div class="w-screen h-screen flex items-center flex-col space-y-40 justify-center">
    <InputField />
    <InputField /> 
  </div>
</template>

<script>
import InputField from "../components/InteractiveInputField.vue";

export default {
  components: {
    InputField,
  },
};
</script>-->

<template>
  <div class="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-100">
    <form @submit.prevent="handleSubmit" class="w-full max-w-sm p-6 bg-white rounded-lg shadow-md">
      <!-- Email Input -->
      <div class="mb-4">
        <label
          :class="{'text-red-500': emailError}"
          class="block mb-2 text-sm font-bold text-gray-700"
          for="email"
        >
          Email
        </label>
        <input
          type="email"
          id="email"
          v-model="email"
          @input="validateEmail"
          :class="{'border-red-500': emailError}"
          class="w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
          placeholder="Enter your email"
        />
        <p v-if="emailError" class="mt-2 text-xs text-red-500">Please enter a valid email address.</p>
      </div>

      <!-- Password Input -->
      <div class="mb-6">
        <label
          :class="{'text-red-500': passwordError}"
          class="block mb-2 text-sm font-bold text-gray-700"
          for="password"
        >
          Password
        </label>
        <input
          type="password"
          id="password"
          v-model="password"
          @input="validatePassword"
          :class="{'border-red-500': passwordError}"
          class="w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
          placeholder="Enter your password"
        />
        <p v-if="passwordError" class="mt-2 text-xs text-red-500">Password does not meet the criteria.</p>

        <!-- Password Criteria -->
        <ul v-if="passwordError" class="mt-2 text-xs">
          <li :class="{'text-green-500': passwordCriteria.length, 'text-red-500': !passwordCriteria.length}">
            Must be at least 8 characters long
          </li>
          <li :class="{'text-green-500': passwordCriteria.uppercase, 'text-red-500': !passwordCriteria.uppercase}">
            Must contain at least one uppercase character
          </li>
          <li :class="{'text-green-500': passwordCriteria.lowercase, 'text-red-500': !passwordCriteria.lowercase}">
            Must contain at least one lowercase character
          </li>
          <li :class="{'text-green-500': passwordCriteria.number, 'text-red-500': !passwordCriteria.number}">
            Must contain at least one number
          </li>
          <li :class="{'text-green-500': passwordCriteria.special, 'text-red-500': !passwordCriteria.special}">
            Must contain at least one special character (e.g., !@#$%^&*)
          </li>
        </ul>
      </div>

      <!-- Submit Button -->
      <div class="flex items-center justify-between">
        <button
          type="submit"
          class="px-4 py-2 font-bold text-white bg-blue-500 rounded hover:bg-blue-700 focus:outline-none focus:shadow-outline"
        >
          Submit
        </button>
      </div>
    </form>
  </div>
  <div class="m-4 relative min-h-10 min-w-12">
    <input
      class="peer h-full w-full rounded-[7px] border-b border-x border-blue-gray-200 bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-pink-500 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"
      placeholder=" "
    />
    <label class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-400 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-pink-500 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:border-pink-500 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-pink-500 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
      Required
    </label>
  </div>

</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      emailError: false,
      passwordError: false,
      passwordCriteria: {
        length: false,
        uppercase: false,
        lowercase: false,
        number: false,
        special: false,
      },
    };
  },
  methods: {
    validateEmail() {
      // Simple email regex pattern
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      this.emailError = !emailPattern.test(this.email);
    },
    validatePassword() {
      // Update password criteria dynamically
      this.passwordCriteria.length = this.password.length >= 8;
      this.passwordCriteria.uppercase = /[A-Z]/.test(this.password);
      this.passwordCriteria.lowercase = /[a-z]/.test(this.password);
      this.passwordCriteria.number = /[0-9]/.test(this.password);
      this.passwordCriteria.special = /[!@#$%^&*(),.?":{}|<>]/.test(this.password);

      // Check if all criteria are met
      this.passwordError = !(
        this.passwordCriteria.length &&
        this.passwordCriteria.uppercase &&
        this.passwordCriteria.lowercase &&
        this.passwordCriteria.number &&
        this.passwordCriteria.special
      );
    },
    handleSubmit() {
      this.validateEmail();
      this.validatePassword();

      // If no errors, proceed to submit
      if (!this.emailError && !this.passwordError) {
        // Redirect or handle successful form submission
        window.location.href = '/';
      }
    },
  },
};
</script>

<style scoped>
/* Custom styles if needed */
</style>
