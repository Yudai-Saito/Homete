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
  visiblePlzLoginOverlay(context) {
    context.commit("updateOverlayState", "plzLogin");
  },
  visibleDeletePostOverlay(context) {
    context.commit("updateOverlayState", "deletePost");
  },
  visibleReportPostOverlay(context) {
    context.commit("updateOverlayState", "reportPost");
  },
  visibleDeleteAccountOverlay(context) {
    context.commit("updateOverlayState", "deleteAccount");
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
