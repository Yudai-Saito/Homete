<template>
  <CommonAlert
    :alertTransition="'slide-y-transition'"
    :alertState="topAlertState"
    :displayAlert="displayTopAlert"
    :alertPosition="'top: 75px; border-radius:50px; height:40px; padding-top:8px;'"
    @click="onClick"
  />
</template>

<script>
import CommonAlert from "./CommonAlert.vue";

export default {
  name: "TopAlert",
  components: {
    CommonAlert,
  },
  computed: {
    topAlertState() {
      return this.$store.getters.topAlertState;
    },
    displayTopAlert() {
      return this.$store.getters.displayTopAlert;
    },
  },
  methods: {
    onClick: function () {
      if (this.alertState == "newPost") {
        this.$store.commit("updateTopAlert", false);
      }
    },
  },
};
</script>
