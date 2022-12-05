const state = {
  alertState: "",
  displayAlert: false,
};

const getters = {
  alertState: (state) => state.alertState,
  displayAlert: (state) => state.displayAlert,
};

const actions = {
  alertError(context) {
    context.commit("updateAlertState", "error");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertPostSuccess(context) {
    context.commit("updateAlertState", "postSuccess");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertDeletePost(context) {
    context.commit("updateAlertState", "deletePost");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertLogin(context) {
    context.commit("updateAlertState", "welcomeBack");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertLogout(context) {
    context.commit("updateAlertState", "seeYouAgain");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertDeleteAccount(context) {
    context.commit("updateAlertState", "deleteAccount");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertReportSuccess(context) {
    context.commit("updateAlertState", "reportSuccess");
    context.commit("updateAlert", true);
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
