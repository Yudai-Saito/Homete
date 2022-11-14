<template>
  <v-card width="400px" height="250px" class="mx-auto mt-5 pa-2 rounded-xl" v-cloak>
    <div>
      <v-btn icon plain text class="closeCardBtn" @click="closeLoginCard">
        <v-icon color="#23282F">mdi-close</v-icon>
      </v-btn>
      <v-card-title class="justify-center">Homete</v-card-title>
      <v-card-text>
        <div>ここに適当なサービスの説明とようこそ的な文章</div>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
          large
          @click="logIn"
          class="text-transform ma-0 pa-0 rounded-lg"
          color="white"
        >
          <img class="svg" src="/assets/google-login-btn.svg" @click="logIn" />
          <div class="loginBtnTxt">Googleでログイン</div>
        </v-btn>
      </v-card-actions>
      <v-card-text>
        <div>ここに注意事項的な文章</div>
      </v-card-text>
    </div>
  </v-card>
</template>

<style>
.closeCardBtn {
  justify-content: center;
  position: absolute;
  left: 350px;
}
.loginBtnTxt {
  color: #494854;
  margin-right: 8px;
  margin-left: 8px;
}
.loadingTxt {
  font-size: 20px;
  font-weight: bold;
  position: relative;
  text-align: center;
  top: 100px;
}
.svg{
  background-image: url("/assets/google-login-btn.svg");
}
</style>

<script>
import {
  getAuth,
  onAuthStateChanged,
} from "firebase/auth";

import axios from "axios";

export default {
  computed: {
    visibleLoginWindow() {
      return this.$store.getter.visibleLoginWindow;
    },
  },
  data() {
    return {
      visibleLoginBtn: false,
    };
  },
  methods: {
    closeLoginCard: function () {
      this.$store.dispatch("toInvisibleLoginWindow");
    },
    logIn: function () {
      this.$router.push("/login");
    },
    //ログアウトだから後で使う。nevermind
    logOut: () => {
      const auth = getAuth();

      onAuthStateChanged(auth, () => {
        auth.signOut().then(() => {
          axios.get("/account/logout", {
            withCredentials: true,
          });
        });
      });
    },
  },
};
</script>

