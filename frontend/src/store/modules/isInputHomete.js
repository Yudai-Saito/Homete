const state = {
    isInputHomete:false,
}

const getters = {
    isInputHomete: state => state.isInputHomete,
}

const actions = {
    toFalseInputHomete(context){
        context.commit('updateInputHomete', false);
    },
    toTrueInputHomete(context){
        context.commit('updateInputHomete', true);
    }
}

const mutations = {
    updateInputHomete(state, bool){
        state.isInputHomete = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
