<template>
  <div id="artBoard" style="background-color: rgb(255, 248, 225)">
    <Header />
    <Login />
    <v-col
      ref="notFound"
      cols="12"
      id="slideNotFoundX"
      :class="{ slideAboutXActive: displayMenu }"
    >
      <div id="notFoundTxt">
        <h1>404</h1>
      </div>
      <div id="nfContainer">
        ページが見つかりませんでした
        <img
          src="/assets/HOMETE_LP6.png"
          style="
            width: 30%;
            display: block;
            margin: 0 auto;
            top: -35px;
            position: relative;
          "
        />
        <div style="position: relative; top: -60px">
          <v-btn
            id="nfReactBtn"
            class="grey--text text--darken-3"
            @click="toTopPage"
            elevation="0"
            outlined
          >
            <v-icon>mdi-arrow-up-bold-box-outline</v-icon>
            <h4>トップへ戻る</h4>
          </v-btn>
        </div>
      </div>
    </v-col>
    <Footer />
  </div>
</template>

<style>
#notFoundTxt {
  font-size: 50px;
  text-align: center;
  z-index: 0;
  margin-top: 30px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
}
#nfContainer {
  display: flex;
  flex-flow: column;
  justify-content: center;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
}
#nfReactBtn {
  background-color: rgb(225 255 255);
}
#slideNotFoundX {
  transition: all 0.4s !important;
  z-index: 0;
  position: relative;
  top: 6vh;
  min-height: 100vh;
}
.slideNotFoundXActive {
  transform: translateX(250px) !important;
  z-index: 0;
  opacity: 0.85;
}
</style>


<script>
import Header from "@/components/header/Header.vue";
import Footer from "@/components/footer/Footer.vue";
import Login from "@/components/overlays/Login.vue";

// $grid-breakpoints を JavaScript のオブジェクトとして取得
const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

export default {
  name: "NotFound",
  components: {
    Login,
    Footer,
    Header,
  },
  computed: {
    displayMenu() {
      return this.$store.getters.displayMenu;
    },
  },
  data() {
    return {
      dragStartX: 0, // タッチ操作開始時のX座標
      dragCurrentX: 0, // 現在のX座標
    };
  },

  methods: {
    toTopPage: function () {
      this.$store.dispatch("toTimeLine");
      this.$router.push("/top");
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
          this.$refs.notFound.style.transform = `translateX(${
            this.dragCurrentX - this.dragStartX
          }px)`;
          this.$refs.notFound.style.opacity = `${
            this.$refs.notFound.style.opacity + 1 - 0.005
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
          this.$refs.notFound.style.transform = "";
          this.$refs.notFound.style.opacity = "";
          this.dragStartX = 0;
          this.dragCurrentX = 0;
        }
      }
    },
  },
  mounted() {
    //画面中央
    // touchstartイベントを監視する
    this.$refs.notFound.addEventListener("touchstart", this.postsTouchStart);
    // touchmoveイベントを監視する
    this.$refs.notFound.addEventListener("touchmove", this.postsTouchMove);
    // touchendイベントを監視する
    this.$refs.notFound.addEventListener("touchend", this.postsTouchEnd);
  },
  beforeDestroy() {
    // イベントの監視を解除する
    this.$refs.notFound.removeEventListener(
      "touchstart",
      this.overlayTouchStart
    );
    this.$refs.notFound.removeEventListener("touchmove", this.overlayTouchMove);
    this.$refs.notFound.removeEventListener("touchend", this.overlayTouchEnd);
  },
};
</script>
