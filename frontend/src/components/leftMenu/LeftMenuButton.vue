<template>
  <v-col>
    <v-btn rounded text v-on:click="onClick">
      <v-icon> {{ btnIcon }} </v-icon>
      {{ btnText }}
    </v-btn>
  </v-col>
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
