<template>
  <v-col class="leftMenu" cols="12">
    <div class="leftMenuFlex">
      <LeftMenuButton
        usage="toTimeLine"
        btnText="タイムライン"
        btnIcon="mdi-home"
      />
      <LeftMenuButton
        usage="toHistory"
        btnText="ヒストリー"
        btnIcon="mdi-history"
      />
      <v-btn
        class="aboutBtn ma-0 pa-0"
        color="#CFD8DC"
        rounded
        x-large
        :elevation="3"
        v-on:click="onClick"
      >
        HOMETEについて
      </v-btn>
    </div>
  </v-col>
</template>
<style>
.aboutBtn {
  position: absolute;
  bottom: 50px;
  height: 30px !important;
  width: 50%;
  left: 50%;
  transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  font-size: 12px !important;
}
.leftMenu {
  display: flex;
  height: 100vh;
  min-height: 100vh;
  max-height: 100vh;
  margin: 0;
  padding: 0;
}
.leftMenuFlex {
  display: flex;
  flex-flow: column;
  margin: auto 36px;
  gap: 40px;
  width: 100%;
}
.leftMenuFlex button {
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
}
.leftMenuFlex button .v-ripple__container {
  height: 100%;
  width: 100%;
}
</style>

<script>
import LeftMenuButton from "./LeftMenuButton.vue";

export default {
  name: "LeftMenu",
  components: {
    LeftMenuButton,
  },
  methods: {
    onClick: function () {
      if (this.$route.path != "/about") {
        this.$store.dispatch("toAbout");
        this.$router.push("/about");
      }
    },
  },
};
</script>
