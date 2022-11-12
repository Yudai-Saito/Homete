import Vue from "vue";
import VueRouter from "vue-router";

import Top from "@/views/Top.vue";
import About from "@/views/About.vue"
import Loginloading from "@/views/LoginLoading.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Top",
    component: Top,
    meta: { title: "トップ" },
  },
  {
    path: "/about",
    name: "About",
    component: About,
    meta: { title: "HOMETEとは？" },
  },
  {
    path: "/login",
    name: "Login",
    component: Loginloading,
    meta: { title: "HOMETEとは？" },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});

export default router;
