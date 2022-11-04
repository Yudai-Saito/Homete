const state = {
  alertState: 0,
  isAlert: false,
}

const getters = {
  alertState: state => state.alertState,
  isAlert: state => state.isAlert,
}

const actions = {
  alertPost(context) {
    context.commit('updateAlertState', 0);
    context.commit('updateAlert', true);
    setTimeout(() => {
      context.commit('updateAlert', false);
    }, 3000);
  },
  alertLogin(context) {
    context.commit('updateAlertState', 1);
    context.commit('updateAlert', true);
    setTimeout(() => {
      context.commit('updateAlert', false);
    }, 3000);
  },
  alertLogout(context) {
    context.commit('updateAlertState', 2);
    context.commit('updateAlert', true);
    setTimeout(() => {
      context.commit('updateAlert', false);
    }, 3000);
  },
}

const mutations = {
  updateAlertState(state, num) {
    state.alertState = num;
  },
  updateAlert(state, bool) {
    state.isAlert = bool;
  },
}

export default {
  state,
  getters,
  actions,
  mutations
}
