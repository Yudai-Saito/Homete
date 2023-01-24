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
  deleteUpdatePosts(state) {
    state.updatePosts = [];
  },
  addUserUpdatePosts(state, posts) {
    //WSで裏で取得していた投稿をコピーして、updatePostsは消す
    let userUpdatePosts = JSON.parse(JSON.stringify(state.updatePosts));

    const updatePostIndex = userUpdatePosts.findIndex(
      (updatePost) => updatePost["post_id"] === posts["post_id"]
    );

    if (updatePostIndex !== -1) {
      userUpdatePosts.splice(updatePostIndex, 1, posts);
    } else {
      userUpdatePosts.unshift(posts);
    }

    state.userUpdatePosts = postsSort(userUpdatePosts);
  },
  deleteUserUpdatePosts(state) {
    state.userUpdatePosts = [];
  },
  addCompletedPost(state, posts) {
    state.completedPost.unshift(posts);
  },
  deleteIntexCompletedPost(state, target) {
    state.completedPost.forEach((item, index) => {
      if (item.post_id == target.post_id) {
        state.completedPost.splice(index, 1);
      }
    });
  },
  deleteCompletedPost(state) {
    state.completedPost = [];
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
};

export default {
  state,
  getters,
  actions,
  mutations,
};
