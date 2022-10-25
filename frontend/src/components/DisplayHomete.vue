<template>
  <v-container fluid>
    <v-card outlined>
      <h4 class="ml-4 mt-2">匿名さん</h4>
      <v-divider class="mx-4"></v-divider>
      <v-card-text class="black--text">
        {{ homete }}
      </v-card-text>
      <v-card-actions>
        <ul class="horizontalListWide d-none d-sm-block">
          <li v-for="reaction in reactions" :key="reaction">
            <ReactionButton
              :reactionIcon="reaction"
              :postReaction="postList.post_reaction"
              :userReaction="postList.user_reaction"
              :postId="postList.post_id"
            />
          </li>
        </ul>
        <ul class="horizontalList d-block d-sm-none">
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
.horizontalList {
  /* 横スクロール設定 */
  overflow-x: auto;
  /* IE, Edgeにおけるスクロールバーの削除対応 */
  -ms-overflow-style: none;
  /* Firefoxにおけるスクロールバーの削除対応 */
  scrollbar-width: none;

  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
  padding: 0;
  margin: 0;
}
/* Chrome, Safariにおけるスクロールバーの削除対応 */
.horizontalList::-webkit-scrollbar {
  display: none;
}
.horizontalList li {
  /* スマホ画面時のリアクションボタンの横スクロール対応 */
  position: relative;
  display: inline-block;
  right: 1em;
}
</style>

<script>
import ReactionButton from "../components/ReactionButton";
export default {
  name: "DisplayHomete",
  computed:{
    reactions(){
      return this.$store.getters.reactions;
    }
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
