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
      firstMsg="削除をすると戻すことはできません。"
      btnTxt="削除する"
      :onClick="deletePost"
    />
  </v-overlay>
</template>

<style>
#reportPost .v-overlay__content {
  width: 100%;
}
</style>

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
            post_id: this.$store.getters.postId,
          },
          withCredentials: true,
        })
        .then(() => {
          this.$store.commit("updateProcess", true);
          this.$store.commit("updatePostsProcess", "delete");
          this.$store.dispatch("invisibleCommonOverlay");
          this.$store.dispatch("alertDeletePost");
        });
    },
  },
};
</script>
