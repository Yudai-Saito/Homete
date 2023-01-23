<template>
  <v-col ref="dispPs" id="postContents" class="virtualScrollBar" cols="12">
    <div v-show="switchPosts" class="loader">
      <div class="loader-inner ball-pulse-sync">
        <div></div>
        <div></div>
        <div></div>
      </div>
    </div>
    <div>
      <DisplayPosts
        v-for="post in posts"
        :key="post.post_id"
        :postList="post"
      />
    </div>
    <div style="display: none" ref="observe_element"></div>
  </v-col>
</template>

<style>
#postContents {
  margin: 0 auto !important;
  margin-bottom: 20vh !important;
  padding: 0;
  width: 100%;
}
.virtualScrollBar {
  overflow: auto;
  /* IE, Edge 対応 */
  -ms-overflow-style: none;
  /* Firefox 対応 */
  scrollbar-width: none;
}
/* Chrome, Safari 対応 */
.virtualScrollBar::-webkit-scrollbar {
  display: none;
}

.loader {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.loader-inner {
  display: flex;
  justify-content: center;
  align-items: center;
}

@-webkit-keyframes ball-pulse-sync {
  33% {
    -webkit-transform: translateY(10px);
    transform: translateY(10px);
  }
  66% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
}

@keyframes ball-pulse-sync {
  33% {
    -webkit-transform: translateY(10px);
    transform: translateY(10px);
  }
  66% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
}

.ball-pulse-sync > div:nth-child(1) {
  -webkit-animation: ball-pulse-sync 0.6s -0.14s infinite ease-in-out;
  animation: ball-pulse-sync 0.6s -0.14s infinite ease-in-out;
}

.ball-pulse-sync > div:nth-child(2) {
  -webkit-animation: ball-pulse-sync 0.6s -0.07s infinite ease-in-out;
  animation: ball-pulse-sync 0.6s -0.07s infinite ease-in-out;
}

.ball-pulse-sync > div:nth-child(3) {
  -webkit-animation: ball-pulse-sync 0.6s 0s infinite ease-in-out;
  animation: ball-pulse-sync 0.6s 0s infinite ease-in-out;
}

.ball-pulse-sync > div {
  background-color: rgb(154, 159, 229);
  width: 25px;
  height: 25px;
  border-radius: 100%;
  margin: 0 5px;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  display: inline-block;
}
</style>

<script>
import DisplayPosts from "./DisplayPosts.vue";
import axios from "axios";

export default {
  name: "TimeLine",
  components: {
    DisplayPosts,
  },
  computed: {
    postsProcess: function () {
      return this.$store.getters.processFlag;
    },
    addUserUpdatePosts: function () {
      return this.$store.getters.userUpdatePosts;
    },
    newPosts: function () {
      return this.$store.getters.displayTopAlert;
    },
  },
  data() {
    return {
      scrollBottomHeight: 0,
      posts: [],
      postsLength: 0,
      switchPosts: false,
      isScrollBottom: false,
      isUnshifted: false,
      isPushed: false,
    };
  },
  props: ["channel", "updatePost"],
  methods: {
    replaceUserReactionNull: function (posts) {
      Object.keys(posts).forEach((key) => {
        if (posts[key]["user_reaction"] == null) {
          posts[key]["user_reaction"] = [];
        }
      });
      return posts;
    },
    set_posts: function (res) {
      var posts = res.data["posts"];

      if (posts.length != 0) {
        posts = this.replaceUserReactionNull(posts);

        if (this.posts.length == 0) {
          this.posts = posts;
        } else {
          posts.forEach((post) => {
            this.posts.push(post);
          });
        }
        this.postsLength = this.posts.length;
      }
    },
    get_posts: function (axios_params = {}) {
      this.switchPosts = true;
      axios
        .get("/posts", { params: axios_params, withCredentials: true })
        .then((res) => {
          this.switchPosts = false;
          this.set_posts(res);
        })
        .catch((err) => {
          this.switchPosts = false;
          console.log(err);
        });
    },
  },
  created() {
    //投稿管理系ステートを全てリセットかける
    this.$store.commit("deleteCompletedPost");
    this.$store.commit("deleteUserUpdatePosts");
    this.$store.commit("deleteUpdatePosts");

    this.get_posts({ channel: this.channel });
    this.postsLength = this.posts.length;
  },
  mounted() {
    this.observer = new IntersectionObserver((entries) => {
      this.$refs.observe_element.style.display = `none`;
      this.isScrollBottom = true;
      const entry = entries[0];
      if (entry && entry.isIntersecting) {
        this.get_posts({
          created_at: this.posts[this.posts.length - 1].created_at,
          update: "old",
          channel: this.channel,
        });
        this.isPushed = true;
      }

      this.isScrollBottom = false;
      this.$refs.observe_element.style.display = `block`;
    });
    const observe_element = this.$refs.observe_element;
    this.observer.observe(observe_element);
  },
  watch: {
    scrollBottomHeight: function (newHeight, oldHeight) {
      if (oldHeight != 0 && this.isPushed == false) {
        var beforeViewHeight = newHeight - oldHeight + window.scrollY;
        console.log("result:", beforeViewHeight);
        console.log("new:", newHeight);
        console.log("old:", oldHeight);
        console.log("postHeight:", newHeight - oldHeight);
        console.log("currentScroll:", window.scrollY);
        window.scrollTo(0, beforeViewHeight);
        this.isUnshifted = false;
      } else {
        this.isPushed = false;
      }
    },
    postsProcess(newProcessFlag) {
      if (this.$store.getters.postsProcess == "delete") {
        if (newProcessFlag === true) {
          // ポスト配列内で、IDがdeletePostIdと一致するものを探し、
          // その位置を検出する
          const index = this.posts.findIndex(
            (post) => post.post_id === this.$store.getters.postId
          );

          // 存在した場合は、その位置から1つの要素を配列から削除する
          if (index !== -1) {
            this.posts.splice(index, 1);
          }
        }
      }
      this.$store.commit("updateProcess", false, "");
    },
    updatePost(newPost) {
      const index = this.posts.findIndex(
        (post) => post.post_id === newPost.post_id
      );
      // 存在した場合は、その位置から1つの要素を配列から削除する
      if (index !== -1) {
        this.$set(this.posts, index, newPost);

        this.postsLength = this.posts.length;
      }
    },
    //投稿完了時の追記
    addUserUpdatePosts(userUpdatePosts) {
      userUpdatePosts = this.replaceUserReactionNull(userUpdatePosts);

      //userUpdatePostsを空にするので動作しないように1以上のときに動くようにする
      if (userUpdatePosts.length > 0) {
        for (let i; i < userUpdatePosts.length; i++) {
          for (let j; j < userUpdatePosts.length; j++) {
            if (this.posts[j].post_id == userUpdatePosts[i].post_id) {
              userUpdatePosts.splice(j);
              break;
            }
            if (this.posts[j].post_id == userUpdatePosts[i].post_id) {
              break;
            }
          }
        }

        this.posts.unshift(...userUpdatePosts);

        this.postsLength = this.posts.length;
        this.isUnshifted = true;

        this.$store.commit("deleteUserUpdatePosts");
        this.$store.commit("updateTopAlert", false);
      }
    },
    //新規投稿通知ボタンを押して追記
    newPosts(newTopAlertState, oldTopAlertState) {
      if (newTopAlertState == false && oldTopAlertState == true) {
        var updatePosts = JSON.parse(
          JSON.stringify(this.$store.getters.updatePosts)
        );

        updatePosts = this.replaceUserReactionNull(updatePosts);

        this.posts.unshift(...updatePosts);

        this.postsLength = this.posts.length;
        this.isUnshifted = true;

        this.$store.commit("deleteUpdatePosts");
        this.$store.commit("updateTopAlert", false);
      }
    },
  },
  updated() {
    if (this.$refs.observe_element.style.display != `block`) {
      this.$refs.observe_element.style.display = `block`;
      this.scrollBottomHeight =
        this.$refs.dispPs.getBoundingClientRect().height;
    } else {
      this.scrollBottomHeight =
        this.$refs.dispPs.getBoundingClientRect().height;
    }
  },
};
</script>
