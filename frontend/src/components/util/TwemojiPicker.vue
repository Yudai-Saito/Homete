<template>
  <twemoji-picker
    id="overridePicker"
    :style="{ transform: `translate(${x}px, ${y}px)` }"
    :emojiPickerDisabled="false"
    :emojiData="emojiDataAll"
    :emojiGroups="emojiGroups"
    :skinsSelection="false"
    :searchEmojisFeat="true"
    :pickerWidth="520"
    :pickerHeight="400"
    :recentEmojisFeat="true"
    :recentEmojiLimit="100"
    :randomEmojiArray="['']"
    :pickerAutoFlip="false"
    :pickerCloseOnClickaway="false"
    twemojiPath="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/"
    recentEmojisStorage="local"
    searchEmojiPlaceholder="絵文字を検索"
    searchEmojiNotFound="絵文字が見つかりませんでした😭"
    isLoadingLabel="検索中...🔍"
    @emojiUnicodeAdded="emojiAdded"
  ></twemoji-picker>
</template>

<style lang="scss">
@media (max-width: 400px) {
  #overridePicker
    div
    #popper-container
    #popper-inner
    #emoji-container
    #emoji-popup
    #emoji-popover-header {
    margin: 0 2% !important;
  }
}
@media (min-width: map-get($grid-breakpoints, md)) {
  // md 以上のブレークポイントでのスタイル定義
  #overridePicker {
    position: fixed;
    width: 520px;
  }
  #overridePicker div #popper-container {
    position: fixed !important;
    width: 520px;
    border-radius: 10px;
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
  }
}
@media (max-width: map-get($grid-breakpoints, md)) {
  // md 以下のブレークポイントでのスタイル定義
  #overridePicker {
    transform: none !important;
    position: relative;
    width: 100%;
    padding: 0 !important;
    border: solid rgba(0, 0, 0, 0.25) 1px !important;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  #overridePicker div #popper-container {
    position: relative !important;
    width: 100%;
    overflow: visible !important;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  #overridePicker
    div
    #popper-container
    #popper-inner
    #emoji-container
    #emoji-popup {
    width: 100% !important;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  #overridePicker
    div
    #popper-container
    #popper-inner
    #emoji-container
    #emoji-popup
    #emoji-popover-header {
    height: 33px;
    display: flex;
    justify-content: space-between;
    padding: 0;
    overflow-x: hidden;
    margin: 0 5%;
  }
  #overridePicker
    div
    #popper-container
    #popper-inner
    #emoji-container
    #emoji-popup
    #emoji-popover-header
    .emoji-tab {
    padding: 0;
    margin: 0 3px;
    height: 100%;
    border-bottom: solid 5px transparent;
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
    width: 100%;
    height: 100%;
    margin-bottom: 5px;
    min-width: 21px;
    min-height: 21px;
  }
  #overridePicker
    div
    #popper-container
    #popper-inner
    #emoji-container
    #emoji-popup
    .emoji-popover-inner {
    height: 330px !important;
  }
}
#overridePicker {
  inset: 0;
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
  transform: none !important;
  inset: 0 !important;
  -webkit-animation: none !important;
  animation: none !important;
  display: block;
  height: 400px;
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
  .emoji-popover-inner {
  width: 100% !important;
  border-top: solid #cfd8dc 1px;
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
  margin: 0 5% !important;
  padding: 0;
  display: flex;
  flex-flow: wrap;
  justify-content: flex-start;
  margin-bottom: 10% !important;
}
#overridePicker
  div
  #popper-container
  #popper-inner
  #emoji-container
  #emoji-popup
  .emoji-popover-inner
  div
  .emoji-list
  span {
  width: min-content;
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
    clickOutSide() {
      return this.$store.getters.clickOutSide;
    },
    emojiBtnClick() {
      return JSON.parse(JSON.stringify(this.$store.getters.emojiBtnClick));
    },
  },
  data() {
    return {
      x: 0,
      y: 0,
      reactions: [],
      postList: {},
    };
  },
  methods: {
    emojiAdded(emojiUnicode) {
      if (!JSON.parse(JSON.stringify(this.reactions)).includes(emojiUnicode)) {
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
      if (this.clickOutSide) {
        this.$store.commit("invisibleTwemojiPicker");
      } else {
        this.$store.commit("clickingOutSide", true);
      }
    },
    movePicker() {
      //呼び出し元の+ボタンが画面の右半分にある時はピッカーを左に
      if (this.pickerX >= window.innerWidth / 2) {
        this.x = this.pickerX - 526;
      }
      //画面左半分の時はピッカーを右に配置
      else {
        this.x = this.pickerX + 33;
      }
      //呼び出し元の+ボタンが画面のピッカーの高さ未満の場所の時、ピッカーの高さ分確保
      if (this.pickerY >= window.innerHeight - 410) {
        this.y = window.innerHeight - 410;
      } else {
        this.y = this.pickerY;
      }
    },
  },
  created() {
    this.movePicker();
  },
  watch: {
    emojiBtnClick: {
      handler: function (newClick, oldClick) {
        this.$store.commit("clickingOutSide", false);
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
