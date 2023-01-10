<template>
  <v-app id="artBoard" class="blue-grey lighten-5">
    <Header @isActive="toggleContents" />
    <Login />

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
          ref="aboutMenu"
          cols="12"
          sm="9"
          md="6"
          lg="5"
          id="slideAboutX"
          :class="{ slideAboutXActive: displayMenu }"
        >
          <v-slide-group
            id="flexSlide"
            v-model="currentDisplay"
            show-arrows
            mandatory
          >
            <v-slide-item v-for="n in 4" :key="n" v-slot="{ active, toggle }">
              <div style="margin-bottom: 17px">
                <v-card
                  :class="active ? 'activeGroupCard' : 'groupCard'"
                  id="aboutGroups"
                  height="70"
                  width="70"
                  @click="toggle"
                >
                  <div v-twemoji style="width: 35px; margin: auto">
                    {{ icon[n - 1] }}
                  </div>
                  <v-scale-transition>
                    <v-icon
                      v-if="active"
                      style="color: #2196f3"
                      size="50"
                    ></v-icon>
                  </v-scale-transition>
                </v-card>
                <div
                  :style="active ? 'color:#2196f3' : 'color:#494854'"
                  style="font-size: 14px; text-align: center"
                >
                  {{ title[n - 1] }}
                </div>
              </div>
            </v-slide-item>
          </v-slide-group>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <Explanation v-if="currentDisplay == 0" />
          </v-fade-transition>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <QuestionAnswer v-if="currentDisplay == 1" />
          </v-fade-transition>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <UserPolicy v-if="currentDisplay == 2" />
          </v-fade-transition>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <PrivacyPolicy v-if="currentDisplay == 3" />
          </v-fade-transition>
        </v-col>
        <v-col cols="3" class="d-none d-md-block"> </v-col>
      </v-row>
    </div>
    <Footer />
  </v-app>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #flexSlide .v-slide-group__prev,
  #flexSlide .v-slide-group__next {
    display: none;
  }
  #flexSlide .v-slide-group__wrapper .v-slide-group__content div div {
    transform: scale(0.75);
    margin: 0;
  }
}
.aboutContainer {
  width: 95%;
  height: 30%;
  text-align: center;
  background-color: #ffffff;
  border-radius: 30px;
  margin: 0 auto;
  margin-bottom: 8vh;
}
.aboutTitleTxt {
  margin-top: 10px;
  color: #494854;
}
.aboutText {
  font-size: 14px;
  margin: 10px 0;
  color: #494854;
}
.aboutGroupTitle {
  margin: 0 15px;
  display: flex;
  justify-content: center;
}
#flexSlide .v-slide-group__wrapper .v-slide-group__content {
  justify-content: center;
}
#aboutGroups {
  display: flex;
  justify-content: center;
  border-radius: 50% !important;
  margin: 20px;
  margin-bottom: 3px;
  padding: 0;
  overflow: hidden;
}
.activeGroupCard {
  border: solid 2px #2196f3 !important;
}
.groupCard {
  border: solid 2px #bdbdbd;
}
.v-card--link:before {
  height: 75px;
  width: 75px;
  left: -4px;
  top: -4px;
}

#slideAboutX {
  transition: all 0.4s !important;
  z-index: 0;
  position: relative;
  top: 10vh;
  min-height: 100vh;
}
.slideAboutXActive {
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
import Explanation from "@/components/abouts/Explanation.vue";
import PrivacyPolicy from "@/components/abouts/PrivacyPolicy.vue";
import QuestionAnswer from "@/components/abouts/QuestionAnswer.vue";
import UserPolicy from "@/components/abouts/UserPolicy.vue";
import twemoji from "twemoji";

// $grid-breakpoints を JavaScript のオブジェクトとして取得
const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

export default {
  name: "About",
  components: {
    Explanation,
    PrivacyPolicy,
    QuestionAnswer,
    UserPolicy,
    Login,
    LeftMenu,
    Footer,
    Header,
  },
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    overlayState() {
      return this.$store.getters.overlayState;
    },
    aboutState() {
      return this.$store.getters.aboutState;
    },
    displayMenu() {
      return this.$store.getters.displayMenu;
    },
  },
  data() {
    return {
      displayDelete: false,
      checked: [],
      btnDisable: true,
      currentDisplay: this.aboutState,
      icon: ["🔍", "💡", "📑", "🔒"],
      title: ["使い方", "Q & A", "利用規約", "プライバシー"],
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
          this.$refs.aboutMenu.style.transform = `translateX(${
            this.dragCurrentX - this.dragStartX
          }px)`;
          this.$refs.aboutMenu.style.opacity = `${
            this.$refs.aboutMenu.style.opacity + 1 - 0.005
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
          this.$refs.aboutMenu.style.transform = "";
          this.$refs.aboutMenu.style.opacity = "";
          this.dragStartX = 0;
          this.dragCurrentX = 0;
        }
      }
    },
  },
  mounted() {
    //画面中央
    // touchstartイベントを監視する
    this.$refs.aboutMenu.addEventListener("touchstart", this.postsTouchStart);
    // touchmoveイベントを監視する
    this.$refs.aboutMenu.addEventListener("touchmove", this.postsTouchMove);
    // touchendイベントを監視する
    this.$refs.aboutMenu.addEventListener("touchend", this.postsTouchEnd);

    this.currentDisplay = this.aboutState;
  },
  beforeDestroy() {
    // イベントの監視を解除する
    this.$refs.aboutMenu.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.aboutMenu.removeEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    this.$refs.aboutMenu.removeEventListener("touchend", this.overlayTouchEnd);
  },
  watch: {
    aboutState(newState) {
      this.currentDisplay = newState;
    },
    displayMenu(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
      } else {
        this.$refs.aboutMenu.style.transform = "";
        this.$refs.aboutMenu.style.opacity = "";
      }
    },
  },
};
</script>
