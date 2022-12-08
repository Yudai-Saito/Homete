<template>
  <v-app class="artBoard blue-grey lighten-5">
    <Header />
    <Login />
    <DeleteAccount />
    <div>
      <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
        <v-col cols="3">
          <LeftMenu class="SideMenuSticky" />
        </v-col>
        <v-col class="mainContents" cols="6">
          <div class="settingContainer">
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
        <v-col class="SideMenuSticky rightMenu" cols="3"></v-col>
      </v-row>
    </div>
    <Footer />
  </v-app>
</template>
<style>
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
}
.mainContents {
  margin: 0;
  margin-top: 47px;
  margin-bottom: 20px;
  padding: 0;
  width: 550px;
  min-width: 550px;
  max-width: 550px;
}
.rightMenu {
  display: flex;
  height: 100vh;
  min-height: 100vh;
  max-height: 100vh;
  margin: 0;
  padding: 0;
}
.settingContainer {
  width: 100%;
  height: 30%;
  margin-top: 30px;
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
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import Login from "@/components/overlays/Login.vue";
import DeleteAccount from "@/components/overlays/DeleteAccount.vue";
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";
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
  mounted() {
    window.onload = () => {
      this.$store.dispatch("invisiblePostForm");
      this.$store.dispatch("invisibleCommonOverlay");
    };
  },
};
</script>
