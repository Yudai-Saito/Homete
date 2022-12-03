<template>
  <v-app class="artBoard blue-grey lighten-5">
    <Header />
    <v-overlay
      :value="overlayState == 'login'"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <CommonOverlay
        usage="login"
        titleTxt="HOMETE"
        firstMsg="ここに適当なサービスの説明とようこそ的な文章"
        btnTxt="Googleでログイン"
        descriptionTxt="ここに注意事項的な文章"
        :onClick="logIn"
      />
    </v-overlay>

    <div>
      <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
        <v-col cols="3">
          <LeftMenu class="SideMenuSticky" />
        </v-col>

        <v-col class="mainContents" cols="6">
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
                  class="aboutGroups"
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
.closeCardBtn {
  justify-content: center;
  position: absolute;
  left: 400px;
}
.deleteaboutGroupTitle {
  color: #ffffff;
  margin-right: 8px;
  margin-left: 8px;
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
.aboutContainer {
  width: 100%;
  height: 30%;
  text-align: center;
  background-color: #ffffff;
  border-radius: 30px;
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
.aboutGroups {
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
</style>


<script>
import Explanation from "@/components/abouts/Explanation.vue";
import PrivacyPolicy from "@/components/abouts/PrivacyPolicy.vue";
import QuestionAnswer from "@/components/abouts/QuestionAnswer.vue";
import UserPolicy from "@/components/abouts/UserPolicy.vue";
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import CommonOverlay from "@/components/util/CommonOverlay.vue";
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";
import twemoji from "twemoji";

export default {
  name: "AccountManagement",
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
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    overlayState() {
      return this.$store.getters.overlayState;
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
    };
  },
  components: {
    Explanation,
    PrivacyPolicy,
    QuestionAnswer,
    UserPolicy,
    CommonOverlay,
    LeftMenu,
    Footer,
    Header,
  },
  methods: {
    displayDeleteCard() {
      this.displayDelete = true;
    },
    closeDeleteCard() {
      this.displayDelete = false;
      this.checked = [];
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
