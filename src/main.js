import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";

import { createPotiah } from 'potiah'
import PrimeVue from 'primevue/config';

import App from "./App.vue";

import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Signup from "./views/Signup.vue";
import NewPassword from "./views/NewPassword.vue";
import EnterNewPassword from "./views/EnterNewPassword.vue";
import Test from "./views/Test.vue";

import "./style.css";
import "primevue/resources/themes/lara-light-green/theme.css";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/send-password", component: NewPassword },
  { path: "/renew-password", component: EnterNewPassword },
  { path: "/test", component: Test },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);

const potiah = createPotiah()
app.use(potiah)

app.use(PrimeVue);

app.mount("#app");
