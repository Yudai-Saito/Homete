const state = {
    isLogin:false,
}

const getters = {
    isLogin: state => state.isLogin,
}

const actions = {
    toFalse(context){
        context.commit('updateLogin', false);
    },
    toTrue(context){
        context.commit('updateLogin', true);
    }
}

const mutations = {
    updateLogin(state, bool){
        state.isLogin = bool;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
