function postsSort(posts) {
  return posts.sort((a, b) => b["post_id"] - a["post_id"]);
}

const state = {
  updatePosts: [],
  userUpdatePosts: [],
  deletePostId: "",
  deletePostFlag: false,
};

const getters = {
  deletePostId: (state) => state.deletePostId,
  deletePostFlag: (state) => state.deletePostFlag,
  userUpdatePosts: (state) => state.userUpdatePosts,
};

const actions = {};

const mutations = {
  setUpdatePosts(state, posts) {
    let newUpdatePosts = [...state.updatePosts, ...posts];
    newUpdatePosts = postsSort(newUpdatePosts);
    state.updatePosts = newUpdatePosts;
  },
  addUserUpdatePosts(state, posts) {
    //WSで裏で取得していた投稿をコピーして、updatePostsは消す
    state.userUpdatePosts = JSON.parse(JSON.stringify(state.updatePosts));
    state.updatePosts = [];

    const updatePostIndex = state.userUpdatePosts.findIndex(
      (updatePost) => updatePost["post_id"] === posts["post_id"]
    );

    if (state.updatePostIndex !== -1) {
      state.userUpdatePosts.splice(updatePostIndex, 1, posts);
    } else {
      state.userUpdatePosts.unshift(posts);
    }

    state.userUpdatePosts = postsSort(state.userUpdatePosts);
  },
  setDeletePostId(state, postId) {
    state.deletePostId = postId;
  },
  updateDeletePostFlag(state, bool) {
    state.deletePostFlag = bool;
  },
  deleteUserUpdatePosts(state) {
    state.userUpdatePosts = [];
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
