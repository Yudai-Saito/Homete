<template>
  <v-btn
    id="leftMenuBtn"
    class="ma-0 pa-0"
    color="rgb(225 255 255)"
    rounded
    x-large
    :elevation="3"
    @click="onClick"
  >
    <v-icon v-if="btnIcon == 'mdiHome'"> {{ mdiHome }} </v-icon>
    <v-icon v-else> {{ mdiClockOutline }} </v-icon>
    {{ btnText }}
  </v-btn>
</template>

<style lang="scss">
@media (max-width: map-get($grid-breakpoints, md)) {
  // md 以下のブレークポイントでのスタイル定義
  #leftMenuBtn {
    font-size: 12px;
    color: rgb(73, 72, 84);
  }
  #leftMenuBtn span div i {
    font-size: 22px !important;
  }
}
#leftMenuBtn {
  width: 100%;
  font-weight: 600;
}
</style>

<script>
import { mdiHome } from "@mdi/js";
import { mdiClockOutline } from "@mdi/js";

export default {
  name: "LeftMenuButton",
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    contentsKey() {
      return this.$store.getters.contentsKey;
    },
  },
  data() {
    return {
      mdiHome,
      mdiClockOutline,
    };
  },
  props: ["usage", "btnText", "btnIcon"],
  methods: {
    onClick: function () {
      if (this.logged || this.usage == "toTimeLine") {
        this.$store.dispatch("invisiblePostForm");
        this.$store.commit("invisibleTwemojiPicker");
        if (
          (this.usage == "toTimeLine" && this.contentsKey == "timeline") ||
          (this.usage == "toHistory" && this.contentsKey == "history")
        ) {
          window.scrollTo({
            top: 0,
            behavior: "smooth",
          });
        } else {
          this.$store.dispatch(this.usage).then(() => {
            if (this.$route.path != "/home") {
              this.$router.push("/home");
            }
          });
        }
      } else {
        this.plzLogin();
      }
    },
    plzLogin: function () {
      this.$store.dispatch("visiblePlzLoginOverlay");
    },
  },
};
</script>
