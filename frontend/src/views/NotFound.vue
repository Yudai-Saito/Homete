<template>
  <div id="artBoard" class="blue-grey lighten-5">
    <Header />
    <Login />
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
    <Footer />
  </div>
</template>

<style>
#notFoundTxt {
  font-size: 50px;
  text-align: center;
  z-index: 0;
  margin-top: 100px;
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
  background-color: rgba(207, 216, 220, 0.5);
}
</style>


<script>
import Header from "@/components/header/Header.vue";
import Footer from "@/components/footer/Footer.vue";
import Login from "@/components/overlays/Login.vue";

export default {
  name: "NotFound",
  components: {
    Login,
    Footer,
    Header,
  },
  computed: {
    overlayState() {
      return this.$store.getters.overlayState;
    },
  },
  methods: {
    toTopPage: function () {
      this.$router.push("/");
    },
  },
};
</script>
