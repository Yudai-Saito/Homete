<template>
  <v-col class="leftMenu" cols="3">
    <div class="leftMenuFlex">
      <LeftMenuButton
        usage=""
        btnText="タイムライン"
        btnIcon="mdi-home"
      />
      <LeftMenuButton
        usage=""
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
  margin: auto;
  gap: 40px;
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
