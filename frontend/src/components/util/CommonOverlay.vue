<template>
  <v-card
    width="400px"
    class="mx-auto pa-2 rounded-xl"
    v-cloak
    v-click-outside="closeOverlayCard"
  >
    <div style="margin: 10px">
      <v-btn
        v-if="usage == 'login'"
        icon
        plain
        text
        id="closeOverlayBtn"
        @click="closeOverlayCard"
      >
        <v-icon color="#23282F">mdi-close</v-icon>
      </v-btn>
      <v-card-title class="justify-center">{{ titleTxt }}</v-card-title>
      <v-card-text>
        <div>{{ firstMsg }}</div>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
          large
          @click="onClick"
          class="text-transform ma-0 pa-0 rounded-lg"
          :color="usage == 'login' ? 'white' : 'red'"
        >
          <img
            v-if="usage == 'login'"
            id="googleSvg"
            src="/assets/google-login-btn.svg"
            @click="onClick"
          />
          <div
            :style="usage == 'login' ? 'color: #494854' : 'color: white'"
            id="overlayBtnTxt"
          >
            {{ btnTxt }}
          </div>
        </v-btn>
      </v-card-actions>

      <v-card-text v-if="usage == 'login'">
        <div>{{ descriptionTxt }}</div>
      </v-card-text>
      <v-card-actions v-else class="justify-center">
        <v-btn
          style="margin-top: 10px"
          large
          @click="closeOverlayCard"
          class="text-transform ma-0 pa-0 rounded-lg"
          color="white"
        >
          <div id="overlayBtnTxt">戻る</div>
        </v-btn>
      </v-card-actions>
    </div>
  </v-card>
</template>

<style>
#closeOverlayBtn {
  justify-content: center;
  position: absolute !important;
  left: 350px !important;
}
#overlayBtnTxt {
  margin-right: 8px;
  margin-left: 8px;
  text-transform: none;
  font-weight: 600;
}
#googleSvg {
  background-image: url("/assets/google-login-btn.svg");
}
</style>

<script>
export default {
  name: "CommonOverlay",
  props: [
    "usage",
    "titleTxt",
    "firstMsg",
    "btnTxt",
    "descriptionTxt",
    "onClick",
  ],
  methods: {
    closeOverlayCard: function () {
      this.$store.dispatch("invisibleCommonOverlay");
    },
  },
};
</script>

