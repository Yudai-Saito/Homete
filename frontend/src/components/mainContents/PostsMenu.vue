<template>
  <v-btn
    @click="onClick"
    style="color: #494854; height: 50px"
    depressed
    plain
    color="#FFFFFF"
  >
    {{ this.labelTxt }}
  </v-btn>
</template>

<script>
export default {
  name: "PostsMenu",
  props: ["labelTxt", "onClick"],
};
</script>
