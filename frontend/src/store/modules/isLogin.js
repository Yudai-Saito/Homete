const state = {
    isLogin: false,
}

const getters = {
    isLogin: state => state.isLogin,
}

const actions = {
    toFalseLogin(context) {
        context.commit('updateLogin', false);
    },
    toTrueLogin(context) {
        context.commit('updateLogin', true);
    }
}

const mutations = {
    updateLogin(state, bool) {
        state.isLogin = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
