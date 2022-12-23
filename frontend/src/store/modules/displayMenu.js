const state = {
  displayMenu: false,
};

const getters = {
  displayMenu: (state) => state.displayMenu,
};

const actions = {
  invisibleMenu(context) {
    context.commit("updateVisibleMenu", false);
  },
  visibleMenu(context) {
    context.commit("updateVisibleMenu", true);
  },
};

const mutations = {
  updateVisibleMenu(state, bool) {
    state.displayMenu = bool;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
