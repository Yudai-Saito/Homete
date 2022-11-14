const state = {
    visibleLoginWindow: false,
}

const getters = {
    visibleLoginWindow: state => state.visibleLoginWindow,
}

const actions = {
    toInvisibleLoginWindow(context) {
        context.commit('updateVisibleLoginWindow', false);
    },
    toVisibleLoginWindow(context) {
        context.commit('updateVisibleLoginWindow', true);
    }
}

const mutations = {
    updateVisibleLoginWindow(state, bool) {
        state.visibleLoginWindow = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
