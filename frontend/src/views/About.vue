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
          cols="12"
          sm="9"
          md="6"
          lg="5"
          id="slideAboutX"
          :class="{ slideAboutXActive: isActiveContents }"
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
#artBoard {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
}
#contentsFlex {
  width: 100%;
  flex-wrap: nowrap;
}
.SideMenuFixed {
  top: 0;
  flex-wrap: nowrap;
  margin: 0;
  padding: 0;
  position: fixed;
  justify-content: center;
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
#flexSlide {
  margin-top: 10vh;
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
  transform: translateX(0px);
  z-index: 0;
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
  },
  data() {
    return {
      displayDelete: false,
      checked: [],
      btnDisable: true,
      currentDisplay: null,
      icon: ["🔍", "💡", "📑", "🔒"],
      title: ["使い方", "Q & A", "利用規約", "プライバシー"],
      isActiveContents: false,
    };
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
  watch: {
    aboutState(newState) {
      this.currentDisplay = newState;
    },
  },
  methods: {
    toggleContents(bool) {
      this.isActiveContents = bool;
    },
  },
};
</script>
