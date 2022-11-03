<template>
  <v-app>
    <v-overlay
      :value="isVisiblePostHomete"
      :dark="false"
      :light="true"
      :z-index="999"
    >
      <PostHomete />
    </v-overlay>
    <v-container fluid class="mainContainer mx-auto">
      <Alert />
      <v-row justify="center" class="mx-auto">
        <LeftMenu class="leftMenuContent" v-on:logout="isLoginCheck" />
        <v-divider vertical />
        <TimeLine />
        <v-divider vertical />
        <v-col class="ma-0 pa-0"> </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>
<style>
.mainContainer {
  max-width: 1200px;
  width: 100%;
  height: 100%;
}
.leftMenuContent {
  position: sticky;
  top: 0px;
}
</style>


<script>
import LeftMenu from "../components/leftMenu/LeftMenu.vue";
import TimeLine from "../components/mainContents/TimeLine.vue";
import Alert from "../components/util/Alert.vue";
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
    PostHomete,
  },
  methods: {
    isLoginCheck: function () {
      this.$store.dispatch("toFalseLogin");
      localStorage.clear("firstLogin");
      setTimeout(() => {
        this.$store.dispatch("alertLogout");
      }, 500);
    },
  },
  created() {
    if (this.$cookies.isKey("expire") == true) {
      this.$store.dispatch("toTrueLogin");
      if (!localStorage.getItem("firstLogin")) {
        setTimeout(() => {
          this.$store.dispatch("alertLogin");
        }, 1500);
      }
      localStorage.setItem("firstLogin", true);
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
