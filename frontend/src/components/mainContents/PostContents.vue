<template>
  <v-col
    ref="dispPs"
    id="postContents"
    class="virtualScrollBar supportBreakPoint"
    cols="12"
  >
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
  background-color: slategrey;
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
    deletePostId: function () {
      return this.$store.getters.deletePostId;
    },
    deletePostFlag: function () {
      return this.$store.getters.deletePostFlag;
    },
    addUserUpdatePosts: function () {
      return this.$store.getters.userUpdatePosts;
    },
  },
  data() {
    return {
      scrollBottomHeight: 0,
      posts: [],
      switchPosts: false,
      isScrollBottom: false,
    };
  },
  props: ["channel", "updatePost"],
  methods: {
    set_posts: function (res) {
      var posts = res.data["posts"];

      if (posts.length != 0) {
        Object.keys(posts).forEach((key) => {
          if (posts[key]["user_reaction"] == null) {
            posts[key]["user_reaction"] = [];
          }
        });

        if (this.posts.length == 0) {
          this.posts = posts;
        } else {
          posts.forEach((post) => {
            this.posts.push(post);
          });
        }
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
    this.get_posts({ channel: this.channel });
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
      }

      this.isScrollBottom = false;
      this.$refs.observe_element.style.display = `block`;
    });
    const observe_element = this.$refs.observe_element;
    this.observer.observe(observe_element);
  },
  watch: {
    posts(newPosts, oldPosts) {
      if (oldPosts != null) {
        var h = this.$refs.dispPs.getBoundingClientRect();
        this.scrollBottomHeight = h;
      }
      if (
        newPosts != null &&
        this.$refs.observe_element.style.display != `block`
      ) {
        this.$refs.observe_element.style.display = `block`;
      }
    },
    scrollBottomHeight: function (newHeight, oldHeight) {
      if (this.isScrollBottom == false) {
        var beforeViewHeight =
          newHeight.height - oldHeight.height + window.scrollY;
        scrollTo(0, beforeViewHeight);
        console.log(beforeViewHeight);
      }
    },
    deletePostFlag(newDeletePostFlag) {
      if (newDeletePostFlag === true) {
        // ポスト配列内で、IDがdeletePostIdと一致するものを探し、
        // その位置を検出する
        const index = this.posts.findIndex(
          (post) => post.post_id === this.deletePostId
        );

        // 存在した場合は、その位置から1つの要素を配列から削除する
        if (index !== -1) {
          this.posts.splice(index, 1);
        }

        this.$store.commit("updateDeletePostFlag", false);
      }
    },
    addUserUpdatePosts(userUpdatePosts) {
      //userUpdatePostsを空にするので動作しなように1以上のときに動くようにする
      if (userUpdatePosts.length > 0) {
        for (let i; i < userUpdatePosts.length; i++) {
          for (let j; j < userUpdatePosts.length; j++) {
            if (this.posts[j].post_id == userUpdatePosts[i].post_id) {
              console.log();
              userUpdatePosts.splice(j);
              break;
            }
            if (this.posts[j].post_id == userUpdatePosts[i].post_id) {
              break;
            }
          }
        }

        this.posts.unshift(...userUpdatePosts);

        this.$store.commit("deleteUserUpdatePosts");
      }
    },
    updatePost(newPost) {
      const index = this.posts.findIndex(
        (post) => post.post_id === newPost.post_id
      );
      // 存在した場合は、その位置から1つの要素を配列から削除する
      if (index !== -1) {
        this.$set(this.posts, index, newPost);
      }
    },
  },
};
</script>
