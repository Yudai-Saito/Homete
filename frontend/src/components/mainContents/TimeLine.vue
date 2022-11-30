<template>
  <v-col class="mainContents virtualScrollBar" cols="12">
    <DisplayPosts v-for="post in posts" :key="post.post_id" :postList="post" />
    <div ref="observe_element"></div>
  </v-col>
</template>

<style>
.mainContents {
  margin: 0 auto;
  margin-top: 10vh !important;
  margin-bottom: 30px !important;
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
      posts: [
        {
          contents: "ぺぺぽ",
          created_at: "2022-11-25 14:45:15.000000",
          icon: {
            accessories: "glasses4",
            clothing_color: "pink01",
            face: "contempt",
            facial_hair: "full",
            hair_color: "variant01",
            head: "turban",
            skin_color: "variant05",
          },
          name: "TEST_NAME",
          post_id: 5,
          post_reactions: [
            {
              count: null,
              reaction: null,
            },
          ],
          user_reaction: null,
        },
        {
          contents: "ああああ",
          created_at: "2022-11-25 14:45:05.000000",
          icon: {
            accessories: null,
            clothing_color: "orange01",
            face: "smileLOL",
            facial_hair: "moustache5",
            hair_color: "variant09",
            head: "flatTopLong",
            skin_color: "variant04",
          },
          name: "TEST_NAME",
          post_id: 4,
          post_reactions: [
            {
              count: null,
              reaction: null,
            },
          ],
          user_reaction: null,
        },
        {
          contents: "ぺぺぽ",
          created_at: "2022-11-25 14:43:14.000000",
          icon: {
            accessories: null,
            clothing_color: "red01",
            face: "contempt",
            facial_hair: "moustache1",
            hair_color: "variant04",
            head: "flatTopLong",
            skin_color: "variant04",
          },
          name: "TEST_NAME",
          post_id: 3,
          post_reactions: [
            {
              count: null,
              reaction: null,
            },
          ],
          user_reaction: null,
        },
        {
          contents: "ほげらん",
          created_at: "2022-11-25 14:43:04.000000",
          icon: {
            accessories: null,
            clothing_color: "red01",
            face: "smileLOL",
            facial_hair: null,
            hair_color: "variant06",
            head: "dreads1",
            skin_color: "variant01",
          },
          name: "TEST_NAME",
          post_id: 2,
          post_reactions: [
            {
              count: null,
              reaction: null,
            },
          ],
          user_reaction: null,
        },
        {
          contents: "ほげ",
          created_at: "2022-11-25 14:42:55.000000",
          icon: {
            accessories: null,
            clothing_color: "lue01",
            face: "suspicious",
            facial_hair: null,
            hair_color: "variant08",
            head: "buns",
            skin_color: "variant02",
          },
          name: "TEST_NAME",
          post_id: 1,
          post_reactions: [
            {
              count: null,
              reaction: null,
            },
          ],
          user_reaction: null,
        },
      ],
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
