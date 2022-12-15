<template>
  <v-app class="artBoard blue-grey lighten-5">
    <Header />
    <Login />
    <DeleteAccount />
    <div>
      <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
        <v-col cols="3" class="d-none d-sm-block">
          <LeftMenu class="SideMenuSticky" />
        </v-col>
        <v-col cols="12" sm="9" md="6" lg="5">
          <div class="settingContainer" style="border-top: none">
            <div class="btnTxt">
              <div
                v-twemoji
                style="width: 20px; margin-right: 5px; margin-top: 10px"
              >
                🚀
              </div>
              <h3 v-twemoji class="settingTitle">ログアウト</h3>
            </div>
            <p class="settingText">
              ログアウトします。また会える日を楽しみにしています。
            </p>
            <v-btn
              class="ma-0 pa-0 settingBtn"
              color="primary"
              x-large
              :elevation="3"
              v-on:click="logout"
            >
              <div class="btnTxt">
                <div v-twemoji style="width: 18px; margin-right: 5px">✈️</div>
                <div>ログアウト</div>
              </div>
            </v-btn>
          </div>
          <div class="settingContainer">
            <div class="btnTxt">
              <div
                v-twemoji
                style="width: 20px; margin-right: 5px; margin-top: 10px"
              >
                🗑
              </div>
              <h3 v-twemoji class="settingTitle">アカウント削除</h3>
            </div>
            <p class="settingText">
              アカウントを削除します。全ての投稿と全てのリアクションが削除されます。
            </p>
            <v-btn
              class="ma-0 pa-0 settingBtn"
              color="error"
              x-large
              :elevation="3"
              @click="displayDeleteAccount"
            >
              <div class="btnTxt">
                <div v-twemoji style="width: 18px; margin-right: 5px">⚠️</div>
                <div>アカウント削除</div>
              </div>
            </v-btn>
          </div>
        </v-col>
        <v-col cols="3" class="d-none d-md-block"></v-col>
      </v-row>
    </div>
    <Footer />
  </v-app>
</template>
<style>
body {
  padding: 0;
}
.artBoard {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.contentsFlex {
  width: 100%;
  flex-wrap: nowrap;
}
.SideMenuSticky {
  position: sticky;
  top: 0;
  flex-wrap: nowrap;
  margin: 0;
  padding: 0;
  justify-content: center;
}

.settingContainer {
  width: 100%;
  height: 30%;
  margin-top: 10vh;
  border-top: solid black 2px;
  text-align: center;
}
.settingTitle {
  margin-top: 10px;
  color: #494854;
}
.settingText {
  font-size: 14px;
  margin: 10px 0;
  color: #494854;
}
.settingBtn {
  height: 40px !important;
}
.btnTxt {
  margin: 0 15px;
  display: flex;
  justify-content: center;
}
</style>


<script>
import Header from "@/components/util/Header.vue";
import Footer from "@/components/footer/Footer.vue";
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import Login from "@/components/overlays/Login.vue";
import DeleteAccount from "@/components/overlays/DeleteAccount.vue";
import twemoji from "twemoji";
import { getAuth } from "firebase/auth";
import axios from "axios";

export default {
  name: "AccountManagement",
  components: {
    Login,
    DeleteAccount,
    LeftMenu,
    Footer,
    Header,
  },
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
  },
  directives: {
    twemoji: {
      inserted(el) {
        el.innerHTML = twemoji.parse(el.innerHTML, {
          folder: "svg",
          ext: ".svg",
        });
      },
    },
  },
  methods: {
    displayDeleteAccount() {
      this.$store.dispatch("visibleDeleteAccountOverlay");
    },
    logout() {
      const auth = getAuth();

      auth.signOut().then(() => {
        axios
          .get("/account/logout", {
            withCredentials: true,
          })
          .then(() => {
            this.$store.dispatch("loggedOut");
            this.$store.dispatch("toTimeLine");
            this.$store.commit("updateAlertState", "logout");
            this.$router.push("/");
            setTimeout(() => {
              this.$store.dispatch("alertLogout");
            }, 500);
          });
      });
    },
  },
};
</script>
