import Vue from "vue";
import VueRouter from "vue-router";
import Top from "@/views/Top.vue";
import About from "@/views/About.vue";
import Loginloading from "@/views/LoginLoading.vue";
import NotFound from "@/views/NotFound.vue";
import AccountManagement from "@/views/AccountManagement.vue";
import LandingPage from "@/views/LandingPage.vue";
import SmLandingPage from "@/views/SmLandingPage.vue";

// $grid-breakpoints を JavaScript のオブジェクトとして取得
const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "LandingPage",
    component: LandingPage,
    beforeEnter: (to, from, next) => {
      if (window.innerWidth < gridBreakpoints.sm) {
        next({ name: "SmLandingPage" });
      } else {
        next();
      }
    },
  },
  {
    path: "/",
    name: "SmLandingPage",
    component: SmLandingPage,
    beforeEnter: (to, from, next) => {
      if (window.innerWidth >= gridBreakpoints.sm) {
        next({ name: "LandingPage" });
      } else {
        next();
      }
    },
  },
  {
    path: "/top",
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
