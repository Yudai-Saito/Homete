const state = {
    isAlertPost:false,
}

const getters = {
    isAlertPost: state => state.isAlertPost,
}

const actions = {
    toFalseAlertPost(context){
        context.commit('updateAlertPost', false);
    },
    toTrueAlertPost(context){
        context.commit('updateAlertPost', true);
    }
}

const mutations = {
    updateAlertPost(state, bool){
        state.isAlertPost = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
