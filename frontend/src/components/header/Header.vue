<template>
  <v-app-bar
    id="header"
    style="border-bottom: solid rgba(0, 0, 0, 0.5) 1px"
    color="rgb(242,217,193)"
    fixed
    elevation="0"
  >
    <v-row
      justify="center"
      style="width: 100%"
      class="contentsFlex mx-auto my-auto"
      no-gutters
    >
      <div
        id="hamburgerMenu"
        :class="{ active: displayMenu }"
        :style="{
          'will-change': displayMenu ? 'transform, filter' : 'auto',
        }"
        @click="toggleMenu"
      >
        <span></span><span>Menu</span><span></span>
      </div>
      <div
        ref="slideBoard"
        id="springBoard"
        :style="
          displayMenu
            ? 'will-change:transform, filter;transform:translateX(0px);'
            : 'will-change:auto;transform:translateX(-250px);'
        "
        v-touch="{
          left: function () {
            swipeBoardObserve();
          },
        }"
      >
        <v-list id="springBoardMenu">
          <v-list-item>
            <SpringBoardMenu
              :labelTxt="logged ? 'アカウント' : 'ログイン'"
              :icon="logged ? 'mdi-account-cog' : 'mdi-login-variant'"
              :onClickSpringBoardMenu="logged ? toAccountManagement : login"
            />
          </v-list-item>
          <v-list-item>
            <SpringBoardMenu
              labelTxt="HOMETEについて"
              icon="mdi-information-variant"
              :onClickSpringBoardMenu="toExplanation"
            />
          </v-list-item>
          <v-list-item>
            <SpringBoardMenu
              labelTxt="Q & A"
              icon="mdi-chat-question-outline"
              :onClickSpringBoardMenu="toQuestionAnswer"
            />
          </v-list-item>
          <v-list-item>
            <SpringBoardMenu
              labelTxt="利用規約"
              icon="mdi-shield-check"
              :onClickSpringBoardMenu="toUserPolicy"
            />
          </v-list-item>
          <v-list-item>
            <SpringBoardMenu
              labelTxt="プライバシー"
              icon="mdi-shield-key-outline"
              :onClickSpringBoardMenu="toPrivacyPolicy"
            />
          </v-list-item>
        </v-list>
      </div>
      <transition name="fade">
        <div
          ref="slideMenuOverlay"
          id="menuOverlay"
          :style="
            displayMenu
              ? 'will-change:opacity, filter;opacity(1);'
              : 'will-change:auto;opacity(0);'
          "
          v-show="displayMenu"
          @click="closeMenu"
          v-touch="{
            left: function () {
              swipeBoardObserve();
            },
          }"
        ></div>
      </transition>
      <v-col id="title" class="md-none text-h5 font-weight-bold" cols="3">
        <img
          src="/assets/homete.webp"
          style="width: 155px; position: relative; top: -3px; left: -15px"
        />
      </v-col>
      <v-col id="contentTitle" cols="6" lg="5">
        {{ contentName }}
      </v-col>
      <v-col id="headerBtn" cols="3">
        <v-btn
          color="rgb(225 255 255)"
          rounded
          @click="toAccountManagement"
          v-if="logged"
        >
          <v-icon>mdi-account-cog</v-icon>
          <div>アカウント</div>
        </v-btn>
        <v-btn color="rgb(225 255 255)" rounded @click="login" v-else>
          <v-icon>mdi-login-variant</v-icon>
          <div>ログイン</div>
        </v-btn>
      </v-col>
    </v-row>
  </v-app-bar>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #title,
  #headerBtn {
    display: flex;
  }
  #hamburgerMenu {
    display: none;
  }
}
@media (max-width: map-get($grid-breakpoints, md)) {
  // md 以下 sm 以上のブレークポイントでのスタイル定義
  #contentTitle {
    max-width: 33%;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #title,
  #headerBtn {
    display: none;
  }
  #hamburgerMenu {
    display: block;
  }
  #contentTitle {
    max-width: 100%;
  }
}
#header {
  z-index: 2;
  transform: translate3d(0px, 0px, 0px);
}
#header div {
  padding: 0 !important;
}
#title {
  margin: 0;
  padding: 0;
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
  justify-content: center;
}
#headerBtn button {
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
  color: rgb(73, 72, 84);
  font-weight: 600;
}

