const state = {
  deletePostId: "",
  deletePostFlag: false,
};

const getters = {
  deletePostId: (state) => state.deletePostId,
  deletePostFlag: (state) => state.deletePostFlag,
};

const actions = {};

const mutations = {
  setDeletePostId(state, postId) {
    state.deletePostId = postId;
  },
  updateDeletePostFlag(state, bool) {
    state.deletePostFlag = bool;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
