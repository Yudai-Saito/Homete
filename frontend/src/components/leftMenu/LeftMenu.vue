<template>
  <v-col class="leftMenu">
    <div class="leftMenuFlex">
      <LeftMenuButton
        usage="alertPost"
        btnText="タイムライン"
        btnIcon="mdi-home"
      />
      <LeftMenuButton
        usage="alertLogin"
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
  gap: 40px;
  margin: auto 0;
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
