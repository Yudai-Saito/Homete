<template>
  <div style="display: flex; justify-content: center">
    <v-alert
      :transition="alertTransition"
      v-show="displayAlert"
      :color="alertColor[alertState]"
      :type="alertState == 'error' ? 'error' : 'success'"
      id="alertShape"
      :style="alertPosition"
      @click="onClick"
    >
      {{ alertText[alertState] }}
    </v-alert>
  </div>
</template>

<style>
#alertShape {
  position: fixed;
  z-index: 999;
  margin: 0;
  border-radius: 20px;
}
</style>

<script>
export default {
  name: "CommonAlert",
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
  props: ["alertTransition", "alertState", "displayAlert", "alertPosition"],
  methods: {
    onClick: function () {
      if (this.alertState == "newPost") {
        this.$store.commit("updateTopAlert", false);
      }
    },
  },
};
</script>
