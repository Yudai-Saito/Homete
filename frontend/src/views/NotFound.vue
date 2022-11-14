<template>
  <div class="artBoard">
    <Header />
      <div class="notFoundTxt">
        <h1>404</h1>
      </div>
      <div class="notFoundCard">
        <v-card class="hometeCard rounded-xl" :elevation="3">
          <h3 class="ml-4 mt-2">あどみん</h3>
          <v-card-text class="cardText black--text font-weight-light">
            このページはすでに削除されているか、URLが間違っているよ
          </v-card-text>
          <v-card-actions>
            <div class="btnDiv">
              <v-btn
                class="grey--text text--darken-3 reactBtn"
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
.artBoard {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  flex-flow: column;
  justify-content: center;
}
.notFoundTxt{
  font-size: 50px;
  text-align: center;
  z-index: 0;
  margin-top: 100px;
  min-width: 520px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
}
.notFoundCard{
  margin-bottom: auto;
}
.hometeCard{
  margin: 0;
  width: 100%;
  min-width: 520px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  z-index: 0;
}
.cardText{
  font-size: 18px;
  line-height: 26px;
}
.btnDiv {
  margin: 0;
  padding: 0;
  margin-right: 6px;
}
.reactBtn {
  background-color: rgba(207, 216, 220, 0.5);
}
</style>


<script>
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";

export default {
  name: "NotFound",
  components: {
    Footer,
    Header,
  },
  methods: {
    toTopPage: function(){
      this.$router.push("/")
    }
  },
}
</script>
