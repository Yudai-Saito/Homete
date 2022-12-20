<template>
  <twemoji-picker
    id="overridePicker"
    v-if="displayTwemojiPicker"
    v-click-outside="closePicker"
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
</template>

<style>
#overridePicker {
  position: fixed;
  inset: 0;
  width: 520px;
  height: 400px;
  z-index: 999;
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
#emoji-container #emoji-popup #emoji-popover-search #search-header input {
  z-index: auto;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  div
  #popper-skins-container
  #popper-inner
  .emoji-popover-inner {
  height: 100% !important;
}
</style>

<script>
import axios from "axios";

import { TwemojiPicker } from "@kevinfaguiar/vue-twemoji-picker";
import EmojiAllData from "@/emoji/emoji-all-groups.json";
import EmojiGroups from "@/emoji/emoji-groups.json";

import ClickOutside from "vue-click-outside";

export default {
  name: "TwemojiPicker",
  components: {
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
    pickerX() {
      return this.$store.getters.pickerX;
    },
    pickerY() {
      return this.$store.getters.pickerY;
    },
    displayTwemojiPicker() {
      return this.$store.getters.displayTwemojiPicker;
    },
    emojiBtnClick() {
      return JSON.parse(JSON.stringify(this.$store.getters.emojiBtnClick));
    },
  },
  data() {
    return {
      x: 0,
      y: 0,
      reactions: null,
      postList: null,
      clickingOutSide: false,
    };
  },
  directives: {
    ClickOutside,
  },
  methods: {
    emojiAdded(emojiUnicode) {
      if (!this.reactions.includes(emojiUnicode)) {
        axios.put(
          "/posts/reaction",
          {
            post_id: this.postList.post_id,
            reaction: emojiUnicode,
          },
          {
            withCredentials: true,
          }
        );

        this.postList.user_reaction.push(emojiUnicode);
        this.postList.post_reactions.push({
          reaction: emojiUnicode,
          count: 1,
        });
        this.$emit("addReaction", this.postList);

        if (this.reactions.length >= 20) {
          this.$store.commit("updateDisplayAddBtn", false);
        }
      }
      this.closePicker();
    },
    closePicker() {
      if (this.clickingOutSide) {
        this.$store.commit("invisibleTwemojiPicker");
      } else {
        this.clickingOutSide = true;
      }
    },
    movePicker() {
      if (this.pickerX >= window.innerWidth / 2) {
        this.x = this.pickerX - 526;
      } else {
        this.x = this.pickerX + 33;
      }
      if (this.pickerY >= window.innerHeight - 410) {
        this.y = window.innerHeight - 410;
      } else {
        this.y = this.pickerY;
      }
    },
  },
  watch: {
    emojiBtnClick: {
      handler: function (newClick, oldClick) {
        this.clickingOutSide = false;
        if (newClick.currentPostId != null) {
          if (oldClick.currentPostId == null) {
            if (newClick.currentPostId != oldClick.currentPostId) {
              this.reactions = newClick.currentReactions;
              this.postList = newClick.currentPostList;
              this.movePicker();
              this.$store.commit("visibleTwemojiPicker");
            }
          } else if (newClick.currentPostId == oldClick.currentPostId) {
            this.$store.commit("invisibleTwemojiPicker");
          } else {
            this.reactions = newClick.currentReactions;
            this.postList = newClick.currentPostList;
            this.movePicker();
          }
        }
      },
      deep: true,
    },
  },
};
</script>
