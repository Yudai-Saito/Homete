import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import contentName from "./modules/contentName";
import displayAlert from "./modules/displayAlert";
import displayCommonOverlay from "./modules/displayCommonOverlay";
import displayPostForm from "./modules/displayPostForm";
import logged from "./modules/logged";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  strict: process.env.NODE_ENV !== "production",
  modules: {
    contentName,
    displayAlert,
    displayCommonOverlay,
    displayPostForm,
    logged,
  },
  state: {},
  mutations: {},
  actions: {},
});
