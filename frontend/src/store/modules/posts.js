const state = {
  post: {},
  formTxt: "",
  dateTime: "",
};

const getters = {
  post: (state) => state.post,
};

const actions = {};

const mutations = {
  unshiftPosts(state, val) {
    state.post = {
      contents: state.formTxt,
      created_at: state.dateTime,
      icon: val.icon,
      name: val.name,
      //post_idがないとv-forでレンダリングされるカードが同じものになる
      post_id: val.post_id,
      post_reactions: [
        {
          count: null,
          reaction: null,
        },
      ],
      user_reaction: null,
    };
  },
  setFormTxt(state, val) {
    state.formTxt = val;
  },
  setDateTime(state, val) {
    state.dateTime = val;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
