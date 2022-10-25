<template>
  <div>
    <button @click="increment">increment {{ step }}</button>
    <span>total {{ count }}</span>
  </div>
</template>

<script>
export default {
  name: "Counter",
  computed: {
    step() {
      return this.$store.getters.step;
    },
    count() {
      return this.$store.getters.count;
    },
  },
  methods: {
    increment() {
      this.$store.dispatch("increment");
    },
  },
};
</script>

<style scoped>
</style>
