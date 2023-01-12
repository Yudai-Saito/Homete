import Vue from "vue";
import VueRouter from "vue-router";
import Top from "@/views/Top.vue";
import About from "@/views/About.vue";
import Loginloading from "@/views/LoginLoading.vue";
import NotFound from "@/views/NotFound.vue";
import AccountManagement from "@/views/AccountManagement.vue";
import LandingPage from "@/views/LandingPage.vue";
import SmLandingPage from "@/views/SmLandingPage.vue";

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
    name: "Account",
    component: AccountManagement,
    meta: { title: "アカウント管理" },
  },
  {
    path: "/contact",
    name: "LandingPage",
    component: LandingPage,
  },
  {
    path: "/smcontact",
    name: "SmLandingPage",
    component: SmLandingPage,
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
