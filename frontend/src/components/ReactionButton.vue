<template>
  <div class="btnDiv">
    <v-btn
      class="d-none d-sm-block grey--text text--darken-3 reactBtn"
      @click="count"
      elevation="0"
      small
      outlined
      v-if="!reactionFlag"
      :disabled="!isLogin"
    >
      <h2>{{ reactionIcon }}</h2>
      {{ reactionCount }}
    </v-btn>
    <v-btn
      class="d-none d-sm-block grey--text text--darken-3 pushedButton"
      @click="count"
      elevation="0"
      small
      outlined
      v-else
      :disabled="!isLogin"
    >
      <h2>{{ reactionIcon }}</h2>
      {{ reactionCount }}
    </v-btn>

    <v-btn
      class="d-block d-sm-none grey--text text--darken-3 reactBtn"
      @click="count"
      elevation="0"
      x-small
      outlined
      height="100%"
      width="40px"
      v-if="!reactionFlag"
      :disabled="!isLogin"
    >
      <h3>{{ reactionIcon }}</h3>
      {{ reactionCount }}
    </v-btn>
    <v-btn
      class="d-block d-sm-none grey--text text--darken-3 pushedButton"
      @click="count"
      elevation="0"
      x-small
      outlined
      height="100%"
      width="40px"
      v-else
      :disabled="!isLogin"
    >
      <h3>{{ reactionIcon }}</h3>
      {{ reactionCount }}
    </v-btn>
  </div>
</template>
<style>
.btnDiv {
  margin: 0;
  padding: 0;
  margin-right: 6px;
}
.reactBtn {
  background-color: rgba(207, 216, 220, 0.5);
}
.reactBtn.v-btn--outlined {
  border: thin solid transparent;
}
.pushedButton {
  background-color: rgba(112, 119, 218, 0.5);
}
.pushedButton.v-btn--outlined {
  border: thin solid rgb(112, 119, 218);
}
</style>

<script>
import axios from "axios";

export default {
  name: "ReactionButton",
  computed:{
    isLogin(){
      return this.$store.getters.isLogin;
    }
  },
  data() {
    return {
      reactionCount: 0,
      reactionFlag: false,
    };
  },
  props: [
    "reactionIcon",
    "postReaction",
    "userReaction",
    "postId",
  ],
  methods: {
    count: function () {
      if (this.reactionFlag) {
        this.reactionCount -= 1;
        this.reactionFlag = false;

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
        this.reactionCount = item.count - 0;
      }
      //他のユーザーの投稿やログアウト時の投稿の表示の際にuserReactionにはnullが入るため、エラー回避をする
      if (this.userReaction !== null) {
        if (this.userReaction.includes(this.reactionIcon)) {
          this.reactionFlag = true;
        }
      }
    });
  },
  updated() {
    if (this.isLogin() == false) {
      this.reactionFlag = false;
    }
  },
};
</script>
