const state = {
  contentName: "",
};

const getters = {
  contentName: (state) => state.contentName,
};

const actions = {
  toTimeLine(context) {
    context.commit("updatecontentName", "タイムライン");
  },
  toHistory(context) {
    context.commit("updatecontentName", "ヒストリー");
  },
  toAccount(context) {
    context.commit("updatecontentName", "アカウント");
  },
};

const mutations = {
  updatecontentName(state, name) {
    state.contentName = name;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
