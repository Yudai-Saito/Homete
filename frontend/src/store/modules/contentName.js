const contents = {
  timeline: "タイムライン",
  history: "ヒストリー",
  account: "アカウント",
  about: "HOMETEについて",
};

const getKeyByValue = (object, value) => {
  return Object.keys(object).find((key) => object[key] === value);
};

const state = {
  contentName: "",
};

const getters = {
  contentsKey: (state) => getKeyByValue(contents, state.contentName),
  contentName: (state) => state.contentName,
};

const actions = {
  toTimeLine(context) {
    context.commit("updatecontentName", contents["timeline"]);
  },
  toHistory(context) {
    context.commit("updatecontentName", contents["history"]);
  },
  toAccount(context) {
    context.commit("updatecontentName", contents["account"]);
  },
  toAbout(context) {
    context.commit("updatecontentName", contents["about"]);
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
