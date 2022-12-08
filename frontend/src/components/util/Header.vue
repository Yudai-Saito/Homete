<template>
  <v-app-bar
    id="header"
    style="border-bottom: solid #00000080 1px"
    color="#BABDBE"
    fixed
    elevation="0"
  >
    <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
      <v-col id="title" class="text-h5 font-weight-bold" cols="3">
        homete…
      </v-col>
      <v-col id="contentTitle" cols="6" lg="5">
        {{ contentName }}
      </v-col>
      <v-col id="headerBtn" cols="3">
        <v-btn color="#CFD8DC" rounded @click="account" v-if="logged">
          <v-icon color="#494854">mdi-account-cog</v-icon>
          <div>アカウント</div>
        </v-btn>
        <v-btn color="#CFD8DC" rounded @click="login" v-else>
          <v-icon color="#494854">mdi-login-variant</v-icon>
          <div>ログイン</div>
        </v-btn>
      </v-col>
    </v-row>
  </v-app-bar>
</template>

<style>
#header div {
  padding: 0 !important;
}
#title {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  color: #494854;
}
#contentTitle {
  margin: 0;
  padding: 0;
  width: 550px;
  display: flex;
  justify-content: center;
  font-size: 20px;
  font-weight: 900;
  color: #494854;
}
#headerBtn {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
}
#headerBtn button {
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
}
</style>

<script>
export default {
  name: "Header",
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    contentName() {
      return this.$store.getters.contentName;
    },
  },
  data() {
    return {};
  },
  methods: {
    login: function () {
      this.$store.dispatch("visibleLoginOverlay");
    },
    logout: function () {
      this.$store.dispatch("loggedOut");
    },
    account: function () {
      this.$store.dispatch("toAccount");
      if (this.$route.path != "/account") {
        this.$router.push("/account");
      }
    },
  },
};
</script>
