<template>
  <v-container fluid>
    <v-card id="postsCard" class="rounded-xl" :elevation="3">
      <v-row id="cardTitle">
        <div id="circle">
          <v-avatar id="avater">
            <svg v-html="this.avatorSvg"></svg>
          </v-avatar>
        </div>
        <div id="nameTxt">
          <VueResponsiveText>
            {{ userName }}
          </VueResponsiveText>
        </div>
        <div id="timeTxt">{{ postTime }}</div>
        <div id="cardMenu">
          <v-menu
            top
            offset-y
            nudge-bottom="90px"
            transition="scale-transition"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn style="bottom: 10px" icon plain v-bind="attrs" v-on="on">
                <v-icon>smi-dots-horizontal</v-icon>
              </v-btn>
            </template>
            <v-list class="ma-0 pa-0">
              <v-list-item class="ma-0 pa-0">
                <PostsMenu
                  labelTxt="削除"
                  :onClick="deletePost"
                  v-if="this.postList.user_post"
                />
                <PostsMenu labelTxt="通報" :onClick="reportPost" v-else />
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-row>
      <v-divider />
      <v-card-text
        id="cardMainText"
        class="black--text break-line"
        v-text="homete"
      ></v-card-text>
      <div id="btns">
        <v-card-actions id="reactionBtns" v-click-outside="closePicker">
          <div id="reactionsDiv" v-for="reaction in reactions" :key="reaction">
            <ReactionButton
              :default_reactions="default_reactions"
              :reactionIcon="reaction"
              :postReaction="postList.post_reactions"
              :userReaction="postList.user_reaction"
              :postId="postList.post_id"
              :privateFlag="postList.private"
              v-on:deleteReaction="deleteReactions"
            />
          </div>
          <v-btn
            id="addReactionBtn"
            class="grey--text text--darken-3 pa-0"
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
<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #addReactionBtn {
    height: 28px !important;
    width: 28px;
    min-width: 28px !important;
  }
  #cardMainText {
    font-size: 16px;
    padding-top: 8px;
  }
  #cardTitle {
    padding-left: 12px;
    padding-bottom: 8px;
  }
  #circle {
    height: 50px;
    width: 50px;
  }
  #avater {
    height: 50px !important;
    width: 50px !important;
    min-width: 50px !important;
  }
  #postsCard {
    padding: 20px;
  }
  #nameTxt {
    font-size: 22px;
    margin-top: 10px;
  }
  #timeTxt {
    font-size: 14px;
    margin-top: 20px;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #addReactionBtn {
    height: 20px !important;
    width: 20px;
    min-width: 20px !important;
  }
  #addReactionBtn span div i {
    font-size: 20px !important;
  }
  #cardMainText {
    font-size: 14px;
    padding: 8px;
  }
  #cardTitle {
    padding-left: 0px;
    padding-bottom: 0px;
  }
  #circle {
    height: 30px;
    width: 30px;
  }
  #avater {
    height: 30px !important;
    width: 30px !important;
    min-width: 30px !important;
  }
  #postsCard {
    padding: 12px;
  }
  #nameTxt {
    font-size: 16px;
    margin-top: 5px;
  }
  #timeTxt {
    font-size: 10px;
    margin-top: 10px;
  }
}

@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.break-line {
  white-space: pre-wrap;
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

#postsCard {
  margin: 0;
  width: 100%;
  max-width: 550px;
  margin-left: auto;
  margin-right: auto;
  padding-bottom: 10px;
  z-index: auto !important;
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
}
#postsCard * {
  z-index: 99;
}
#btns {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
}
#reactionBtns {
  margin: 0;
  padding: 0;
  flex-wrap: wrap;
  z-index: auto;
}
#reactionsDiv {
  margin-bottom: 10px;
  margin-right: 10px;
  z-index: auto;
}
#reactionsDiv * {
  z-index: auto;
}
#addReactionBtn {
  background-color: rgba(144, 152, 156, 0.5);
  overflow: hidden;
  z-index: auto;
  margin-bottom: auto;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
#addReactionBtn * {
  z-index: auto;
}

#addReactionBtn.v-btn--outlined {
  border: thin solid transparent;
}
#cardTitle {
  margin: 0;
  padding: 0;
  justify-content: baseline;
  z-index: auto;
}
#circle {
  background: #cfd8dc;
  border-radius: 50%;
  overflow: hidden;
  z-index: auto;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
  display: flex;
  justify-content: flex-end;
}
#circle * {
  z-index: auto;
}
#nameTxt {
  font-weight: 600;
  padding: 0;
  margin-left: 10px;
  z-index: auto;
  position: relative;
}
#timeTxt {
  color: #6b7280;
  padding: 0;
  margin-left: 15px;
  z-index: auto;
  position: relative;
}
#cardMenu {
  margin: 0;
  padding: 0;
  margin-left: auto;
  z-index: auto;
}
#cardMenu * {
  z-index: auto;
}
#cardMainText {
  line-height: 26px;
  z-index: auto;
}
</style>

<script>
import axios from "axios";

import PostsMenu from "./PostsMenu.vue";
import ReactionButton from "./ReactionButton.vue";
import VueResponsiveText from "vue-responsive-text";

import { createAvatar } from "@dicebear/avatars";
import * as style from "@dicebear/open-peeps";

import { TwemojiPicker } from "@kevinfaguiar/vue-twemoji-picker";
import EmojiAllData from "@/emoji/emoji-all-groups.json";
import EmojiGroups from "@/emoji/emoji-groups.json";

import ClickOutside from "vue-click-outside";

export default {
  name: "DisplayPosts",
  components: {
    PostsMenu,
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
  data() {
    return {
      avatorSvg: "",
      userName: "",
      postTime: "",
      homete: "",
      default_reactions: ["👍", "👀", "💯", "🥰", "🎉"],
      reactions: [],
      x: 0,
      y: 0,
      displayPicker: false,
      displayAddBtn: true,
      fhp: 0,
      ap: 0,
    };
  },
  props: ["postList"],
  directives: {
    ClickOutside,
  },
  methods: {
    emojiAdded(emojiUnicode) {
      if (!this.reactions.includes(emojiUnicode)) {
        this.postList.user_reaction.push(emojiUnicode);
        this.postList.post_reactions.push({
          reaction: emojiUnicode,
          count: 1,
        });
        this.reactions.push(emojiUnicode);
      }

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
    deletePost() {
      this.$store.commit("setDeletePostId", this.postList.post_id);
      this.$store.dispatch("visibleDeletePostOverlay");
    },
    reportPost() {
      this.$store.dispatch("visibleReportPostOverlay");
    },
  },
  created() {
    //投稿の本文に親コンポーネントから渡されたデータを設定
    this.reactions = [...this.default_reactions];

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
        if (reaction.reaction != null) {
          this.reactions.push(reaction.reaction);
        }
      }
    });
  },
};
</script>
