import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";

import store from "./store/store";

import axios from "axios";

import VueCookies from "vue-cookies";
Vue.use(VueCookies);

import { initializeApp } from "firebase/app";
import { firebaseConfig } from "./firebase-config.js";

const firebaseApp = initializeApp(firebaseConfig);
export { firebaseApp };

//axiosを使う際のbaseURLにエンドポイントを設定
axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;
//axiosでpostをする際にデフォルトでContent-Typeがutf-8のJSON形式になるよう設定
axios.defaults.headers.post["Content-Type"] = "application/json;charset=utf-8";
Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
