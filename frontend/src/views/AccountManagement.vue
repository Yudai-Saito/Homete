<template>
  <v-app id="artBoard" style="background-color: rgb(255, 248, 225)">
    <Header @isActive="toggleContents" ref="header" />
    <Login />
    <DeleteAccount />
    <div>
      <v-row
        id="contentsFlex"
        justify="center"
        class="mx-auto my-auto"
        no-gutters
      >
        <v-col cols="3" class="d-none d-sm-block">
          <LeftMenu class="SideMenuFixed" />
        </v-col>
        <v-col
          ref="accountMenu"
          cols="12"
          sm="9"
          md="6"
          lg="5"
          id="slideAccountX"
          :class="{ slideAccountXActive: displayMenu }"
          v-touch="{
            right: function () {
              swipeAccountMenuObserve();
            },
          }"
        >
          <div v-if="switchPosts" class="loader">
            <div class="loader-inner ball-pulse-sync">
              <div></div>
              <div></div>
              <div></div>
            </div>
          </div>
          <div v-else>
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
            <v-divider style="width: 90%; margin: 25px auto"></v-divider>
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
          </div>
        </v-col>
        <v-col cols="3" class="d-none d-md-block"></v-col>
      </v-row>
    </div>
    <Footer />
  </v-app>
</template>
<style>
.settingContainer {
  width: 90%;
  text-align: center;
  margin: 0 auto;
}
.settingTitle {
  margin-top: 5px;
  color: #494854;
}
.settingText {
  font-size: 15px;
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
  font-weight: 600;
}

#slideAccountX {
  transition: all 0.4s !important;
  z-index: 0;
  position: relative;
  top: 10vh;
  min-height: 100vh;
}
</style>


<script>
import Header from "@/components/header/Header.vue";
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
    displayMenu() {
      return this.$store.getters.displayMenu;
    },
  },
  data() {
    return {
      isActiveContents: false,
      switchPosts: false,
    };
  },
  directives: {
    twemoji: {
      inserted(el) {
        el.innerHTML = twemoji.parse(el.innerHTML, {
          folder: "svg",
          ext: ".svg",
          base: "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/",
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
      this.switchPosts = true;

      auth.signOut().then(() => {
        axios
          .get("/account/logout", {
            withCredentials: true,
          })
          .then(() => {
            this.$store.dispatch("loggedOut");
            this.$store.dispatch("toTimeLine").then(() => {
              this.$router.push("/");
            });
          });
      });
    },
    toggleContents(bool) {
      this.isActiveContents = bool;
    },
    openMenu() {
      this.$store.dispatch("visibleMenu");
      this.$refs.header.$refs.slideBoard.style.transform = `translateX(0px)`;
      this.$refs.accountMenu.style.opacity = `0.85`;
      this.$refs.header.$refs.slideBoard.style.opacity = `1`;
    },
    closeMenu() {
      this.$store.dispatch("invisibleMenu");
      this.$refs.header.$refs.slideBoard.style.transform = `translateX(-250px)`;
      this.$refs.accountMenu.style.opacity = `1`;
      this.$refs.header.$refs.slideBoard.style.opacity = `0`;
    },
    swipeAccountMenuObserve() {
      this.openMenu();
    },
  },
  created() {
    if (!this.logged) {
      this.$router.push("/");
    }
  },
  watch: {
    displayMenu(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
        this.openMenu();
      } else {
        document.body.style.touchAction = "";
        this.closeMenu();
      }
    },
  },
};
</script>
