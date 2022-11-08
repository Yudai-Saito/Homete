<template>
  <v-card width="400px" height="250px" class="mx-auto mt-5 pa-2 rounded-xl">
    <div v-if="loginState">
      <v-btn
        icon
        plain
        text
        class="closeCardBtn"
        @click="closeCard"
      >
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
          <img src="@/assets/google-login-btn.svg" @click="logIn" />
          <div class="logInBtnTxt">Googleでログイン</div>
        </v-btn>
      </v-card-actions>
      <v-card-text>
        <div>ここに注意事項的な文章</div>
      </v-card-text>
    </div>
    <div v-else>
      <v-progress-linear indeterminate color="cyan"></v-progress-linear>
      <div class="loadingTxt">ログイン中…</div>
    </div>
  </v-card>
</template>

<style>
.closeCardBtn {
  justify-content: center;
  position: absolute;
  left: 350px;
}
.logInBtn {
  margin-right: 8px;
  margin-left: 8px;
}
.logInBtnTxt {
  color: #494854;
  margin-right: 8px;
  margin-left: 8px;
}
.loadingTxt{
  font-size: 20px;
  font-weight: bold;
  position: relative;
  text-align: center;
  top: 100px;
}
</style>

<script>
import {
  getAuth,
  GoogleAuthProvider,
  signInWithRedirect,
  onAuthStateChanged,
  getIdToken,
} from "firebase/auth";

import axios from "axios";

export default {
  data() {
    return {
      loginState: false,
    };
  },
  methods: {
    logIn: () => {
      const auth = getAuth();
      const provider = new GoogleAuthProvider();

      provider.setCustomParameters({
        prompt: "select_account",
      });

      signInWithRedirect(auth, provider);
    },

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
  beforeCreate() {
    const auth = getAuth();

    onAuthStateChanged(auth, (user) => {
      if (user) {
        const { currentUser } = getAuth();
        getIdToken(currentUser, true).then((token) => {
          axios
            .post(
              "/account/login",
              {
                email: user.email,
              },
              {
                headers: {
                  Authorization: `${token}`,
                },
                withCredentials: true,
              }
            )
            .then(() => {
              //this.$router.push("/");
            })
            .catch(() => {
              //エラー画面処理へ
            });
        });
      } else {
        //ログインしてなければログインボタン出したいのでtrueにする
        this.loginState = true;
      }
    });
  },
};
</script>

