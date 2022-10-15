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
        document.title = "HOMETE";
      }
    },
  },

  mounted: function () {
    let routeInstance = this.$route;
    this.createTitleDesc(routeInstance);
  },

  watch: {
    $route(routeInstance) {
      this.createTitleDesc(routeInstance);
    },
  },
};
</script>
