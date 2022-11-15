<template>
  <v-app class="artBoard">
    <Header />
    <v-overlay
      :value="displayLogin"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <Login />
    </v-overlay>
    <v-overlay
      :value="displayPostForm"
      :dark="false"
      :light="true"
      :z-index="999"
    >
      <PostForm />
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
import PostForm from "@/components/util/PostForm.vue";

export default {
  name: "Top",
  computed: {
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    },
    displayLogin() {
      return this.$store.getters.displayLogin;
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
    PostForm,
  },
  mounted() {
    window.onload = () => {
      this.$store.dispatch("invisiblePostForm");
      this.$store.dispatch("invisibleLogin");
    };
  },
};
</script>
