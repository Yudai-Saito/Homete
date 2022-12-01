import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import contentName from "./modules/contentName";
import displayAlert from "./modules/displayAlert";
import displayLogin from "./modules/displayLogin";
import displayPostForm from "./modules/displayPostForm";
import logged from "./modules/logged";
import posts from "./modules/posts";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  strict: process.env.NODE_ENV !== "production",
  modules: {
    contentName,
    displayAlert,
    displayLogin,
    displayPostForm,
    logged,
    posts,
  },
  state: {},
  mutations: {},
  actions: {},
});
