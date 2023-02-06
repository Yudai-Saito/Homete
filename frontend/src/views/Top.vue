<template>
  <v-app id="artBoard" style="background-color: rgb(255, 248, 225)">
    <Header ref="header" />
    <Login />
    <DeletePost />
    <ReportPost />
    <transition name="fade">
      <div id="formOverlay" v-show="displayPostForm" @click="closeForm">
        <transition name="slide-y-reverse">
          <div
            ref="postFormCard"
            id="postFormOverlayCard"
            v-show="displayPostForm"
            @click.stop
          >
            <div
              ref="postFormDraggable"
              id="draggableShape"
              @click="closeForm"
              v-touch="{
                down: function () {
                  swipeOverlayObserve();
                },
              }"
            >
              <div id="draggableInner"></div>
            </div>
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
          <div
            ref="pickerCard"
            id="pickerOverlay"
            v-show="displayTwemojiPicker"
            @click.stop
          >
            <div
              ref="pickerDraggable"
              id="draggableShape"
              @click="closePicker"
              v-touch="{
                down: function () {
                  swipeOverlayObserve();
                },
              }"
            >
              <div id="draggableInner"></div>
            </div>
            <TwemojiPicker
              v-click-outside="closePickerOutSide"
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
        <!-- メニューが表示されているときはslideTopXActiveクラスによってスライドする -->
        <v-col
          id="slideTopX"
          ref="scrollPosts"
          :style="fixedScroll"
          :class="{ slideTopXActive: displayMenu }"
          cols="12"
          sm="9"
          md="6"
          lg="5"
          v-touch="{
            right: function () {
              swipePostObserve();
            },
          }"
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
        <div id="postBtnFloat" ref="postBtn">
          <v-btn
            class="d-md-none"
            style="background-color: rgb(225 255 255)"
            :class="{ slideTopXActive: displayMenu }"
            elevation="3"
            fab
            icon
            rounded
            @click="onClickPostBtn"
          >
            <v-icon color="rgb(73,72,84)"> mdi-pen-plus </v-icon>
          </v-btn>
        </div>
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
  #postFormOverlayCard {
    bottom: 30px;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #postFormOverlayCard {
    bottom: 50px;
  }
}
body {
  padding: 0;
}
.v-menu__content {
  font-family: "M PLUS Rounded 1c", sans-serif;
}
#artBoard {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
  font-family: "M PLUS Rounded 1c", sans-serif;
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
  z-index: 0;
  position: relative;
  top: 10vh;
  min-height: 100vh;
}
.slideTopXActive {
  transform: translateX(250px) !important;
  z-index: 0;
  opacity: 0.85;
}

#postBtnFloat {
  position: fixed;
  inset: auto 30px 60px auto;
  transition: all 0.4s !important;
  transform: translateX(0px);
  z-index: 0;
}
#postBtnFloat span i {
  color: whitesmoke;
}
#postFormOverlayCard {
  width: 100vw;
  position: relative;
  z-index: 999;
}
#postFormOverlayCard #formTxtCard {
  margin: 0 !important;
  padding: 0 !important;
  border-bottom-left-radius: 0px !important;
  border-bottom-right-radius: 0px !important;
  border-top-left-radius: 10px !important;
  border-top-right-radius: 10px !important;
}
#draggableShape {
  width: 100%;
  height: 250px;
  position: absolute;
  z-index: 9999;
  top: -235px;
  display: flex;
  justify-content: center;
}
#draggableInner {
  width: 60px;
  height: 5px;
  border-radius: 10px;
  background-color: rgba(230, 230, 230, 0.75);
  margin-top: auto;
  margin-bottom: 20px;
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

import ws from "@/ws-client";

// $grid-breakpoints を JavaScript のオブジェクトとして取得
const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

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
    displayMenu() {
      return this.$store.getters.displayMenu;
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
      if (window.matchMedia(`(max-width: ${gridBreakpoints.md}px)`).matches) {
        return "slide-y-reverse";
      }
      return "fade";
    },
    fixedScroll() {
      if (window.matchMedia(`(max-width: ${gridBreakpoints.md}px)`).matches) {
        //絵文字ピッカーか投稿フォームが表示されている時にスタイルを付与
        if (this.displayTwemojiPicker || this.displayPostForm)
          return {
            "pointer-events": "none",
          };
      }
      return {};
    },
  },
  data() {
    return {
      updatePost: null,
      currentScrollPosition: 0,
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
      if (this.logged) {
        this.$store.dispatch("visiblePostForm");
      } else {
        this.plzLogin();
      }
    },
    plzLogin: function () {
      this.$store.dispatch("visiblePlzLoginOverlay");
    },
    closeForm() {
      this.$store.dispatch("invisiblePostForm");
    },
    addPickerReaction(updatePost) {
      this.updatePost = updatePost;
    },
    closePicker() {
      if (window.matchMedia(`(min-width: ${gridBreakpoints.md}px)`).matches) {
        if (this.clickOutSide) {
          this.$store.commit("invisibleTwemojiPicker");
        } else {
          this.$store.commit("clickingOutSide", true);
        }
      } else {
        this.$store.commit("invisibleTwemojiPicker");
      }
    },
    closePickerOutSide() {
      if (window.matchMedia(`(min-width: ${gridBreakpoints.md}px)`).matches) {
        this.closePicker();
      }
    },
    openMenu() {
      this.$store.dispatch("visibleMenu");
      this.$refs.scrollPosts.style.transform = `translateX(250px)`;
      this.$refs.postBtn.style.transform = `translateX(250px)`;
      this.$refs.header.$refs.slideBoard.style.transform = `translateX(0px)`;
      this.$refs.scrollPosts.style.opacity = `0.85`;
      this.$refs.postBtn.style.opacity = `0.85`;
      this.$refs.header.$refs.slideBoard.style.opacity = `1`;
    },
    closeMenu() {
      this.$store.dispatch("invisibleMenu");
      this.$refs.scrollPosts.style.transform = `translateX(0px)`;
      this.$refs.postBtn.style.transform = `translateX(0px)`;
      this.$refs.header.$refs.slideBoard.style.transform = `translateX(-250px)`;
      this.$refs.scrollPosts.style.opacity = `1`;
      this.$refs.postBtn.style.opacity = `1`;
      this.$refs.header.$refs.slideBoard.style.opacity = `0`;
    },
    swipePostObserve() {
      this.openMenu();
    },
    swipeOverlayObserve() {
      this.closeForm();
      this.closePicker();
    },
  },
  mounted() {
    //投稿管理系ステートを全てリセットかける
    this.$store.commit("deleteUserUpdatePosts");
    this.$store.commit("deleteUpdatePosts");

    //WS接続
    ws.connect(this);
  },
  watch: {
    //それぞれ開く際にタッチアクションを無効化
    displayTwemojiPicker(newBool) {
      if (newBool) {
        document.body.style.touchAction = "none";
      } else {
        document.body.style.touchAction = "";
      }
    },
    displayPostForm(newBool) {
      if (newBool) {
        document.body.style.touchAction = "none";
      } else {
        document.body.style.touchAction = "";
      }
    },
    displayMenu(newBool) {
      if (newBool) {
        document.body.style.touchAction = "none";
        this.openMenu();
      } else {
        document.body.style.touchAction = "";
        this.closeMenu();
      }
    },
  },
  beforeDestroy() {
    ws.disconnect();
  },
};
</script>
