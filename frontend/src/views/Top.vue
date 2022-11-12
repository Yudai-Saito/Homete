<template>
  <v-app class="artBoard">
    <Header />
    <v-overlay
      :value="visibleLoginWindow"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <Login />
    </v-overlay>
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
        <LeftMenu class="SideMenuSticky" />
        <TimeLine />
        <RightMenu class="SideMenuSticky" />
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
.contents {
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
import Login from "@/components/Account/Login.vue";
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import TimeLine from "@/components/mainContents/TimeLine.vue";
import RightMenu from "@/components/rightMenu/RightMenu.vue";
import Alert from "@/components/util/Alert.vue";
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";
import PostHomete from "@/components/util/PostHomete.vue";

export default {
  name: "Top",
  computed: {
    isVisiblePostHomete() {
      return this.$store.getters.isVisiblePostHomete;
    },
    isLogin() {
      return this.$store.getters.isLogin;
    },
    visibleLoginWindow() {
      return this.$store.getters.visibleLoginWindow;
    },
  },
  components: {
    Login,
    LeftMenu,
    TimeLine,
    RightMenu,
    Alert,
    Footer,
    Header,
    PostHomete,
  },
  mounted() {
    window.onload = () => {
      this.$store.dispatch("toFalseAlertPost");
      this.$store.dispatch("toInvisiblePostHomete");
      this.$store.dispatch("toInvisibleLoginWindow");
    };
  },
};
</script>
