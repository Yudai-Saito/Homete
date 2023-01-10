<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  methods: {
    createTitleDesc: function (routeInstance) {
      if (routeInstance.meta.title) {
        let setTitle = routeInstance.meta.title + " | HOMETE";
        document.title = setTitle;
      } else {
        document.title = "HOMETE | 日常を全肯定されるSNS";
      }
    },
  },

  mounted: function () {
    let routeInstance = this.$route;
    this.createTitleDesc(routeInstance);
    window.onload = () => {
      this.$store.dispatch("invisiblePostForm");
      this.$store.dispatch("invisibleCommonOverlay");
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("invisibleAlert");
      this.$store.commit("invisibleTwemojiPicker");
      if (this.$route.path == "/") {
        this.$store.dispatch("toTimeLine");
      }
    };
  },

  watch: {
    $route(routeInstance) {
      this.createTitleDesc(routeInstance);
    },
  },
};
</script>
