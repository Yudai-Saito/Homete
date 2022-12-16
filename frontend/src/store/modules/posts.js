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

  addUpdatePosts(state, posts) {
    state.updatePosts.forEach((item) => {
      if (item["post_id"] == posts["post_id"]) {
        item = { ...posts };
      }
    });
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
