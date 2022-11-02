<template>
  <v-container fluid>
    <v-card outlined>
      <h4 class="ml-4 mt-2">匿名さん</h4>
      <v-divider class="mx-4"></v-divider>
      <v-card-text class="black--text">
        {{ homete }}
      </v-card-text>
      <v-card-actions>
        <ul class="horizontalListWide">
          <li v-for="reaction in reactions" :key="reaction">
            <ReactionButton
              :reactionIcon="reaction"
              :postReaction="postList.post_reaction"
              :userReaction="postList.user_reaction"
              :postId="postList.post_id"
            />
          </li>
        </ul>
      </v-card-actions>
    </v-card>
  </v-container>
</template>
<style>
.horizontalListWide {
  /* 縦スクロール設定 */
  overflow: auto;

  white-space: pre-line;
  -webkit-overflow-scrolling: touch;
  padding: 0;
  margin: 0;
}
.horizontalListWide li {
  /* PC画面時のリアクションボタンの折り返し表示 */
  position: relative;
  display: inline-block;
  right: 1em;
}
</style>

<script>
import ReactionButton from "../components/ReactionButton";
export default {
  name: "DisplayHomete",
  computed: {
    reactions() {
      return this.$store.getters.reactions;
    },
  },
  data() {
    return {
      homete: "",
    };
  },
  props: ["postList"],
  components: {
    ReactionButton,
  },
  created() {
    //投稿の本文に親コンポーネントから渡されたデータを設定
    this.homete = this.postList.post_content;
  },
};
</script>
