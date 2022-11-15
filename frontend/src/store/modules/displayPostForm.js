const state = {
    displayPostForm: false,
}

const getters = {
    displayPostForm: state => state.displayPostForm,
}

const actions = {
    invisiblePostForm(context) {
        context.commit('updateVisiblePostForm', false);
    },
    visiblePostForm(context) {
        context.commit('updateVisiblePostForm', true);
    }
}

const mutations = {
    updateVisiblePostForm(state, bool) {
        state.displayPostForm = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
