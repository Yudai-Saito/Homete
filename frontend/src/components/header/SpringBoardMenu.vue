<template>
  <v-btn
    id="sbMenuBtn"
    @click="onClickSpringBoardMenu"
    style="color: #494854"
    depressed
    plain
    color="#FFFFFF"
  >
    <v-icon style="margin-right: 5px">{{ this.icon }}</v-icon>
    {{ this.labelTxt }}
  </v-btn>
</template>

<style>
#sbMenuBtn {
  width: 100%;
  height: 49px;
  padding: 0 !important;
  font-weight: 600;
}
#sbMenuBtn .v-btn__content {
  opacity: 1 !important;
  color: #333;
  justify-content: flex-start;
}
</style>

<script>
export default {
  name: "SpringBoardMenu",
  props: ["labelTxt", "icon", "onClickSpringBoardMenu"],
};
</script>
