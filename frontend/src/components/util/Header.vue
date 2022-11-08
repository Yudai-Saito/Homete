<template>
  <v-app-bar absolute dense elevation="0" color="#BABDBE">
    <v-toolbar-title class="text-h5 font-weight-bold title">
      homete…
    </v-toolbar-title>
    <v-btn class="accountBtn" color="#CFD8DC" rounded>
      <v-icon color="#494854">mdi-account-cog</v-icon>
    </v-btn>
    <v-btn class="loginBtn" color="#CFD8DC" rounded>
      <v-icon color="#494854">mdi-login-variant</v-icon>
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
  margin-left: 16px;
  margin-right: 5%;
}
</style>
