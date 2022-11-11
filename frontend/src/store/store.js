import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import isAlert from './modules/isAlert';
import isInputHomete from './modules/isInputHomete';
import isLogin from './modules/isLogin';
import isVisiblePostHomete from './modules/isVisiblePostHomete';
import reactions from './modules/reactions';
import visibleLoginWindow from './modules/visibleLoginWindow';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  strict: process.env.NODE_ENV !== 'production',
  modules: {
    isAlert,
    isInputHomete,
    isLogin,
    isVisiblePostHomete,
    reactions,
    visibleLoginWindow
  },
  state: {

  },
  mutations: {

  },
  actions: {

  }
})
