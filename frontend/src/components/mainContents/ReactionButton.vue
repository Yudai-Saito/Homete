<template>
  <div class="ma-0 pa-0 reactionBtnDiv">
    <v-btn
      class="grey--text text--darken-3 reactionBtn ma-0 pa-0"
      @click="count"
      elevation="0"
      small
      outlined
      v-if="!reactionFlag"
      :disabled="!logged"
    >
      <div class="btnIcon" v-twemoji>{{ reactionIcon }}</div>
      <div class="countNum">{{ reactionCount }}</div>
    </v-btn>
    <v-btn
      class="grey--text text--darken-3 pushedBtn ma-0 pa-0"
      @click="count"
      elevation="0"
      small
      outlined
      v-else
      :disabled="!logged"
    >
      <div class="btnIcon" v-twemoji>{{ reactionIcon }}</div>
      <div class="countNum">{{ reactionCount }}</div>
    </v-btn>
  </div>
</template>
<style>
.reactionBtnDiv {
  display: flex;
  justify-content: center;
}
.reactionBtn {
  background-color: rgba(207, 216, 220, 0.5);
  gap: 0;
  height: 24px !important;
  width: 45px !important;
  min-width: 0 !important;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
.reactionBtn.v-btn--outlined {
  border: thin solid transparent;
}
.pushedBtn {
  background-color: rgba(112, 119, 218, 0.5);
  height: 24px !important;
  width: 45px !important;
  min-width: 0 !important;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
.pushedBtn.v-btn--outlined {
  border: thin solid rgb(112, 119, 218);
}
.btnIcon {
  margin: 5px;
  padding: 0;
  width: 16px;
  height: 16px;
  font-size: 2px;
}
.btnIcon img.emoji {
  margin: 0;
  padding: 0;
}
.countNum {
  display: flex;
  flex-flow: column;
  margin: 0;
  padding: 0;
  margin-right: 5px;
  height: 20px;
  text-align: center;
  justify-content: center;
  font-size: 14px;
}
</style>

<script>
import axios from "axios";

import twemoji from "twemoji";

export default {
  name: "ReactionButton",
  //v-twemojiプロパティを追加
  directives: {
    twemoji: {
      inserted(el) {
        el.innerHTML = twemoji.parse(el.innerHTML, {
          folder: "svg",
          ext: ".svg",
        });
      },
    },
  },
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
  props: ["reactionIcon", "postReaction", "userReaction", "postId"],
  methods: {
    count: function () {
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

        axios.post(
          "/post/reaction",
          {
            post_id: this.postId,
            reaction: this.reactionIcon,
          },
          {
            withCredentials: true,
          }
        );
      } else {
        this.reactionCount += 1;
        this.reactionFlag = true;

        axios.put(
          "/post/reaction",
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
        this.reactionCount = item.count;
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
