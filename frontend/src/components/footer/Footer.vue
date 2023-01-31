<template>
  <v-footer
    style="border-top: solid #00000080 1px; justify-content: space-around"
    id="footer"
    color="rgb(242,217,193)"
    fixed
    padless
  >
    <v-col id="ftTxt" class="text-center" cols="12"> ©2023 by HOMETE </v-col>
    <FooterBtn
      usage="toTimeLine"
      ftBtnIcon="mdi-home"
      ftBtnTxt="タイムライン"
    />
    <FooterBtn
      usage="toHistory"
      ftBtnIcon="mdi-clock-outline"
      ftBtnTxt="ヒストリー"
    />
  </v-footer>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #footer {
    height: 30px;
  }
  #ftTxt {
    display: block;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #footer {
    height: 50px;
  }
  #ftTxt {
    display: none;
  }
}

#footer {
  margin: 0;
  padding: 0;
}
#ftTxt {
  position: absolute;
  color: #494854;
  margin: 0;
  padding: 0;
  font-size: 12px;
}
</style>

<script>
import FooterBtn from "./FooterBtn.vue";
export default {
  name: "Footer",
  components: {
    FooterBtn,
  },
};
</script>
