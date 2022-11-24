const state = {
  alertState: "",
  displayAlert: false,
};

const getters = {
  alertState: (state) => state.alertState,
  displayAlert: (state) => state.displayAlert,
};

const actions = {
  alertPostSuccess(context) {
    context.commit("updateAlertState", "primary");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertPostError(context) {
    context.commit("updateAlertState", "redAccent2");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertLogin(context) {
    context.commit("updateAlertState", "greenLighten2");
    context.commit("updateAlert", true);
    setTimeout(() => {
      context.commit("updateAlert", false);
    }, 3000);
  },
  alertLogout(context) {
    context.commit("updateAlertState", "redAccent2");
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
