<template>
  <v-expand-transition>
    <v-alert
      v-show="isAlertPost"
      :color=alertColor[alertState]
      text
      type="success"
      class="alertSucess"
    >
      {{ alertText[alertState] }}
    </v-alert>
  </v-expand-transition>
</template>

<style>
.alertSucess {
  width: 90%;
  margin-right: auto;
  margin-left: auto;
}
</style>

<script>
export default {
  data() {
    return {
      //[投稿、ログイン、ログアウト]
      alertState: 0,
      alertColor: ["primary", "green lighten-2", "red accent-2"],
      alertText: [
        "投稿しました!",
        "おかえりなさい",
        "ログアウトが完了しました",
      ],
    };
  },
  computed: {
    isAlertPost() {
      return this.$store.getters.isAlertPost;
    },
  },
};
</script>
