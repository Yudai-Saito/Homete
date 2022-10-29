import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import counter from './modules/counter';
import reactions from './modules/reactions';
import isLogin from './modules/isLogin';
import isVisiblePostHomete from './modules/isVisiblePostHomete';
import isInputHomete from './modules/isInputHomete'

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  strict: process.env.NODE_ENV !== 'production',
  modules: {
    counter,
    reactions,
    isLogin,
    isVisiblePostHomete,
    isInputHomete,
  },
  state: {

  },
  mutations: {

  },
  actions: {

  }
})
