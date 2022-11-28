import Vue from "vue";
import VueRouter from "vue-router";
import Top from "@/views/Top.vue";
import About from "@/views/About.vue";
import Loginloading from "@/views/LoginLoading.vue";
import NotFound from "@/views/NotFound.vue";
import AccountManagement from "@/views/AccountManagement.vue";

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
  {
    path: "/account",
    name: "account",
    component: AccountManagement,
    meta: { title: "アカウント管理" },
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound,
    meta: { title: "404NotFound" },
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
