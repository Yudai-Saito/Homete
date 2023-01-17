<template>
  <v-overlay
    :value="overlayState == 'login' || overlayState == 'plzLogin'"
    :light="true"
    :dark="false"
    :z-index="999"
  >
    <CommonOverlay
      usage="login"
      titleTxt="HOMETE"
      :firstMsg="
        overlayState == 'login'
          ? 'ここに適当なサービスの説明とようこそ的な文章'
          : '過去投稿の閲覧やリアクション、投稿はログインしないとできないよ！'
      "
      btnTxt="Googleでログイン"
      descriptionTxt="ここに注意事項的な文章"
      :onClick="logIn"
    />
  </v-overlay>
</template>

<script>
import CommonOverlay from "@/components/overlays/CommonOverlay.vue";

export default {
  name: "Login",
  components: {
    CommonOverlay,
  },
  computed: {
    overlayState() {
      return this.$store.getters.overlayState;
    },
  },
  methods: {
    logIn: function () {
      this.$router.push("/login");
    },
  },
};
</script>
