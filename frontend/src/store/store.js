import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import contentName from "./modules/contentName";
import displayAlert from "./modules/displayAlert";
import displayCommonOverlay from "./modules/displayCommonOverlay";
import displayMenu from "./modules/displayMenu";
import displayTwemojiPicker from "./modules/displayTwemojiPicker";
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
    displayCommonOverlay,
    displayMenu,
    displayTwemojiPicker,
    displayPostForm,
    logged,
    posts,
  },
  state: {},
  mutations: {},
  actions: {},
});
