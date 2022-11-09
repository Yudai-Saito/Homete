<template>
  <v-col class="leftMenu">
    <div class="sideMenuButton">
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
    </div>
  </v-col>
</template>
<style>
.leftMenu{
  width: 100%;
  height: 80vh;
  min-height: 80vh;
  max-height: 80vh;
  margin: 0;
  padding: 0;
}
.sideMenuButton {
  display: flex;
  flex-flow: column;
  z-index: 100;
}
</style>

<script>
import axios from "axios";
import LeftMenuButton from "./LeftMenuButton.vue";

export default {
  name: "SideMenu",
  computed: {
    isVisiblePostHomete() {
      return this.$store.getters.isVisiblePostHomete;
    },
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
