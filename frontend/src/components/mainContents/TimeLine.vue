<template>
  <v-col
    class="mainContents virtualScrollBar"
    cols="6"
  >
    <DisplayPosts v-for="post in posts" :key="post.post_id" :postList="post" />
    <div ref="observe_element"></div>
  </v-col>
</template>

<style>
.mainContents {
  margin: 0;
  margin-top: 47px;
  margin-bottom: 20px;
  padding: 0;
  width: 550px;
  min-width: 550px;
  max-width: 550px;
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
  data() {
    return {
      posts: [],
      scrolledBottom: false,
    };
  },
  components: {
    DisplayPosts,
  },
  created() {
    axios
      .get("/post", {
        withCredentials: true,
      })
      .then((res) => {
        this.posts = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  mounted() {
    this.observer = new IntersectionObserver((entries) => {
      const entry = entries[0];
      if (entry && entry.isIntersecting) {
        axios
          .get(
            "/post",
            {
              params: {
                created_at: this.posts[this.posts.length - 1].created_at,
              },
            },
            {
              withCredentials: true,
            }
          )
          .then((res) => {
            //投稿の追記
            this.posts = this.posts.concat(res.data);
            this.scrolledBottom = false;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    });
    const observe_element = this.$refs.observe_element;
    this.observer.observe(observe_element);
  },
};
</script>
