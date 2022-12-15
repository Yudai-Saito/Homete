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
  aboutState: 0,
};

const getters = {
  contentsKey: (state) => getKeyByValue(contents, state.contentName),
  contentName: (state) => state.contentName,
  aboutState: (state) => state.aboutState,
};

const actions = {
  toTimeLine(context) {
    context.commit("updateContentName", contents["timeline"]);
  },
  toHistory(context) {
    context.commit("updateContentName", contents["history"]);
  },
  toAccount(context) {
    context.commit("updateContentName", contents["account"]);
  },
  toExplanation(context) {
    context.commit("updateContentName", contents["about"]);
    context.commit("updateAboutState", 0);
  },
  toQuestionAnswer(context) {
    context.commit("updateContentName", contents["about"]);
    context.commit("updateAboutState", 1);
  },
  toUserPolicy(context) {
    context.commit("updateContentName", contents["about"]);
    context.commit("updateAboutState", 2);
  },
  toPrivacyPolicy(context) {
    context.commit("updateContentName", contents["about"]);
    context.commit("updateAboutState", 3);
  },
};

const mutations = {
  updateContentName(state, name) {
    state.contentName = name;
  },
  updateAboutState(state, num) {
    state.aboutState = num;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