/*ボタン外側※レイアウトによってpositionや形状は適宜変更してください*/
#hamburgerMenu {
  position: absolute; /*ボタン内側の基点となるためrelativeを指定*/
  cursor: pointer;
  width: 45px;
  height: 45px;
  border-radius: 10px;
  border: solid #494854 1px;
  top: 5px;
  left: 5vw;
  transform: scale(0.95);
  background-color: rgb(225 255 255);
}

/*ボタン内側*/
#hamburgerMenu span {
  display: inline-block;
  transition: all 0.4s; /*アニメーションの設定*/
  position: absolute;
  will-change: width, transform, left, top, filter;
}

#hamburgerMenu span:nth-of-type(1),
#hamburgerMenu span:nth-of-type(3) {
  height: 2px;
  background: #494854;
  width: 62%;
  left: 8px;
}

#hamburgerMenu span:nth-of-type(1) {
  top: 10px;
}

#hamburgerMenu span:nth-of-type(2) {
  top: 14px;
  left: 7px;
  font-size: 0.6rem;
  text-transform: uppercase;
  color: #494854;
}

#hamburgerMenu span:nth-of-type(3) {
  top: 30px;
}

/*activeクラスが付与されると線が回転して×になり、Menu表記をしている2つ目の要素が透過して消える*/
#hamburgerMenu.active span:nth-of-type(1) {
  top: 14px;
  left: 14px;
  transform: translateY(6px) rotate(-45deg);
  width: 30%;
}

#hamburgerMenu.active span:nth-of-type(2) {
  opacity: 0;
}

#hamburgerMenu.active span:nth-of-type(3) {
  top: 26px;
  left: 14px;
  transform: translateY(-6px) rotate(45deg);
  width: 30%;
}

#springBoard {
  position: fixed;
  left: 0px;
  height: calc(100vh - 56px);
  width: 250px;
  margin: 0 auto;
  top: 56px;
  z-index: 5;
  transition: all 0.4s !important;
  transform: translateX(-250px);
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}
#springBoardMenu {
  left: 0px;
  height: calc(100vh - 56px);
  width: 250px;
  position: fixed;
  background-color: rgb(255, 248, 225);
  z-index: 2;
}
#springBoardMenu .v-list-item {
  width: 75%;
  margin: 0 auto;
  top: 20px;
  font-size: 13px;
  margin-bottom: 5px;
}

#menuOverlay {
  align-items: flex-end;
  height: calc(100vh - 56px);
  width: 100vw;
  margin: 0;
  padding: 0;
  z-index: auto;
  justify-content: center;
  position: fixed;
  display: flex;
  top: 56px;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(33, 33, 33, 0.26);
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

/*========= レイアウトのためのCSS ===============*/

body {
  background: #f3f3f3;
  padding: 20px;
}

a {
  color: #333;
  text-decoration: none;
}

.lead {
  margin: 20px 0 0 0;
}

.btn-block {
  width: 200px;
  padding: 30px;
}
</style>

<script>
import SpringBoardMenu from "./SpringBoardMenu.vue";

export default {
  name: "Header",
  components: {
    SpringBoardMenu,
  },
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    contentName() {
      return this.$store.getters.contentName;
    },
    displayMenu() {
      return this.$store.getters.displayMenu;
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
    toAccountManagement: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toAccount").then(() => {
        if (this.$route.path != "/account") {
          this.$router.push("/account");
        }
      });
    },
    toExplanation: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toExplanation").then(() => {
        if (this.$route.path != "/about") {
          this.$router.push("/about");
        }
      });
    },
    toQuestionAnswer: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toQuestionAnswer").then(() => {
        if (this.$route.path != "/about") {
          this.$router.push("/about");
        }
      });
    },
    toUserPolicy: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toUserPolicy").then(() => {
        if (this.$route.path != "/about") {
          this.$router.push("/about");
        }
      });
    },
    toPrivacyPolicy: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toPrivacyPolicy").then(() => {
        if (this.$route.path != "/about") {
          this.$router.push("/about");
        }
      });
    },
    toggleMenu() {
      if (this.displayMenu) {
        this.closeMenu();
      } else {
        this.$store.dispatch("visibleMenu");
      }
    },
    closeMenu() {
      this.$store.dispatch("invisibleMenu");
    },
    swipeBoardObserve() {
      this.closeMenu();
    },
  },
};
</script>
