<template>
  <v-app class="artBoard">
    <Header />
    <v-overlay
      :value="isVisiblePostHomete"
      :dark="false"
      :light="true"
      :z-index="999"
    >
      <PostHomete />
    </v-overlay>
    <v-container class="contents mx-auto">
      <Alert />
      <v-row justify="center" class="contentsFlex mx-auto my-auto">
        <LeftMenu class="SideMenuSticky" v-on:logout="isLoginCheck" />
        <TimeLine />
        <v-col class="ma-0 pa-0"> </v-col>
      </v-row>
    </v-container>
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
.contents{
  width: 1000px;
  margin: 0;
  padding: 0;
}
.contentsFlex {
  display: flex;
}
.SideMenuSticky {
  position: sticky;
  top: 0;
}
</style>


<script>
import LeftMenu from "../components/leftMenu/LeftMenu.vue";
import TimeLine from "../components/mainContents/TimeLine.vue";
import Alert from "../components/util/Alert.vue";
import Footer from "../components/util/Footer.vue";
import Header from "../components/util/Header.vue";
import PostHomete from "../components/util/PostHomete.vue";

export default {
  name: "Top",
  computed: {
    isVisiblePostHomete() {
      return this.$store.getters.isVisiblePostHomete;
    },
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  components: {
    LeftMenu,
    TimeLine,
    Alert,
    Footer,
    Header,
    PostHomete,
  },
  methods: {
    isLoginCheck: function () {
      this.$store.dispatch("toFalseLogin");
      setTimeout(() => {
        this.$store.dispatch("alertLogout");
      }, 500);
    },
  },
  created() {
    //ログイン判定
    if (this.$cookies.isKey("expire") == true) {
      this.$store.dispatch("toTrueLogin");
      setTimeout(() => {
          this.$store.dispatch("alertLogin");
        }, 1500);
    } else {
      this.$store.dispatch("toFalseLogin");
    }
  },
  mounted() {
    window.onload = () => {
      this.$store.dispatch("toFalseAlertPost");
      this.$store.dispatch("toInvisiblePostHomete");
    };
  },
};
</script>
