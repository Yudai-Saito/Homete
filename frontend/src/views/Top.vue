<template>
  <v-app class="artBoard blue-grey lighten-5">
    <Header />
    <Login />
    <DeletePost />
    <ReportPost />
    <div>
      <Alert />
      <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
        <v-col cols="3">
          <LeftMenu class="SideMenuSticky" />
        </v-col>
        <v-col cols="6">
          <PostContents v-if="contentsKey == 'timeline'" :key="contentsKey" />
          <PostContents
            v-if="contentsKey == 'history'"
            :channel="contentsKey"
            :key="contentsKey"
          />
        </v-col>
        <v-col cols="3">
          <RightMenu class="SideMenuSticky" />
        </v-col>
      </v-row>
    </div>
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
.contentsFlex {
  width: 100%;
  flex-wrap: nowrap;
}
.SideMenuSticky {
  position: sticky;
  top: 0;
  flex-wrap: nowrap;
  margin: 0;
  padding: 0;
}
</style>


<script>
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import PostContents from "@/components/mainContents/PostContents.vue";
import RightMenu from "@/components/rightMenu/RightMenu.vue";
import Login from "@/components/overlays/Login.vue";
import DeletePost from "@/components/overlays/DeletePost.vue";
import ReportPost from "@/components/overlays/ReportPost.vue";
import Alert from "@/components/util/Alert.vue";
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";

export default {
  name: "Top",
  components: {
    LeftMenu,
    PostContents,
    RightMenu,
    Login,
    DeletePost,
    ReportPost,
    Alert,
    Footer,
    Header,
  },
  computed: {
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    },
    overlayState() {
      return this.$store.getters.overlayState;
    },
    contentsKey() {
      return this.$store.getters.contentsKey;
    },
  },
  methods: {
    logIn: function () {
      this.$router.push("/login");
    },
  },
  mounted() {
    window.onload = () => {
      this.$store.dispatch("invisiblePostForm");
      this.$store.dispatch("invisibleCommonOverlay");
      this.$store.dispatch("toTimeLine");
    };
  },
};
</script>
