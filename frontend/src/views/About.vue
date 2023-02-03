<template>
  <v-app id="artBoard" style="background-color: rgb(255, 248, 225)">
    <Header @isActive="toggleContents" ref="header" />
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
          v-touch="{
            right: function () {
              swipeAboutMenuObserve();
            },
          }"
        >
          <v-slide-group
            id="flexSlide"
            v-model="currentDisplay"
            show-arrows
            :mandatory="false"
          >
            <v-slide-item v-for="n in 5" :key="n" v-slot="{ active, toggle }">
              <div style="margin-bottom: 17px">
                <v-card
                  :class="active ? 'activeGroupCard' : 'groupCard'"
                  id="aboutGroups"
                  height="60"
                  width="60"
                  @click="active ? void 0 : toggle()"
                  :style="{ pointerEvents: active ? 'none' : 'auto' }"
                >
                  <div v-twemoji id="groupImg">
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
                  style="font-size: 13px; text-align: center; margin-top: 8px"
                >
                  {{ title[n - 1] }}
                </div>
              </div>
            </v-slide-item>
          </v-slide-group>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <Explanation v-if="currentDisplay == 1" />
          </v-fade-transition>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <QuestionAnswer v-if="currentDisplay == 2" />
          </v-fade-transition>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <UserPolicy v-if="currentDisplay == 3" />
          </v-fade-transition>

          <v-fade-transition :hide-on-leave="true" mode="in-out">
            <PrivacyPolicy v-if="currentDisplay == 4" />
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
  #groupImg {
    width: 30px;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #flexSlide .v-slide-group__prev,
  #flexSlide .v-slide-group__next {
    display: none;
  }
  #flexSlide .v-slide-group__wrapper .v-slide-group__content div div {
    transform: scale(0.75);
    margin: auto;
  }
  #groupImg {
    width: 40px;
  }
}
.aboutContainer {
  padding: 0% 5%;
  width: 95%;
  height: fit-content;
  background-color: #ffffff;
  border-radius: 30px;
  margin: 0 auto;
  margin-bottom: 8vh;
  border: solid 1px rgba(135, 143, 255, 0.5);
}
.aboutTitle {
  width: 20px;
  margin-right: 5px;
  margin-top: 12px;
}
.divider {
  margin: 10px;
}
.aboutTitleTxt {
  margin-top: 8px;
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
  margin: 20px 10px;
  margin-bottom: 3px;
  padding: 0;
  overflow: hidden;
}
#groupImg {
  margin: auto;
}
#groupImg img {
  margin-top: 3px;
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
  margin-top: 10vh;
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
      icon: ["🔍", "🔰", "💡", "📑", "🔒"],
      title: ["HOMETEとは", "使い方", "Q & A", "利用規約", "プライバシー"],
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
    openMenu() {
      this.$store.dispatch("visibleMenu");
      this.$refs.aboutMenu.style.transform = `translateX(250px)`;
      this.$refs.header.$refs.slideBoard.style.transform = `translateX(0px)`;
      this.$refs.aboutMenu.style.opacity = `0.85`;
      this.$refs.header.$refs.slideBoard.style.opacity = `1`;
    },
    closeMenu() {
      this.$store.dispatch("invisibleMenu");
      this.$refs.aboutMenu.style.transform = `translateX(0px)`;
      this.$refs.header.$refs.slideBoard.style.transform = `translateX(-250px)`;
      this.$refs.aboutMenu.style.opacity = `1`;
      this.$refs.header.$refs.slideBoard.style.opacity = `0`;
    },
    swipeAboutMenuObserve() {
      this.openMenu();
    },
  },
  mounted() {
    this.currentDisplay = this.aboutState;
  },
  watch: {
    aboutState(newState) {
      this.currentDisplay = newState;
    },
    displayMenu(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
        this.openMenu();
      } else {
        document.body.style.touchAction = "";
        this.$refs.aboutMenu.style.transform = "";
        this.$refs.aboutMenu.style.opacity = "";
        this.closeMenu();
      }
    },
    currentDisplay(newState) {
      if (newState === 0) {
        if (window.innerWidth < gridBreakpoints.sm) {
          this.$router.push({ name: "SmLandingPage" });
        } else {
          this.$router.push({ name: "LandingPage" });
        }
      }
      this.$store.dispatch("setAboutState", newState);
    },
  },
};
</script>
