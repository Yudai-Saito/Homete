<template>
  <v-btn
    id="leftMenuBtn"
    class="ma-0 pa-0"
    color="#CFD8DC"
    rounded
    x-large
    :elevation="3"
    v-on:click="onClick"
  >
    <v-icon> {{ btnIcon }} </v-icon>
    {{ btnText }}
  </v-btn>
</template>

<style lang="scss">
@media (max-width: map-get($grid-breakpoints, md)) {
  // md 以下のブレークポイントでのスタイル定義
  #leftMenuBtn {
    font-size: 12px;
  }
  #leftMenuBtn span div i {
    font-size: 22px !important;
  }
}
#leftMenuBtn {
  width: 100%;
}
</style>

<script>
export default {
  name: "LeftMenuButton",
  props: ["usage", "btnText", "btnIcon"],
  methods: {
    onClick: function () {
      this.$store.dispatch(this.usage);
      if (this.$route.path != "/") {
        this.$router.push("/");
      }
    },
  },
};
</script>
