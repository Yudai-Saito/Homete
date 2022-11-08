<template>
  <v-app-bar absolute dense elevation="0" color="#BABDBE">
    <v-toolbar-title class="text-h5 font-weight-bold title">
      homete…
    </v-toolbar-title>
    <v-btn class="accountBtn" color="#CFD8DC" rounded v-if="isLogin">
      <v-icon color="#494854">mdi-account-cog</v-icon>
    </v-btn>
    <v-btn class="loginBtn" color="#CFD8DC" rounded @click="login" v-if="!isLogin">
      <v-icon color="#494854">mdi-login-variant</v-icon>
    </v-btn>
    <v-btn class="logoutBtn" color="#CFD8DC" rounded @click="logout" v-else>
      <v-icon color="#494854">mdi-logout-variant</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<style>
.title {
  margin-left: 5%;
  color: #494854;
}
.accountBtn {
  margin-left: auto;
}
.loginBtn {
  margin-left: auto;
  margin-right: 5%;
}
.logoutBtn {
  margin-left: 16px;
  margin-right: 5%;
}
</style>

<script>
export default {
  name: "Header",
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
    };
  },
  methods: {
    login: function(){
      this.$store.dispatch("toTrueLogin")
    },
    logout: function(){
      this.$store.dispatch("toFalseLogin")
    },
  },
}
</script>
