<template>
  <v-btn
    class="ma-0 pa-0 leftMenuBtn"
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

<style>
.leftMenuBtn {
  width: 175px;
}
</style>

<script>
export default {
  name: "LeftMenuButton",
  props: ["usage", "btnText", "btnIcon"],
  methods: {
    onClick: function () {
      this.$store.dispatch(this.usage);
    },
  },
};
</script>
