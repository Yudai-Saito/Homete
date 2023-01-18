function postsSort(posts) {
  return posts.sort((a, b) => b["post_id"] - a["post_id"]);
}

const state = {
  updatePosts: [],
  userUpdatePosts: [],
  completedPost: [],

  //TODO - この2つで分離したファイルにしたほうが良い気がする
  postId: "",
  processFlag: false,
  postsProcess: "",
};

const getters = {
  postId: (state) => state.postId,
  processFlag: (state) => state.processFlag,
  postsProcess: (state) => state.postsProcess,
  userUpdatePosts: (state) => state.userUpdatePosts,
  updatePosts: (state) => state.updatePosts,
  completedPost: (state) => state.completedPost,
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
  setPostId(state, postId) {
    state.postId = postId;
  },
  updateProcess(state, bool) {
    state.processFlag = bool;
  },
  updatePostsProcess(state, postsProcess) {
    state.postsProcess = postsProcess;
  },
  deleteUserUpdatePosts(state) {
    state.userUpdatePosts = [];
  },
  deleteUpdatePosts(state) {
    state.updatePosts = [];
  },
  addCompletedPost(state, posts) {
    state.completedPost.unshift(posts);
  },
  deleteCompletedPost(state, target) {
    state.completedPost.forEach((item, index) => {
      if (item === target) {
        state.completedPost.splice(index, 1);
      }
    });
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
