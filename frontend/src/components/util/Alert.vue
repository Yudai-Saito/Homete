<template>
  <v-expand-transition>
    <v-alert
      v-show="displayAlert"
      :color="alertColor[alertState]"
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
      alertColor: {
        primary: "primary",
        greenLighten2: "green lighten-2",
        redAccent2: "red accent-2",
      },
      alertText: {
        postSuccess: "投稿しました!",
        welcomeBack: "おかえりなさい",
        logoutSuccess: "ログアウトが完了しました",
      },
    };
  },
  computed: {
    alertState() {
      return this.$store.getters.alertState;
    },
    displayAlert() {
      return this.$store.getters.displayAlert;
    },
  },
};
</script>
