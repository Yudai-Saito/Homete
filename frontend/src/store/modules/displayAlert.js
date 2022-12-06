const state = {
  alertState: "",
  displayAlert: false,
};

const getters = {
  alertState: (state) => state.alertState,
  displayAlert: (state) => state.displayAlert,
};

const actions = {
  alertNewPost(context) {
    context.commit("updateAlertState", "newPost");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
  },
  alertError(context) {
    context.commit("updateAlertState", "error");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertPostSuccess(context) {
    context.commit("updateAlertState", "postSuccess");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertDeletePost(context) {
    context.commit("updateAlertState", "deletePost");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertLogin(context) {
    context.commit("updateAlertState", "login");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertLogout(context) {
    context.commit("updateAlertState", "logout");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertDeleteAccount(context) {
    context.commit("updateAlertState", "deleteAccount");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertReportSuccess(context) {
    context.commit("updateAlertState", "reportSuccess");
    setTimeout(() => {
      context.commit("updateAlert", true);
    }, 1);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
};

const mutations = {
  updateAlertState(state, num) {
    state.alertState = num;
  },
  updateAlert(state, bool) {
    state.displayAlert = bool;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
