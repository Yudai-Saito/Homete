<template>
  <v-app id="artBoard" class="blue-grey lighten-5">
    <Header />
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
            <div ref="postFormDraggable" id="draggableShape" @click="closeForm">
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
            <div ref="pickerDraggable" id="draggableShape">
              <div id="draggableInner"></div>
            </div>
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
          ref="scrollPosts"
          :style="fixedScroll"
          :class="{ slideTopXActive: displayMenu }"
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
        <div id="postBtnFloat" ref="postBtn">
          <v-btn
            class="d-md-none"
            style="background-color: #1da1f2"
            :class="{ slideTopXActive: displayMenu }"
            elevation="3"
            fab
            icon
            rounded
            @click="onClickPostBtn"
          >
            <v-icon> mdi-pen-plus </v-icon>
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
  height: 50px;
  position: absolute;
  z-index: 9999;
  top: -35px;
  display: flex;
  justify-content: center;
}
#draggableInner {
  width: 60px;
  height: 5px;
  border-radius: 10px;
  background-color: rgba(230, 230, 230, 0.75);
  margin-top: auto;
  margin-bottom: auto;
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
        if (
          this.displayTwemojiPicker ||
          this.displayPostForm ||
          this.displayMenu
        )
          return {
            height: "100vh",
            bottom: `${this.currentScrollPosition}px`,
            position: "relative",
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
      dragStartY: 0, // タッチ操作開始時のY座標
      dragCurrentY: 0, // 現在のY座標
      dragStartX: 0, // タッチ操作開始時のX座標
      dragCurrentX: 0, // 現在のX座標
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
    overlayTouchStart(event) {
      this.dragStartY = event.touches[0].clientY;
    },
    // touchmoveイベントのハンドラ
    overlayTouchMove(event) {
      this.dragCurrentY = event.touches[0].clientY;
      // スライドさせたい要素のスタイルを変更する
      if (this.dragCurrentY - this.dragStartY >= 0) {
        this.$refs.postFormCard.style.transform = `translateY(${
          this.dragCurrentY - this.dragStartY
        }px)`;
        this.$refs.postFormCard.style.opacity = `${
          this.$refs.postFormCard.style.opacity + 1 - 0.005
        }`;

        this.$refs.pickerCard.style.transform = `translateY(${
          this.dragCurrentY - this.dragStartY
        }px)`;
        this.$refs.pickerCard.style.opacity = `${
          this.$refs.pickerCard.style.opacity + 1 - 0.005
        }`;
      }
    },
    overlayTouchEnd() {
      if (this.dragCurrentY - this.dragStartY >= 50) {
        this.closeForm();
        this.$refs.postFormCard.style.transform = "";
        this.$refs.postFormCard.style.opacity = "";
        this.closePicker();
        this.$refs.pickerCard.style.transform = "";
        this.$refs.pickerCard.style.opacity = "";
        this.dragStartY = 0;
        this.dragCurrentY = 0;
      } else {
        this.$refs.postFormCard.style.transform = "";
        this.$refs.postFormCard.style.opacity = "";

        this.$refs.pickerCard.style.transform = "";
        this.$refs.pickerCard.style.opacity = "";

        this.dragStartY = 0;
        this.dragCurrentY = 0;
      }
    },

    postsTouchStart(event) {
      this.dragStartX = event.touches[0].clientX;
    },
    // touchmoveイベントのハンドラ
    postsTouchMove(event) {
      this.dragCurrentX = event.touches[0].clientX;
      // スライドさせたい要素のスタイルを変更する
      if (this.dragCurrentX - this.dragStartX >= 0) {
        this.$refs.scrollPosts.style.transform = `translateX(${
          this.dragCurrentX - this.dragStartX
        }px)`;
        this.$refs.postBtn.style.transform = `translateX(${
          this.dragCurrentX - this.dragStartX
        }px)`;
        this.$refs.scrollPosts.style.opacity = `${
          this.$refs.scrollPosts.style.opacity + 1 - 0.005
        }`;
        this.$refs.postBtn.style.opacity = `${
          this.$refs.postFormCard.style.opacity + 1 - 0.005
        }`;
      }
    },
    postsTouchEnd() {
      if (this.dragCurrentX - this.dragStartX >= 50) {
        this.$store.dispatch("visibleMenu");
        this.dragStartX = 0;
        this.dragCurrentX = 0;
      } else {
        this.$refs.scrollPosts.style.transform = "";
        this.$refs.scrollPosts.style.opacity = "";
        this.$refs.postBtn.style.transform = "";
        this.$refs.postBtn.style.opacity = "";
        this.dragStartX = 0;
        this.dragCurrentX = 0;
      }
    },
  },
  mounted() {
    //投稿フォーム
    // touchstartイベントを監視する
    this.$refs.postFormDraggable.addEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    // touchmoveイベントを監視する
    this.$refs.postFormDraggable.addEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    // touchendイベントを監視する
    this.$refs.postFormDraggable.addEventListener(
      "touchend",
      this.overlayTouchEnd
    );

    //絵文字ピッカー
    // touchstartイベントを監視する
    this.$refs.pickerDraggable.addEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    // touchmoveイベントを監視する
    this.$refs.pickerDraggable.addEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    // touchendイベントを監視する
    this.$refs.pickerDraggable.addEventListener(
      "touchend",
      this.overlayTouchEnd
    );

    //投稿一覧全体
    // touchstartイベントを監視する
    this.$refs.scrollPosts.addEventListener("touchstart", this.postsTouchStart);
    // touchmoveイベントを監視する
    this.$refs.scrollPosts.addEventListener("touchmove", this.postsTouchMove);
    // touchendイベントを監視する
    this.$refs.scrollPosts.addEventListener("touchend", this.postsTouchEnd);

    //投稿ボタン
    // touchstartイベントを監視する
    this.$refs.postBtn.addEventListener("touchstart", this.postsTouchStart);
    // touchmoveイベントを監視する
    this.$refs.postBtn.addEventListener("touchmove", this.postsTouchMove);
    // touchendイベントを監視する
    this.$refs.postBtn.addEventListener("touchend", this.postsTouchEnd);
  },
  beforeDestroy() {
    // イベントの監視を解除する
    this.$refs.postFormDraggable.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.postFormDraggable.removeEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    this.$refs.postFormDraggable.removeEventListener(
      "touchend",
      this.overlayTouchEnd
    );

    this.$refs.pickerDraggable.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.pickerDraggable.removeEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    this.$refs.pickerDraggable.removeEventListener(
      "touchend",
      this.overlayTouchEnd
    );

    this.$refs.scrollPosts.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.scrollPosts.removeEventListener(
      "touchmove",
      this.overlayTouchMove
    );
    this.$refs.scrollPosts.removeEventListener(
      "touchend",
      this.overlayTouchEnd
    );

    this.$refs.postBtn.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.postBtn.removeEventListener("touchmove", this.overlayTouchMove);
    this.$refs.postBtn.removeEventListener("touchend", this.overlayTouchEnd);
  },
  updated() {
    if (window.matchMedia(`(max-width: ${gridBreakpoints.md}px)`).matches) {
      if (
        !this.displayTwemojiPicker &&
        !this.displayPostForm &&
        !this.displayMenu
      ) {
        window.scrollTo(0, this.currentScrollPosition);
        this.currentScrollPosition = 0;
        document.body.style.touchAction = "";
      }
    }
  },
  watch: {
    displayTwemojiPicker(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
      }
    },
    displayPostForm(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
      }
    },
    displayMenu(newBool) {
      if (newBool) {
        this.currentScrollPosition = window.scrollY;
        document.body.style.touchAction = "none";
      } else {
        this.$refs.scrollPosts.style.transform = "";
        this.$refs.scrollPosts.style.opacity = "";
        this.$refs.postBtn.style.transform = "";
        this.$refs.postBtn.style.opacity = "";
      }
    },
  },
};
</script>
