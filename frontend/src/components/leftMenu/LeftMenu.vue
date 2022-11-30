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
    </div>
  </v-col>
</template>
<style>
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
};
</script>
