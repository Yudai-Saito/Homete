<template>
  <v-container fluid>
    <v-card class="hometeCard rounded-xl" :elevation="3">
      <v-row class="cardTitle">
        <div class="circle">
          <v-avatar size="50">
            <svg v-html="this.avatorSvg"></svg>
          </v-avatar>
        </div>
        <div class="nameTxt mt-auto">
          <VueResponsiveText>
            {{ userName }}
          </VueResponsiveText>
        </div>
        <div class="timeTxt mt-auto">{{ postTime }}</div>
        <div class="cardMenu">
          <v-menu
            top
            offset-y
            nudge-bottom="90px"
            transition="scale-transition"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn style="bottom: 10px" icon plain v-bind="attrs" v-on="on">
                <v-icon>mdi-dots-horizontal</v-icon>
              </v-btn>
            </template>
            <v-list class="ma-0 pa-0">
              <v-list-item class="ma-0 pa-0">
                <v-btn
                  style="color: #494854; height: 50px"
                  depressed
                  plain
                  color="#FFFFFF"
                >
                  なにか
                </v-btn>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-row>
      <v-card-text class="cardMainText black--text">
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
.hometeCard {
  margin: 0;
  width: 100%;
  min-width: 520px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
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
.cardTitle {
  margin: 0;
  padding: 0;
  padding-left: 12px;
  justify-content: baseline;
}
.circle {
  width: 50px;
  height: 50px;
  background: #cfd8dc;
  border-radius: 50%;
  overflow: hidden;
}
.nameTxt {
  max-width: 280px;
  font-size: 22px;
  font-weight: 600;
  margin: 0;
  padding: 0;
  margin-left: 10px;
}
.timeTxt {
  color: #6b7280;
  font-size: 14px;
  margin: 0;
  padding: 0;
  margin-bottom: 4px;
  margin-left: 15px;
}
.cardMenu {
  margin: 0;
  padding: 0;
  margin-left: auto;
}
.cardMainText {
  font-size: 16px;
  line-height: 26px;
}
</style>

<script>
import ReactionButton from "./ReactionButton.vue";
import VueResponsiveText from "vue-responsive-text";

import { createAvatar } from '@dicebear/avatars';
import * as style from '@dicebear/open-peeps';

export default {
  name: "DisplayHomete",
  data() {
    return {
      avatorSvg: "",
      userName: "とくめいさん",
      postTime: "2022/11/17",
      homete: "",
      reactions: ["👍", "👀", "💯", "🥰", "🎉"],
    };
  },
  props: ["postList"],
  components: {
    ReactionButton,
    VueResponsiveText,
  },
  created() {
    //投稿の本文に親コンポーネントから渡されたデータを設定
    this.homete = this.postList.post_content;

    this.avatorSvg = createAvatar(style, {
      seed: 'cu',
    })
  },
};
</script>
