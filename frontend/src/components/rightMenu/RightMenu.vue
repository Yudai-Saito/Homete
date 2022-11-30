<template>
  <v-col class="rightMenu" cols="12">
    <PostForm />
  </v-col>
</template>
<style>
.rightMenu {
  display: flex;
  height: 100vh;
  min-height: 100vh;
  max-height: 100vh;
  margin: 0;
  padding: 0;
}
</style>

<script>
import PostForm from "@/components/util/PostForm.vue";

export default {
  name: "RightMenu",
  computed: {
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    },
  },
  components: {
    PostForm,
  },
  methods: {
    clickPost: function () {
      if (this.logged) {
        this.$store.dispatch("visiblePostForm");
      } else {
        //ログインを促すポップアップやオーバーレイ
      }
    },
  },
};
</script>
