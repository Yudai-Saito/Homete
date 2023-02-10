<template>
  <div id="artBoard" style="background-color: rgb(255, 248, 225)">
    <Header ref="header" />
    <Login />
    <v-col
      ref="notFound"
      cols="12"
      id="slideNotFoundX"
      :class="{ slideAboutXActive: displayMenu }"
      v-touch="{
        right: function () {
          swipeNotFoundObserve();
        },
      }"
    >
      <div id="notFoundTxt">
        <h1>404</h1>
      </div>
      <div id="nfContainer">
        ページが見つかりませんでした
        <img
          src="/assets/HOMETE_LP6.webp"
          style="display: block; margin: 0 auto; top: -35px; position: relative"
        />
        <div style="position: relative; top: -60px">
          <v-btn
            id="nfReactBtn"
            class="grey--text text--darken-3"
            @click="toHome"
            elevation="0"
            outlined
          >
            <v-icon>{{ mdiArrowUpBoldBoxOutline }}</v-icon>
            <h4>Homeへ戻る</h4>
          </v-btn>
        </div>
      </div>
    </v-col>
    <Footer />
  </div>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, md)) {
  // md 以上のブレークポイントでのスタイル定義
  #nfContainer img {
    width: 30%;
  }
}
@media (max-width: map-get($grid-breakpoints, md)) {
  // sm 以上 md 以下のブレークポイントでのスタイル定義
  #nfContainer img {
    width: 50%;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #nfContainer img {
    width: 80%;
  }
}
#notFoundTxt {
  font-size: 50px;
  text-align: center;
  z-index: 0;
  margin-top: auto;
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
  margin-bottom: auto;
}
#nfReactBtn {
  background-color: rgb(225 255 255);
}
#slideNotFoundX {
  transition: all 0.4s !important;
  z-index: 0;
  position: relative;
  min-height: 100vh;
  transform: scale(0.95);
  display: flex;
  flex-flow: column;
}
</style>


<script>
import Header from "@/components/header/Header.vue";
import Footer from "@/components/footer/Footer.vue";
import Login from "@/components/overlays/Login.vue";

import { mdiArrowUpBoldBoxOutline } from "@mdi/js";

export default {
  name: "NotFound",
  components: {
    Login,
    Footer,
    Header,
  },
  data() {
    return {
      mdiArrowUpBoldBoxOutline,
    };
  },
  computed: {
    displayMenu() {
      return this.$store.getters.displayMenu;
    },
  },
  methods: {
    toHome: function () {
      this.$store.dispatch("toTimeLine").then(() => {
        this.$router.push("/home");
      });
    },
    openMenu() {
      this.$store.dispatch("visibleMenu");
    },
    closeMenu() {
      this.$store.dispatch("invisibleMenu");
    },
    swipeNotFoundObserve() {
      this.openMenu();
    },
  },
};
</script>
