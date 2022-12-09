<template>
  <v-footer
    style="border-top: solid #00000080 1px; justify-content: space-around"
    id="footer"
    color="#BABDBE"
    fixed
    padless
  >
    <v-col id="ftTxt" class="text-center" cols="12"> ©2022 by HOMETE </v-col>
    <v-btn plain class="ftBtn"></v-btn>
    <v-btn plain class="ftBtn"></v-btn>
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
  .ftBtn {
    display: none;
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
  .ftBtn {
    display: block;
    height: 50px !important;
    border-radius: 0px !important;
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
export default {
  name: "Footer",
};
</script>
