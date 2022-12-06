<template>
  <div style="display: flex; justify-content: center">
    <v-alert
      :transition="
        alertState == 'newPost'
          ? 'slide-y-transition'
          : 'slide-y-reverse-transition'
      "
      v-show="displayAlert"
      :color="alertColor[alertState]"
      :type="alertState == 'error' ? 'error' : 'success'"
      id="alertPosition"
    >
      {{ alertText[alertState] }}
    </v-alert>
  </div>
</template>

<style>
#alertPosition {
  position: fixed;
  bottom: 40px;
  z-index: 999999;
  margin: 0;
  border-radius: 20px;
}
</style>

<script>
export default {
  name: "Alert",
  computed: {
    alertState() {
      return this.$store.getters.alertState;
    },
    displayAlert() {
      return this.$store.getters.displayAlert;
    },
  },
  data() {
    return {
      //[投稿完了、投稿削除、ログイン、ログアウト、アカウント削除、通報完了]
      alertColor: {
        newPost: "primary",
        error: "red accent-2",
        postSuccess: "primary",
        deletePost: "red accent-2",
        login: "green lighten-2",
        logout: "green lighten-2",
        deleteAccount: "red accent-2",
        reportSuccess: "primary",
      },
      alertText: {
        newPost: "新しい投稿があります",
        error: "通信に失敗しました。時間をおいてもう一度お願いします。",
        postSuccess: "投稿しました!",
        deletePost: "投稿を削除しました",
        login: "おかえりなさい",
        logout: "またのご利用をお待ちしています",
        deleteAccount: "アカウントを削除しました",
        reportSuccess: "通報しました",
      },
    };
  },
};
</script>
