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
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["timeline"]);
      resolve();
    });
  },
  toHistory(context) {
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["history"]);
      resolve();
    });
  },
  toAccount(context) {
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["account"]);
      resolve();
    });
  },
  toExplanation(context) {
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["about"]);
      context.commit("updateAboutState", 0);
      resolve();
    });
  },
  toQuestionAnswer(context) {
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["about"]);
      context.commit("updateAboutState", 1);
      resolve();
    });
  },
  toUserPolicy(context) {
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["about"]);
      context.commit("updateAboutState", 2);
      resolve();
    });
  },
  toPrivacyPolicy(context) {
    return new Promise((resolve) => {
      context.commit("updateContentName", contents["about"]);
      context.commit("updateAboutState", 3);
      resolve();
    });
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
