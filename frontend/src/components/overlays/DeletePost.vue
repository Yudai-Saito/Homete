<template>
  <v-overlay
    :value="overlayState == 'deletePost'"
    :light="true"
    :dark="false"
    :z-index="999"
  >
    <CommonOverlay
      usage="deletePost"
      titleTxt="本当に削除しますか？"
      firstMsg="この投稿はタイムライン、あなたのヒストリーから削除されます。"
      btnTxt="削除する"
      :onClick="deletePost"
    />
  </v-overlay>
</template>

<script>
import axios from "axios";

import CommonOverlay from "@/components/overlays/CommonOverlay.vue";

export default {
  name: "DeletePost",
  components: {
    CommonOverlay,
  },
  computed: {
    overlayState() {
      return this.$store.getters.overlayState;
    },
  },
  methods: {
    deletePost: function () {
      axios
        .delete("/posts", {
          params: {
            post_id: this.$store.getters.deletePostId,
          },
          withCredentials: true,
        })
        .then(() => {
          this.$store.commit("updateDeletePostFlag", true);
          this.$store.dispatch("invisibleCommonOverlay");
        });
    },
  },
};
</script>
