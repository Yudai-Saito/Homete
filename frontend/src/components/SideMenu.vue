<template>
  <v-container class="sideContainer">
    <v-row justify="start" class="mt-7 sideMenuButton">
      <LeftMenuButton
        usage="alertPost"
        btnText="タイムライン"
        btnIcon="mdi-home"
      />
      <LeftMenuButton
        usage="alertLogin"
        btnText="ヒストリー"
        btnIcon="mdi-history"
      />
    </v-row>
  </v-container>
</template>
<style>
.sideContainer {
  height: 100vh;
}
.sideMenuButton {
  position: relative;
  z-index: 100;
  margin-bottom: 5pt;
}
</style>

<script>
import axios from "axios";
import LeftMenuButton from "./LeftMenuButton";

export default {
  name: "SideMenu",
  computed: {
    isVisiblePostHomete() {
      return this.$store.getters.isVisiblePostHomete;
    },
  },
  data() {
    return {
      t: ["alertLogin", "a"],
    };
  },
  components: {
    LeftMenuButton,
  },
  methods: {
    alertPostVisible: function () {
      this.$store.dispatch(this.t[0]);
    },
    visibleCard: function () {
      this.alertPostVisible();
      this.$store.dispatch("toVisiblePostHomete");
    },
    logout: function () {
      axios
        .post(
          "/user/logout",
          {
            //
          },
          {
            withCredentials: true,
          }
        )
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            this.$emit("logout");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
