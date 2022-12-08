<template>
  <div style="display: flex; justify-content: center">
    <v-slide-y-transition>
      <v-btn v-show="displayTopAlert" id="btnPosition" @click="onClick">
        <CommonAlert
          :alertTransition="'slide-y-transition'"
          :alertState="topAlertState"
          :displayAlert="true"
          :alertPosition="'border-radius:50px; height:40px; padding-top:8px; z-index:auto'"
        />
      </v-btn>
    </v-slide-y-transition>
  </div>
</template>

<style>
#btnPosition {
  position: fixed;
  top: 75px;
  height: 40px;
  width: 248px;
  border-radius: 50px;
  z-index: 900;
  background-color: transparent;
}
</style>

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
      this.$store.commit("updateTopAlert", false);
    },
  },
};
</script>
