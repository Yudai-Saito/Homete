const state = {
  overlayState: "",
};

const getters = {
  overlayState: (state) => state.overlayState,
};

const actions = {
  invisibleCommonOverlay(context) {
    context.commit("updateOverlayState", "");
  },
  visibleLoginOverlay(context) {
    context.commit("updateOverlayState", "login");
  },
  visibleDeletePostOverlay(context) {
    context.commit("updateOverlayState", "deletePost");
  },
  visibleReportPostOverlay(context) {
    context.commit("updateOverlayState", "reportPost");
  },
};

const mutations = {
  updateOverlayState(state, str) {
    state.overlayState = str;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
