const state = {
    logged: false,
}

const getters = {
    logged: state => state.logged,
}

const actions = {
    loggedIn(context) {
        context.commit('updateLogged', true);
    },
    loggedOut(context) {
        context.commit('updateLogged', false);
    }
}

const mutations = {
    updateLogged(state, bool) {
        state.logged = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
