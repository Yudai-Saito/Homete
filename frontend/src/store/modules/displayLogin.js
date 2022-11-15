const state = {
    displayLogin: false,
}

const getters = {
    displayLogin: state => state.displayLogin,
}

const actions = {
    invisibleLogin(context) {
        context.commit('updateDisplayLogin', false);
    },
    visibleLogin(context) {
        context.commit('updateDisplayLogin', true);
    }
}

const mutations = {
    updateDisplayLogin(state, bool) {
        state.displayLogin = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
