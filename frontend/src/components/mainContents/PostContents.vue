<template>
  <v-col ref="dispPs" id="postContents" class="virtualScrollBar" cols="12">
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
  will-change: transform;
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
</style>

<script>
import DisplayPosts from "./DisplayPosts.vue";
import axios from "axios";

// $grid-breakpoints を JavaScript のオブジェクトとして取得
//const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

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
      posts: [],
      postsLength: 0,
      isFirstRendering: true,
      isLastRendering: false,
      isUnshifted: false,
      isPushed: false,
      scrollHeight: 0,
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
      axios
        .get("/posts", { params: axios_params, withCredentials: true })
        .then((res) => {
          this.set_posts(res);
          if (res.data.posts.length < 15) {
            //todo:ここに最後の投稿表示時に何か処理が書ける
            this.isLastRendering = true;
            this.$emit("switchingPosts", false);
            this.$refs.observe_element.style.display = `none`;
          } else {
            this.isPushed = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    //表示切替で新しく投稿を受信するためアラートは削除
    this.$store.commit("updateTopAlert", false);

    this.get_posts({ channel: this.channel });
    this.postsLength = this.posts.length;
  },
  mounted() {
    this.observer = new IntersectionObserver((entries) => {
      if (this.isFirstRendering == true) {
        this.isFirstRendering = false;
        this.isPushed = false;
        this.$refs.observe_element.style.display = `block`;
        this.$emit("switchingPosts", false);
      } else if (this.isLastRendering == false) {
        if (this.isPushed == false) {
          this.$refs.observe_element.style.display = `none`;
          this.$emit("switchingPosts", true);
          this.isPushed = true;
          const entry = entries[0];
          if (entry && entry.isIntersecting) {
            this.get_posts({
              created_at: this.posts[this.posts.length - 1].created_at,
              update: "old",
              channel: this.channel,
            });
          }
        }
      }
    });
    const observe_element = this.$refs.observe_element;
    this.observer.observe(observe_element);
  },
  watch: {
    scrollHeight(newHeight, oldHeight) {
      if (oldHeight != 0 && this.isUnshifted == true) {
        var newPostHeight = newHeight - oldHeight;
        var scrollToHeight = newPostHeight + window.scrollY;

        console.log("bs:", window.scrollY);
        window.scrollTo(0, scrollToHeight);
        console.log("as:", window.scrollY);

        console.log("newH:", newHeight);
        console.log("oldH:", oldHeight);
        console.log("newPostH:", newPostHeight);
        console.log("scrollToH:", scrollToHeight);
        this.isUnshifted = false;
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
      let updatePosts = JSON.parse(JSON.stringify(userUpdatePosts));

      updatePosts = this.replaceUserReactionNull(updatePosts);

      //userUpdatePostsを空にするので動作しないように1以上のときに動くようにする
      if (updatePosts.length > 0) {
        for (let i; i < updatePosts.length; i++) {
          for (let j; j < updatePosts.length; j++) {
            if (this.posts[j].post_id == updatePosts[i].post_id) {
              updatePosts.splice(j);
              break;
            }
            if (this.posts[j].post_id == updatePosts[i].post_id) {
              break;
            }
          }
        }

        this.posts.unshift(...updatePosts);
        this.isUnshifted = true;

        this.postsLength = this.posts.length;

        this.$store.commit("deleteUserUpdatePosts");
        this.$store.commit("deleteUpdatePosts");
        this.$store.commit("updateTopAlert", false);
      }
    },
    //新規投稿通知ボタンを押して追記
    newPosts(newTopAlertState, oldTopAlertState) {
      if (newTopAlertState == false && oldTopAlertState == true) {
        let updatePosts = JSON.parse(
          JSON.stringify(this.$store.getters.updatePosts)
        );

        updatePosts = this.replaceUserReactionNull(updatePosts);

        this.posts.unshift(...updatePosts);
        this.isUnshifted = true;

        this.postsLength = this.posts.length;

        this.$store.commit("deleteUpdatePosts");
        this.$store.commit("updateTopAlert", false);
      }
    },
  },
  updated() {
    if (this.isUnshifted == true || this.isPushed == true) {
      this.scrollHeight = this.$refs.dispPs.getBoundingClientRect().height;
    }
    if (this.isPushed == true) {
      this.$emit("switchingPosts", false);
      setTimeout(() => {
        this.isPushed = false;
        this.$refs.observe_element.style.display = `block`;
      }, "1000");
    }
  },
};
</script>
