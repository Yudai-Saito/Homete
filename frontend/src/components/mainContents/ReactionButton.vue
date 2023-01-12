<template>
  <div id="reactionBtnDiv" class="ma-0 pa-0">
    <v-btn
      id="reactionBtn"
      class="grey--text text--darken-3 ma-0 pa-0"
      @click="count"
      elevation="0"
      small
      outlined
      v-if="!reactionFlag"
      :disabled="!logged && !isSample"
    >
      <div id="btnIcon" v-twemoji>{{ reactionIcon }}</div>
      <div v-if="!privateFlag" id="countNum">{{ reactionCount }}</div>
    </v-btn>
    <v-btn
      id="pushedBtn"
      class="grey--text text--darken-3 ma-0 pa-0"
      @click="count"
      elevation="0"
      small
      outlined
      v-else
      :disabled="!logged && !isSample"
    >
      <div id="btnIcon" v-twemoji>{{ reactionIcon }}</div>
      <div v-if="!privateFlag" id="countNum">{{ reactionCount }}</div>
    </v-btn>
  </div>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #reactionBtn {
    width: 45px !important;
  }
  #pushedBtn {
    width: 45px !important;
  }
  #btnIcon {
    width: 16px;
    height: 16px;
  }
  #countNum {
    font-size: 14px;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #reactionBtn {
    width: 35px !important;
    height: 20px;
  }
  #pushedBtn {
    width: 35px !important;
    height: 20px;
  }
  #btnIcon {
    width: 13px;
    height: 13px;
  }
  #countNum {
    font-size: 12px;
  }
}
#reactionBtnDiv {
  display: flex;
  justify-content: center;
}
#reactionBtn {
  background-color: rgba(207, 216, 220, 0.5);
  gap: 0;
  min-width: 0 !important;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
#reactionBtn.v-btn--outlined {
  border: thin solid transparent;
}
#pushedBtn {
  background-color: rgba(112, 119, 218, 0.5);
  min-width: 0 !important;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
#pushedBtn.v-btn--outlined {
  border: thin solid rgb(112, 119, 218);
}
#btnIcon {
  margin: 5px;
  padding: 0;
  font-size: 2px;
}
#btnIcon img.emoji {
  margin: 0;
  padding: 0;
}
#countNum {
  display: flex;
  flex-flow: column;
  margin: 0;
  padding: 0;
  margin-right: 5px;
  height: 20px;
  text-align: center;
  justify-content: center;
}
</style>

<script>
import axios from "axios";

import twemoji from "twemoji";

export default {
  name: "ReactionButton",
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
  },
  data() {
    return {
      //リアクションの押された数
      reactionCount: 1,
      //リアクションが押されているかどうか
      reactionFlag: true,
    };
  },
  props: [
    "default_reactions",
    "reactionIcon",
    "postReaction",
    "userReaction",
    "postId",
    "privateFlag",
    "isSample",
  ],
  //v-twemojiプロパティを追加
  directives: {
    twemoji: {
      inserted(el) {
        el.innerHTML = twemoji.parse(el.innerHTML, {
          folder: "svg",
          ext: ".svg",
          base: "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/",
        });
      },
    },
  },
  methods: {
    count: function () {
      //カウントダウン
      if (this.reactionFlag) {
        this.reactionCount -= 1;
        this.reactionFlag = false;
        //カウントが0になったリアクションに対して処理
        if (this.reactionCount <= 0) {
          //postReactionから削除
          var pVal = {
            reaction: this.reactionIcon,
            count: 1,
          };
          var pIndex = this.postReaction.indexOf(pVal);
          this.postReaction.splice(pIndex, 1);

          //userReactionから削除
          var uVal = this.reactionIcon;
          var uIndex = this.userReaction.indexOf(uVal);
          this.userReaction.splice(uIndex, 1);

          this.$emit("deleteReaction", this.reactionIcon);
        }

        axios.delete("/posts/reaction", {
          params: {
            post_id: this.postId,
            reaction: this.reactionIcon,
          },
          withCredentials: true,
        });
        //カウントアップ
      } else {
        this.reactionCount += 1;
        this.reactionFlag = true;

        axios.put(
          "/posts/reaction",
          {
            post_id: this.postId,
            reaction: this.reactionIcon,
          },
          {
            withCredentials: true,
          }
        );
      }
    },
  },
  mounted() {
    this.postReaction.forEach((item) => {
      if (item.reaction == this.reactionIcon) {
        if (item.count == null) {
          item.count = 1;
        }
        if (this.default_reactions.includes(item.reaction)) {
          this.reactionCount = item.count + 1;
        } else {
          this.reactionCount = item.count;
        }
      }
      //他のユーザーの投稿やログアウト時の投稿の表示の際にuserReactionにはnullが入るため、エラー回避をする
      if (this.userReaction !== null) {
        if (this.userReaction.includes(this.reactionIcon)) {
          this.reactionFlag = true;
        } else {
          this.reactionFlag = false;
        }
      } else {
        this.reactionFlag = false;
      }
    });
  },
};
</script>
