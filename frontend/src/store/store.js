import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export const loginState = {
  firstLogin: false,
  distinctLogin: false,
};

export default new Vuex.Store({
  state: loginState,
  mutations: {
    setFirstLogin(state, firstLogin) {
      state.firstLogin = firstLogin;
    },
    setDistinctLogin(state, distinctLogin) {
      state.distinctLogin = distinctLogin;
    },
  },
  actions: {
    setFirstLogin({ commit }, value) {
      commit("setFirstLogin", value);
    },
    setDistinctLogin({ commit }, value) {
      commit("setDistinctLogin", value);
    },
  },
  getters: {
    firstLogin(state) {
      return state.firstLogin;
    },
    distinctLogin(state) {
      return state.distinctLogin;
    },
  },
  // `createPersistedState()`でインスタンス作成。引数に設定を書く
  plugins: [
    createPersistedState({
      ssr: false,
      // ストレージのキーを指定。デフォルトではvuex
      key: "homete",

      // 管理対象のステートを指定。pathsを書かない時は`modules`に書いたモジュールに含まれるステート全て。`[]`の時はどれも保存されない
      paths: ["loginState"],
      // ストレージの種類を指定する。デフォルトではローカルストレージ
      storage: window.localStorage,
    }),
  ],
});
