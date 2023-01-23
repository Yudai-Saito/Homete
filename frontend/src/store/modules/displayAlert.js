const state = {
  topAlertState: "",
  bottomAlertState: "",
  displayTopAlert: false,
  displayBottomAlert: false,
};

const getters = {
  topAlertState: (state) => state.topAlertState,
  bottomAlertState: (state) => state.bottomAlertState,
  displayTopAlert: (state) => state.displayTopAlert,
  displayBottomAlert: (state) => state.displayBottomAlert,
};

const actions = {
  invisibleAlert(context) {
    context.commit("updateTopAlert", false);
    context.commit("updateBottomAlert", false);
  },
  alertNewPost(context) {
    context.commit("setTopAlertState", "newPost");
    setTimeout(() => {
      context.commit("updateTopAlert", true);
    }, 1);
  },

  //以下BottomAlert用
  alertError(context) {
    context.commit("setBottomAlertState", "error");
    setTimeout(() => {
      context.commit("updateBottomAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateBottomAlert", false);
    }, 3000);
  },
  alertPostSuccess(context) {
    context.commit("setBottomAlertState", "postSuccess");
    setTimeout(() => {
      context.commit("updateBottomAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateBottomAlert", false);
    }, 3000);
  },
  alertDeletePost(context) {
    context.commit("setBottomAlertState", "deletePost");
    setTimeout(() => {
      context.commit("updateBottomAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateBottomAlert", false);
    }, 3000);
  },
  alertLogin(context) {
    context.commit("setBottomAlertState", "login");
    setTimeout(() => {
      context.commit("updateBottomAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateBottomAlert", false);
    }, 3000);
  },
  alertReportSuccess(context) {
    context.commit("setBottomAlertState", "reportSuccess");
    setTimeout(() => {
      context.commit("updateBottomAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateBottomAlert", false);
    }, 3000);
  },
};

const mutations = {
  setTopAlertState(state, str) {
    state.topAlertState = str;
  },
  setBottomAlertState(state, str) {
    state.bottomAlertState = str;
  },
  updateTopAlert(state, bool) {
    state.displayTopAlert = bool;
  },
  updateBottomAlert(state, bool) {
    state.displayBottomAlert = bool;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
