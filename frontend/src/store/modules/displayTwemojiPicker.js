const state = {
  displayTwemojiPicker: false,
  pickerX: 0,
  pickerY: 0,
  emojiBtnClick: {
    click: false,
    currentPostId: null,
    currentReactions: null,
    currentPostList: null,
  },
};

const getters = {
  displayTwemojiPicker: (state) => state.displayTwemojiPicker,
  pickerX: (state) => state.pickerX,
  pickerY: (state) => state.pickerY,
  emojiBtnClick: (state) => state.emojiBtnClick,
};

const actions = {
  clickBtn({ commit }, { x, y, reactions, postList, postId }) {
    const param = {
      pickerX: x,
      pickerY: y,
      currentReactions: reactions,
      currentPostList: postList,
      currentPostId: postId,
    };
    commit("updatePicker", param);
    commit("reverseemojiBtnClick");
  },
};

const mutations = {
  visibleTwemojiPicker(state) {
    state.displayTwemojiPicker = true;
  },
  invisibleTwemojiPicker(state) {
    state.pickerX = 0;
    state.pickerY = 0;
    state.displayTwemojiPicker = false;
    state.emojiBtnClick.click = false;
    state.emojiBtnClick.currentPostId = null;
    state.emojiBtnClick.currentReactions = null;
    state.emojiBtnClick.currentPostList = null;
  },
  updatePicker(state, param) {
    state.pickerX = param.pickerX;
    state.pickerY = param.pickerY;
    state.emojiBtnClick.currentPostId = param.currentPostId;
    state.emojiBtnClick.currentReactions = param.currentReactions;
    state.emojiBtnClick.currentPostList = param.currentPostList;
  },
  reverseemojiBtnClick(state) {
    state.emojiBtnClick.click = !state.emojiBtnClick.click;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
