<template>
  <v-card
    width="400px"
    height="250px"
    class="mx-auto mt-5 pa-2 rounded-xl"
    v-cloak
    v-click-outside="closeOverlayCard"
  >
    <div>
      <v-btn icon plain text id="closeOverlayBtn" @click="closeOverlayCard">
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
          color="white"
        >
          <img
            v-if="usage == 'login'"
            id="googleSvg"
            src="/assets/google-login-btn.svg"
            @click="onClick"
          />
          <div id="overlayBtnTxt">{{ btnTxt }}</div>
        </v-btn>
      </v-card-actions>

      <v-card-text>
        <div v-if="usage == 'login'">{{ descriptionTxt }}</div>
      </v-card-text>
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
  color: #494854;
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
      this.$store.dispatch("invisibleLogin");
    },
  },
};
</script>

