<template>
  <v-col id="postContents" class="virtualScrollBar supportBreakPoint" cols="12">
    <div>
      <DisplayPosts
        v-for="post in posts"
        :key="post.post_id"
        :postList="post"
      />
    </div>
    <div ref="observe_element"></div>
  </v-col>
</template>

<style>
#postContents {
  margin: 0 auto !important;
  margin-top: 10vh !important;
  margin-bottom: 30px !important;
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
  },
  data() {
    return {
      posts: [],
    };
  },
  props: ["channel"],
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
      axios
        .get("/posts", { params: axios_params, withCredentials: true })
        .then((res) => {
          this.set_posts(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.get_posts({ channel: this.channel });
  },
  mounted() {
    this.observer = new IntersectionObserver((entries) => {
      const entry = entries[0];
      if (entry && entry.isIntersecting) {
        this.get_posts({
          created_at: this.posts[this.posts.length - 1].created_at,
          update: "old",
          channel: this.channel,
        });
      }
    });
    const observe_element = this.$refs.observe_element;
    this.observer.observe(observe_element);
  },
  watch: {
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
  },
};
</script>
