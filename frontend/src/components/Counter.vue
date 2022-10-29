<template>
  <div>
    <button @click="increment">increment {{ step }}</button>
    <span>total {{ count }}</span>
  </div>
</template>

<script>
//開発環境におけるテスト用コンポーネント
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
      this.$store.dispatch("toTrueLogin");
    },
  },
};
</script>

<style scoped>
</style>
