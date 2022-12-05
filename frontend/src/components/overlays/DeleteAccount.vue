<template>
  <v-overlay
    :value="overlayState == 'deleteAccount'"
    :light="true"
    :dark="false"
    :z-index="999"
  >
    <CommonOverlay
      usage="deleteAccount"
      titleTxt="アカウント削除"
      firstMsg="全てにチェックをつけてアカウントを削除する。"
      btnTxt="削除する"
      :onClick="deleteAccount"
    />
  </v-overlay>
</template>

<script>
import CommonOverlay from "@/components/overlays/CommonOverlay.vue";

import { getAuth } from "firebase/auth";
import axios from "axios";

export default {
  name: "DeleteAccount",
  components: {
    CommonOverlay,
  },
  computed: {
    overlayState() {
      return this.$store.getters.overlayState;
    },
  },
  methods: {
    deleteAccount() {
      const auth = getAuth();

      auth.signOut().then(() => {
        axios
          .delete("/account/delete", {
            withCredentials: true,
          })
          .then(() => {
            this.$store.dispatch("loggedOut");
            this.$store.dispatch("toTimeLine");
            this.$store.commit("updateAlertState", "deleteAccount");
            this.$router.push("/");
            setTimeout(() => {
              this.$store.dispatch("alertDeleteAccount");
            }, 500);
          });
      });
    },
  },
};
</script>
