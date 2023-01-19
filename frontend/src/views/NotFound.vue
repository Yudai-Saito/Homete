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
      <div id="notFoundCard">
        <v-card id="hometeCard" class="rounded-xl" :elevation="3">
          <h3 class="ml-4 mt-2">あどみん</h3>
          <v-card-text id="cardText" class="black--text font-weight-light">
            このページはすでに削除されているか、URLが間違っているよ
          </v-card-text>
          <v-card-actions>
            <div id="btnDiv">
              <v-btn
                id="reactBtn"
                class="grey--text text--darken-3"
                @click="toTopPage"
                elevation="0"
                outlined
              >
                <v-icon>mdi-arrow-up-bold-box-outline</v-icon>
                <h4>Topへ戻る</h4>
              </v-btn>
            </div>
          </v-card-actions>
        </v-card>
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
#notFoundCard {
  margin-bottom: auto;
  padding: 10px;
}
#hometeCard {
  margin: 0;
  width: 100%;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  z-index: 0;
}
#cardText {
  font-size: 18px;
  line-height: 26px;
}
#btnDiv {
  margin: 0;
  padding: 0;
  margin-right: 6px;
}
#reactBtn {
  background-color: rgb(225, 227, 255);
}
#slideNotFoundX {
  transition: all 0.4s !important;
  z-index: 0;
  position: relative;
  top: 10vh;
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
      this.$router.push("/");
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
