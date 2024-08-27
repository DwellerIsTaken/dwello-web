import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";

import { createPotiah } from 'potiah'
import PrimeVue from 'primevue/config';

import App from "./App.vue";

import Home from "./views/Home.vue";
import Docs from "./views/Docs.vue";
import Login from "./views/Login.vue";
import Signup from "./views/Signup.vue";
import NewPassword from "./views/NewPassword.vue";
import UpdatePassword from "./views/UpdatePassword.vue";
import Test from "./views/Test.vue";
import Test2 from "./views/Test2.vue";
import Test3 from "./views/Test3.vue";

import "./style.css";
import "primevue/resources/themes/lara-light-green/theme.css";

const routes = [
  { path: "/", component: Home },
  { path: "/docs", component: Docs },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/send-password", component: NewPassword },
  { path: "/update-password", component: UpdatePassword },
  { path: "/test", component: Test },
  { path: "/test2", component: Test2 },
  { path: "/test3", component: Test3 }
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
