<template>
  <v-overlay
    style="height: 100vh"
    :value="overlayState == 'login' || overlayState == 'plzLogin'"
    :light="true"
    :dark="false"
    :z-index="999"
  >
    <CommonOverlay
      usage="login"
      :firstMsg="
        overlayState == 'login'
          ? `HOMETEは誰かに褒めてもらえるやさしいSNSだよ
日常のどんなことでも投稿しちゃおう！`
          : '過去投稿の閲覧やリアクション、投稿はログインしないとできないよ！'
      "
      btnTxt="Googleでログイン"
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
