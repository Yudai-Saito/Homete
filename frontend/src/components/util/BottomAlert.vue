<template>
  <CommonAlert
    :alertTransition="'slide-y-reverse-transition'"
    :alertState="bottomAlertState"
    :displayAlert="displayBottomAlert"
    :alertPosition="'bottom: 40px'"
  />
</template>

<script>
import CommonAlert from "./CommonAlert.vue";

export default {
  name: "BottomAlert",
  components: {
    CommonAlert,
  },
  computed: {
    bottomAlertState() {
      return this.$store.getters.bottomAlertState;
    },
    displayBottomAlert() {
      return this.$store.getters.displayBottomAlert;
    },
  },
};
</script>
