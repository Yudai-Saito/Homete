<template>
  <v-app id="artBoard" class="blue-grey lighten-5">
    <Header @isActive="toggleContents" />
    <Login />
    <DeletePost />
    <ReportPost />
    <transition name="fade">
      <div id="formOverlay" v-show="displayPostForm" @click="closeForm">
        <transition name="slide-y-reverse">
          <div v-show="displayPostForm" id="smOverlayCard" @click.stop>
            <PostForm />
          </div>
        </transition>
      </div>
    </transition>
    <transition name="fade">
      <div
        id="formOverlay"
        style="z-index: 2"
        v-show="displayTwemojiPicker"
        @click="closePicker"
      >
        <transition :name="transitionName">
          <div v-show="displayTwemojiPicker" id="pickerOverlay" @click.stop>
            <TwemojiPicker
              v-click-outside="closePicker"
              @addReaction="addPickerReaction"
            />
          </div>
        </transition>
      </div>
    </transition>
    <div>
      <TopAlert />
      <BottomAlert />
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
          id="slideTopX"
          :class="{ slideTopXActive: isActiveContents }"
          cols="12"
          sm="9"
          md="6"
          lg="5"
        >
          <PostContents
            v-if="contentsKey == 'timeline'"
            :key="contentsKey"
            :updatePost="updatePost"
          />
          <PostContents
            v-if="contentsKey == 'history'"
            :channel="contentsKey"
            :key="contentsKey"
            :updatePost="updatePost"
          />
        </v-col>
        <v-btn
          id="postBtnFloat"
          class="d-md-none"
          :class="{ slideTopXActive: isActiveContents }"
          elevation="3"
          fab
          icon
          rounded
          @click="onClickPostBtn"
        >
          <v-icon> mdi-pen-plus </v-icon>
        </v-btn>
        <v-col cols="3" class="d-none d-md-block">
          <RightMenu class="SideMenuFixed" />
        </v-col>
      </v-row>
    </div>
    <Footer />
  </v-app>
</template>
<style lang="scss">
@media (max-width: map-get($grid-breakpoints, md)) {
  #pickerOverlay {
    bottom: 30px;
    width: 100vw;
    position: relative;
    z-index: 999;
  }
  #formOverlay {
    align-items: flex-end;
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
    z-index: 1;
    justify-content: center;
    position: fixed;
    display: flex;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(33, 33, 33, 0.46);
    overflow: hidden;
  }
}
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #smOverlayCard {
    bottom: 30px;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #smOverlayCard {
    bottom: 50px;
  }
}
body {
  padding: 0;
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

#slideTopX {
  transition: all 0.4s !important;
  transform: translateX(0px);
  z-index: 0;
}
.slideTopXActive {
  transform: translateX(250px) !important;
  z-index: 0;
  opacity: 0.85;
}

#postBtnFloat {
  position: fixed;
  background-color: #1da1f2;
  inset: auto 30px 60px auto;
  transition: all 0.4s !important;
  transform: translateX(0px);
  z-index: 0;
}
#postBtnFloat span i {
  color: whitesmoke;
}
#smOverlayCard {
  width: 100vw;
  position: relative;
  z-index: 999;
}
#smOverlayCard #formTxtCard {
  margin: 0 !important;
  padding: 0 !important;
  border-bottom-left-radius: 0px !important;
  border-bottom-right-radius: 0px !important;
  border-top-left-radius: 10px !important;
  border-top-right-radius: 10px !important;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.slide-y-reverse-enter-active {
  transition: all 0.2s;
}
.slide-y-reverse-leave-active {
  transition: all 0.4s;
}
.slide-y-reverse-enter,
.slide-y-reverse-leave-to {
  transform: translateY(100%);
}
.slide-y-reverse-leave,
.slide-y-reverse-enter-to {
  transform: translateY(0%);
}
</style>


<script>
import Header from "@/components/header/Header.vue";
import Footer from "@/components/footer/Footer.vue";
import TopAlert from "@/components/alerts/TopAlert.vue/";
import BottomAlert from "@/components/alerts/BottomAlert.vue";
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import PostContents from "@/components/mainContents/PostContents.vue";
import RightMenu from "@/components/rightMenu/RightMenu.vue";
import Login from "@/components/overlays/Login.vue";
import DeletePost from "@/components/overlays/DeletePost.vue";
import ReportPost from "@/components/overlays/ReportPost.vue";
import PostForm from "@/components/util/PostForm.vue";
import TwemojiPicker from "@/components/util/TwemojiPicker.vue";

import ClickOutside from "vue-click-outside";

export default {
  name: "Top",
  components: {
    LeftMenu,
    PostContents,
    RightMenu,
    Login,
    DeletePost,
    ReportPost,
    TopAlert,
    BottomAlert,
    Footer,
    Header,
    PostForm,
    TwemojiPicker,
  },
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    overlayState() {
      return this.$store.getters.overlayState;
    },
    contentsKey() {
      return this.$store.getters.contentsKey;
    },
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    clickOutSide() {
      return this.$store.getters.clickOutSide;
    },
    displayTwemojiPicker() {
      return this.$store.getters.displayTwemojiPicker;
    },
    transitionName() {
      // $grid-breakpoints を JavaScript のオブジェクトとして取得します
      const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };
      if (window.matchMedia(`(max-width: ${gridBreakpoints.md}px)`).matches) {
        return "slide-y-reverse";
      }
      return "fade";
    },
  },
  data() {
    return {
      isActiveContents: false,
      updatePost: null,
    };
  },
  directives: {
    ClickOutside,
  },
  methods: {
    logIn: function () {
      this.$router.push("/login");
    },
    onClickPostBtn() {
      this.$store.dispatch("visiblePostForm");
    },
    closeForm() {
      this.$store.dispatch("invisiblePostForm");
    },
    toggleContents(bool) {
      this.isActiveContents = bool;
    },
    addPickerReaction(updatePost) {
      this.updatePost = updatePost;
    },
    closePicker() {
      if (this.clickOutSide) {
        this.$store.commit("invisibleTwemojiPicker");
      } else {
        this.$store.commit("clickingOutSide", true);
      }
    },
  },
};
</script>
