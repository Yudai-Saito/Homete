import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import displayAlert from './modules/displayAlert';
import displayLogin from './modules/displayLogin';
import displayPostForm from './modules/displayPostForm';
import logged from './modules/logged';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  strict: process.env.NODE_ENV !== 'production',
  modules: {
    displayAlert,
    displayLogin,
    displayPostForm,
    logged,
  },
  state: {

  },
  mutations: {

  },
  actions: {

  }
})
