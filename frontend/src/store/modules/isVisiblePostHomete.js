const state = {
    isVisiblePostHomete:false,
}

const getters = {
    isVisiblePostHomete: state => state.isVisiblePostHomete,
}

const actions = {
    toInvisiblePostHomete(context){
        context.commit('updateVisiblePostHomete', false);
    },
    toVisiblePostHomete(context){
        context.commit('updateVisiblePostHomete', true);
    }
}

const mutations = {
    updateVisiblePostHomete(state, bool){
        state.isVisiblePostHomete = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
