const state = {
  deletePostId: "",
  deletePost: {},
  deletePostFlag: false,
};

const getters = {
  deletePostId: (state) => state.deletePostId,
  deletePost: (state) => state.deletePost,
  deletePostFlag: (state) => state.deletePostFlag,
};

const actions = {};

const mutations = {
  updateDeletePostId(state, deletePostId) {
    state.deletePostId = deletePostId;
  },
  setDeletePost(state, post) {
    state.deletePost = post;
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
