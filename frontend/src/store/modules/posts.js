const state = {
  updatePosts: [],
  deletePostId: "",
  deletePostFlag: false,
};

const getters = {
  deletePostId: (state) => state.deletePostId,
  deletePostFlag: (state) => state.deletePostFlag,
};

const actions = {};

const mutations = {
  setUpdatePosts(state, posts) {
    const newUpdatePosts = [...state.updatePosts, ...posts];

    state.updatePosts = newUpdatePosts;
  },
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
