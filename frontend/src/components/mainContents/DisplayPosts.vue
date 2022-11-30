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
        <v-card-actions class="reactionBtns" v-click-outside="closePicker">
          <div
            class="reactionsDiv"
            v-for="reaction in reactions"
            :key="reaction"
          >
            <ReactionButton
              :reactionIcon="reaction"
              :postReaction="postList.post_reactions"
              :userReaction="postList.user_reaction"
              :postId="postList.post_id"
              v-on:deleteReaction="deleteReactions"
            />
          </div>
          <v-btn
            class="grey--text text--darken-3 addReactionBtn pa-0"
            v-if="displayAddBtn"
            @click="displayEmojiPicker"
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
              :pickerWidth="520"
              :pickerHeight="400"
              :recentEmojisFeat="true"
              :randomEmojiArray="['']"
              :pickerAutoFlip="false"
              :pickerCloseOnClickaway="false"
              twemojiPath="https://twemoji.maxcdn.com/v/latest/"
              recentEmojisStorage="local"
              searchEmojiPlaceholder="絵文字を検索"
              searchEmojiNotFound="絵文字が見つかりませんでした😭"
              isLoadingLabel="検索中...🔍"
              @emojiUnicodeAdded="emojiAdded"
            ></twemoji-picker>
          </div>
        </v-card-actions>
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
#overridePicker {
  position: fixed;
  inset: 0;
  width: 520px;
  height: 400px;
}
#overridePicker div #popper-button {
  width: 0px;
  height: 0px;
}
#overridePicker div #popper-container {
  padding: 0;
  background: #f7f7f7;
  border: none;
  border-radius: 10px;
  transform: none !important;
  inset: 0 !important;
  -webkit-animation: none !important;
  animation: none !important;
  display: block;
  width: 520px;
  height: 400px;
  position: fixed !important;
  top: 0 !important;
  z-index: 2147483647;
  overflow: hidden;
}
#overridePicker div #popper-container #arrow {
  display: none !important;
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
  padding: 0 11px;
  height: 33px;
  border-bottom: solid #cfd8dc 1px;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  #emoji-popover-header
  .emoji-tab {
  padding: 0 7px;
  height: 33px;
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
  height: 300px !important;
  width: 100% !important;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  .emoji-popover-inner
  div
  .emoji-list {
  margin: 0 5px !important;
}
.hometeCard {
  margin: 0;
  width: 100%;
  min-width: 520px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  padding-bottom: 10px;
  z-index: auto !important;
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
}
.hometeCard * {
  z-index: 99;
}
.btns {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
}
.reactionBtns {
  margin: 0;
  padding: 0;
  flex-wrap: wrap;
  max-width: 450px;
  z-index: auto;
}
.reactionsDiv {
  margin-bottom: 10px;
  margin-right: 10px;
  z-index: auto;
}
.reactionsDiv * {
  z-index: auto;
}
.addReactionBtn {
  background-color: rgba(144, 152, 156, 0.5);
  overflow: hidden;
  height: 24px !important;
  width: 24px;
  min-width: 24px !important;
  z-index: auto;
  margin-bottom: auto;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
.addReactionBtn * {
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
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
  display: flex;
  justify-content: flex-end;
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

import ClickOutside from "vue-click-outside";

export default {
  name: "DisplayHomete",
  directives: {
    ClickOutside,
  },
  data() {
    return {
      avatorSvg: "",
      userName: "とくめいさん",
      postTime: "2022/11/17",
      homete: "",
      reactions: ["👍", "👀", "💯", "🥰", "🎉"],
      x: 0,
      y: 0,
      displayPicker: false,
      displayAddBtn: true,
      fhp: 0,
      ap: 0,
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
      if (!this.reactions.includes(emojiUnicode)) {
        this.postList.user_reaction.push(emojiUnicode);
        this.postList.post_reactions.push({
          reaction: emojiUnicode,
          count: 1,
        });
        this.reactions.push(emojiUnicode);
      }
      if (this.reactions.length >= 20) {
        this.displayAddBtn = false;
      }
      this.displayPicker = false;
    },
    displayEmojiPicker() {
      var rect = this.$refs.addBtn.getBoundingClientRect();
      if (rect.x >= window.innerWidth / 2) {
        this.x = rect.x - 526;
      } else {
        this.x = rect.x + 33;
      }
      if (rect.y >= window.innerHeight - 410) {
        this.y = window.innerHeight - 410;
      } else {
        this.y = rect.y;
      }
      this.displayPicker = !this.displayPicker;
    },
    closePicker() {
      this.displayPicker = false;
    },
    deleteReactions(icon) {
      var rVal = icon;
      var rIndex = this.reactions.indexOf(rVal);
      this.reactions.splice(rIndex, 1);
      if (this.displayAddBtn == false) {
        this.displayAddBtn = true;
      }
    },
  },
  created() {
    //投稿の本文に親コンポーネントから渡されたデータを設定
    this.userName = this.postList.name;
    this.homete = this.postList.contents;

    if (this.postList.icon.facialHair != null) {
      this.fhp = 100;
    }
    if (this.postList.icon.accessories != null) {
      this.ap = 100;
    }
    this.avatorSvg = createAvatar(style, {
      head: [this.postList.icon.head],
      face: [this.postList.icon.face],
      facialHair: [this.postList.icon.facial_hair],
      facialHairProbability: this.fhp,
      maskProbability: 0,
      accessories: [this.postList.icon.accessories],
      accessoriesProbability: this.ap,
      skinColor: [this.postList.icon.skin_color],
      clothingColor: [this.postList.icon.clothing_color],
      hairColor: [this.postList.icon.hair_color],
    });

    this.postTime = this.postList.created_at.slice(0, 10).replace(/-/g, "/");

    this.postList.post_reactions.forEach((reaction) => {
      if (!this.reactions.includes(reaction.reaction)) {
        if(reaction.reaction != null){
          this.reactions.push(reaction.reaction);
        }
      }
    });
  },
};
</script>
