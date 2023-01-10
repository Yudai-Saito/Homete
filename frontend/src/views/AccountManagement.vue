<template>
  <v-app id="artBoard" class="blue-grey lighten-5">
    <Header @isActive="toggleContents" />
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
        >
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

#slideAccountX {
  transition: all 0.4s !important;
  z-index: 0;
  position: relative;
  top: 10vh;
  min-height: 100vh;
}
.slideAccountXActive {
  transform: translateX(250px) !important;
  z-index: 0;
  opacity: 0.85;
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

// $grid-breakpoints を JavaScript のオブジェクトとして取得
const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

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
      dragStartX: 0, // タッチ操作開始時のX座標
      dragCurrentX: 0, // 現在のX座標
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

      auth.signOut().then(() => {
        axios
          .get("/account/logout", {
            withCredentials: true,
          })
          .then(() => {
            this.$store.dispatch("loggedOut");
            this.$store.commit("updateAlertState", "logout");
            this.$store.dispatch("toTimeLine").then(() => {
              this.$router.push("/");
              setTimeout(() => {
                this.$store.dispatch("alertLogout");
              }, 500);
            });
          });
      });
    },
    toggleContents(bool) {
      this.isActiveContents = bool;
    },

    //スワイプ開始
    postsTouchStart(event) {
      if (window.matchMedia(`(max-width: ${gridBreakpoints.sm}px)`).matches) {
        this.dragStartX = event.touches[0].clientX;
      }
    },
    //スワイプ中
    postsTouchMove(event) {
      if (window.matchMedia(`(max-width: ${gridBreakpoints.sm}px)`).matches) {
        this.dragCurrentX = event.touches[0].clientX;
        // スライドさせたい要素のスタイルを変更する
        if (this.dragCurrentX - this.dragStartX >= 0) {
          this.$refs.accountMenu.style.transform = `translateX(${
            this.dragCurrentX - this.dragStartX
          }px)`;
          this.$refs.accountMenu.style.opacity = `${
            this.$refs.accountMenu.style.opacity + 1 - 0.005
          }`;
        }
      }
    },
    //スワイプ終了
    postsTouchEnd() {
      if (window.matchMedia(`(max-width: ${gridBreakpoints.sm}px)`).matches) {
        if (this.dragCurrentX - this.dragStartX >= 50) {
          this.$store.dispatch("visibleMenu");
          this.dragStartX = 0;
          this.dragCurrentX = 0;
        } else {
          this.$refs.accountMenu.style.transform = "";
          this.$refs.accountMenu.style.opacity = "";
          this.dragStartX = 0;
          this.dragCurrentX = 0;
        }
      }
    },
  },
  mounted() {
    //画面中央
    // touchstartイベントを監視する
    this.$refs.accountMenu.addEventListener("touchstart", this.postsTouchStart);
    // touchmoveイベントを監視する
    this.$refs.accountMenu.addEventListener("touchmove", this.postsTouchMove);
    // touchendイベントを監視する
    this.$refs.accountMenu.addEventListener("touchend", this.postsTouchEnd);
  },
  beforeDestroy() {
    // イベントの監視を解除する
    this.$refs.accountMenu.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.accountMenu.removeEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    this.$refs.accountMenu.removeEventListener(
      "touchend",
      this.overlayTouchEnd
    );
  },
  watch: {
    displayMenu(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
      } else {
        this.$refs.accountMenu.style.transform = "";
        this.$refs.accountMenu.style.opacity = "";
      }
    },
  },
};
</script>
