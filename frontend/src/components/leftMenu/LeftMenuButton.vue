<template>
  <v-btn  class="ma-0 pa-0" rounded text v-on:click="onClick">
    <v-icon> {{ btnIcon }} </v-icon>
    {{ btnText }}
  </v-btn>
</template>

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
