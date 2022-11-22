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
                  通報
                </v-btn>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-row>
      <v-divider />
      <v-card-text class="cardMainText black--text">
        {{ homete }}
      </v-card-text>
      <div class="btns">
        <v-card-actions class="reactionBtns">
          <div
            class="reactionsDiv"
            v-for="reaction in reactions"
            :key="reaction"
          >
            <ReactionButton
              :reactionIcon="reaction"
              :postReaction="postList.post_reaction"
              :userReaction="postList.user_reaction"
              :postId="postList.post_id"
            />
          </div>
        </v-card-actions>
        <v-btn
          class="grey--text text--darken-3 reactionBtn ma-0 pa-0"
          @click="display"
          elevation="0"
          small
          outlined
          :disabled="!logged"
        >
          <div ref="addBtn">
            <v-icon>mdi-plus</v-icon>
          </div>
        </v-btn>
        <div>
          <twemoji-picker
            id="overridePicker"
            v-if="displayPicker"
            :style="{ transform: `translate(${x}px, ${y}px)` }"
            :emojiPickerDisabled="false"
            :emojiData="emojiDataAll"
            :emojiGroups="emojiGroups"
            :skinsSelection="true"
            :searchEmojisFeat="true"
            :pickerWidth="500"
            :pickerHeight="250"
            :recentEmojisFeat="true"
            :randomEmojiArray="['']"
            twemojiPath="https://twemoji.maxcdn.com/v/latest/"
            recentEmojisStorage="local"
            searchEmojiPlaceholder="Search here."
            searchEmojiNotFound="Emojis not found."
            isLoadingLabel="Loading..."
            @emojiImgAdded="emojiAdded"
          ></twemoji-picker>
        </div>
      </div>
    </v-card>
  </v-container>
</template>
<style>
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
#overridePicker div #popper-button {
  width: 0px;
  height: 0px;
}
#overridePicker div #popper-container {
  padding: 0;
  background: #f7f7f7;
  border: none;
  border-radius: 3px;
  transform: none !important;
  inset: 0 !important;
  -webkit-animation: none !important;
  animation: none !important;
  display: block;
  width: 520px;
  height: 250px;
  position: fixed !important;
  top: 0 !important;
  z-index: 99999;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup {
  width: 520px;
  height: 250px;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-search
  #search-header {
  height: 28px;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-search
  #search-header
  span {
  padding: 0;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-search
  #search-header
  span
  .emoji {
  width: 20px;
  height: 20px;
  vertical-align: -0.4rem !important;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-header {
  padding: 0 5px;
  height: 28px;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-header
  .emoji-tab {
  padding: 0 5px;
  height: 28px;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-header
  .emoji-tab
  .emoji {
  width: 28px;
  height: 28px;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  .emoji-popover-inner {
  height: 180px !important;
}
.hometeCard {
  margin: 0;
  width: 100%;
  min-width: 520px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  z-index: auto !important;
}
.hometeCard * {
  z-index: 999999;
}
.btns {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  gap: 6px;
}
.reactionBtns {
  margin: 0;
  padding: 0;
  flex-wrap: wrap;
  width: 100%;
  max-width: 330px;
  z-index: auto;
}
.reactionsDiv {
  width: 20%;
  margin-bottom: 6px;
  z-index: auto;
}
.reactionsDiv * {
  z-index: auto;
}
.addReactionBtn {
  background-color: rgba(207, 216, 220, 0.5);
  overflow: hidden;
  width: 50px;
  z-index: auto;
}
.addReactionBtn.v-btn--outlined {
  border: thin solid transparent;
}
.cardTitle {
  margin: 0;
  padding: 0;
  padding-left: 12px;
  justify-content: baseline;
  padding-bottom: 8px;
  z-index: auto;
}
.circle {
  width: 50px;
  height: 50px;
  background: #cfd8dc;
  border-radius: 50%;
  overflow: hidden;
  z-index: auto;
}
.circle * {
  z-index: auto;
}
.nameTxt {
  max-width: 280px;
  font-size: 22px;
  font-weight: 600;
  margin: 0;
  padding: 0;
  margin-left: 10px;
  z-index: auto;
}
.timeTxt {
  color: #6b7280;
  font-size: 14px;
  margin: 0;
  padding: 0;
  margin-bottom: 4px;
  margin-left: 15px;
  z-index: auto;
}
.cardMenu {
  margin: 0;
  padding: 0;
  margin-left: auto;
  z-index: auto;
}
.cardMenu * {
  z-index: auto;
}
.cardMainText {
  font-size: 16px;
  line-height: 26px;
  padding-top: 8px;
  z-index: auto;
}
</style>

<script>
import ReactionButton from "./ReactionButton.vue";
import VueResponsiveText from "vue-responsive-text";

import { createAvatar } from "@dicebear/avatars";
import * as style from "@dicebear/open-peeps";

import { TwemojiPicker } from "@kevinfaguiar/vue-twemoji-picker";
import EmojiAllData from "@/emoji/emoji-all-groups.json";
import EmojiGroups from "@/emoji/emoji-groups.json";

export default {
  name: "DisplayHomete",
  data() {
    return {
      avatorSvg: "",
      userName: "とくめいさん",
      postTime: "2022/11/17",
      homete: "",
      reactions: ["👍", "👀", "💯", "🥰", "🎉", "😄"],
      x: 0,
      y: 0,
      displayPicker: false,
    };
  },
  props: ["postList"],
  components: {
    ReactionButton,
    VueResponsiveText,
    "twemoji-picker": TwemojiPicker,
  },
  computed: {
    emojiDataAll() {
      return EmojiAllData;
    },
    emojiGroups() {
      return EmojiGroups;
    },
    logged() {
      return this.$store.getters.logged;
    },
  },
  methods: {
    emojiAdded(emojiUnicode) {
      //ここで絵文字選択イベントが発動する
      console.log(emojiUnicode);
    },
    display(e) {
      var rect = this.$refs.addBtn.getBoundingClientRect();
      console.log(rect.x);
      this.displayPicker = !this.displayPicker;
      this.x = e.offsetX;
      this.y = e.offsetY;
    },
  },
  created() {
    //投稿の本文に親コンポーネントから渡されたデータを設定
    this.homete = this.postList.post_content;

    this.avatorSvg = createAvatar(style, {
      seed: "custom-seed",
    });
  },
};
</script>
