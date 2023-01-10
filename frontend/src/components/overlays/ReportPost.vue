<template>
  <v-overlay
    id="reportPost"
    :value="overlayState == 'reportPost'"
    :light="true"
    :dark="false"
    :z-index="999"
  >
    <CommonOverlay
      usage="reportPost"
      titleTxt="注意"
      firstMsg="この投稿を管理者に通報します。"
      btnTxt="通報する"
      :onClick="reportPost"
    />
  </v-overlay>
</template>

<style>
#reportPost .v-overlay__content {
  width: 100%;
}
</style>

<script>
import CommonOverlay from "@/components/overlays/CommonOverlay.vue";

export default {
  name: "ReportPost",
  components: {
    CommonOverlay,
  },
  computed: {
    overlayState() {
      return this.$store.getters.overlayState;
    },
  },
  methods: {
    reportPost: function () {
      this.$store.dispatch("invisibleCommonOverlay");
      this.$store.dispatch("alertReportSuccess");
    },
  },
};
</script>
