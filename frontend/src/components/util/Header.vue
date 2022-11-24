<template>
  <v-app-bar
    style="border-bottom: solid #00000080 2px"
    :height="50"
    color="#BABDBE"
    fixed
    dense
    elevation="0"
  >
    <v-toolbar-title class="text-h5 font-weight-bold title">
      homete…
    </v-toolbar-title>
    <v-btn class="headerBtn" color="#CFD8DC" rounded v-if="logged">
      <v-icon color="#494854">mdi-account-cog</v-icon>
      <div>アカウント</div>
    </v-btn>
    <v-btn class="headerBtn" color="#CFD8DC" rounded @click="login" v-else>
      <v-icon color="#494854">mdi-login-variant</v-icon>
      <div>ログイン</div>
    </v-btn>
  </v-app-bar>
</template>

<style>
.title {
  margin-left: 5%;
  color: #494854;
}
.headerBtn {
  margin-left: auto;
  margin-right: 5%;
}
</style>

<script>
export default {
  name: "Header",
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
  },
  data() {
    return {};
  },
  methods: {
    login: function () {
      this.$store.dispatch("visibleLogin");
    },
    logout: function () {
      this.$store.dispatch("loggedOut");
    },
  },
};
</script>
