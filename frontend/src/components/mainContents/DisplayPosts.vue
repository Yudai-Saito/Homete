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
            z-index="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                style="bottom: 10px"
                icon
                plain
                :ripple="false"
                v-bind="attrs"
                v-on="on"
                :disabled="isSample"
              >
                <v-icon>mdi-dots-horizontal</v-icon>
              </v-btn>
            </template>
            <v-list class="ma-0 pa-0">
              <v-list-item class="ma-0 pa-0">
                <PostsMenu
                  labelTxt="削除"
                  :onClickPostsMenu="deletePost"
                  v-if="this.postList.user_post"
                />
                <PostsMenu
                  labelTxt="通報"
                  :onClickPostsMenu="reportPost"
                  v-else
                />
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-row>
      <v-divider id="divider" />
      <v-card-text
        id="cardMainText"
        class="black--text break-line"
        v-text="homete"
      ></v-card-text>
      <div id="btns">
        <v-card-actions id="reactionBtns">
          <div id="reactionsDiv" v-for="reaction in reactions" :key="reaction">
            <ReactionButton
              :default_reactions="default_reactions"
              :reactionIcon="reaction"
              :postReaction="postList.post_reactions"
              :userReaction="postList.user_reaction"
              :postId="postList.post_id"
              :privateFlag="postList.private"
              v-on:deleteReaction="deleteReactions"
              :isSample="isSample"
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
            :disabled="!logged && !isSample"
          >
            <div ref="addBtn">
              <v-icon>mdi-plus</v-icon>
            </div>
          </v-btn>
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
  #divider {
    margin: 0 auto;
  }
  #cardMainText {
    font-size: 16px;
    padding-top: 8px;
    margin: 0 auto;
    padding-left: 0px;
    padding-right: 0px;
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
    max-width: 550px;
  }
  #nameTxt {
    font-size: 22px;
    margin-top: 10px;
  }
  #timeTxt {
    font-size: 14px;
    margin-top: 20px;
  }
  #cardMainText {
    width: 75%;
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
  #divider {
    margin: 0 auto;
  }
  #cardMainText {
    font-size: 14px;
    padding: 8px;
    margin: 0 auto;
    padding-left: 0px;
    padding-right: 0px;
  }
  #cardTitle {
    padding-left: 0px;
    padding-bottom: 0px;
  }
  #circle {
    height: 40px;
    width: 40px;
  }
  #avater {
    height: 40px !important;
    width: 40px !important;
    min-width: 40px !important;
  }
  #postsCard {
    padding: 12px;
    max-width: 350px;
  }
  #nameTxt {
    font-size: 16px;
    margin-top: 8px;
  }
  #timeTxt {
    font-size: 10px;
    margin-top: 13px;
  }
  #btns {
    width: 70%;
    margin: 0 auto;
  }
  #cardMainText {
    width: 70%;
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

#postsCard {
  margin: 0;
  width: 100%;
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
#divider {
  width: 75%;
}
#cardMainText {
  line-height: 26px;
  z-index: auto;
}
</style>

<script scoped>
import PostsMenu from "./PostsMenu.vue";
import ReactionButton from "./ReactionButton.vue";
import VueResponsiveText from "vue-responsive-text";

import { createAvatar } from "@dicebear/avatars";
import * as style from "@dicebear/open-peeps";

export default {
  name: "DisplayPosts",
  components: {
    PostsMenu,
    ReactionButton,
    VueResponsiveText,
  },
  computed: {
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
      fhp: 0,
      ap: 0,
      displayAddBtn: true,
    };
  },
  props: ["postList", "isSample"],
  methods: {
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
    displayEmojiPicker() {
      var rect = this.$refs.addBtn.getBoundingClientRect();
      this.$store.dispatch("clickBtn", {
        x: rect.x,
        y: rect.y,
        reactions: this.reactions,
        postList: this.postList,
        postId: this.postList.post_id,
      });
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
  watch: {
    postList() {
      this.postList.post_reactions.forEach((reaction) => {
        if (!this.reactions.includes(reaction.reaction)) {
          if (reaction.reaction != null) {
            this.reactions.push(reaction.reaction);
            if (this.reactions.length >= 20) {
              this.displayAddBtn = false;
            }
          }
        }
      });
    },
  },
};
</script>
