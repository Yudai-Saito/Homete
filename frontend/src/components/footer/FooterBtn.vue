<template>
  <v-btn
    id="ftBtn"
    class="d-md-none"
    :class="contentName == ftBtnTxt ? 'activeFtBtn' : 'nonActiveFtBtn'"
    :ripple="false"
    plain
    @click="onClick"
  >
    <div id="ftBtnIcon">
      <v-icon v-if="ftBtnIcon == 'mdiHome'">{{ mdiHome }}</v-icon>
      <v-icon v-else>{{ mdiClockOutline }}</v-icon>
    </div>
    <div id="ftBtnTxt">{{ ftBtnTxt }}</div>
  </v-btn>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #ftBtn,
  #ftBtnTxt,
  #ftBtnIcon {
    display: none;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #ftBtn {
    height: 50px !important;
    width: 50px;
    border-radius: 0px !important;
  }
  #ftBtn .v-btn__content {
    flex-flow: column;
  }
  #ftBtnTxt {
    font-size: 10px;
    transform: scale(0.75);
  }
}

.activeFtBtn .v-btn__content {
  opacity: 1 !important;
}

.nonActiveFtBtn {
  color: rgba(0, 0, 0, 0.75) !important;
}
</style>

<script>
import { mdiHome } from "@mdi/js";
import { mdiClockOutline } from "@mdi/js";

export default {
  name: "FooterBtn",
  computed: {
    contentName() {
      return this.$store.getters.contentName;
    },
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
  props: ["usage", "ftBtnIcon", "ftBtnTxt"],
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
          this.$store.dispatch("invisibleMenu");
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
