<template>
  <v-container fluid>
    <v-card class="hometeCard rounded-xl" :elevation="3">
      <h3 class="ml-4 mt-2">とくめいさん</h3>
      <v-card-text class="cardText black--text font-weight-light">
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
.hometeCard{
  margin: 0;
  width: 100%;
  min-width: 520px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
}
.cardText{
  font-size: 18px;
  line-height: 26px;
}
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
import ReactionButton from "./ReactionButton.vue";
export default {
  name: "DisplayHomete",
  data() {
    return {
      homete: "",
      reactions:["👍", "👀", "💯", "🥰", "🎉"],
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
