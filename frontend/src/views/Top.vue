<template>
  <v-app>
    <v-overlay
      :value="isVisiblePostHomete"
      :dark="false"
      :light="true"
      :z-index="999"
    >
      <PostHomete />
    </v-overlay>
    <v-container fluid class="mainContainer mx-auto">
      <Alert />
      <v-row justify="center" class="mx-auto">
        <v-col class="ma-0 pa-0">
          <SideMenu class="leftMenuContent" v-on:logout="isLoginCheck" />
        </v-col>

        <v-divider vertical></v-divider>

        <v-col
          sm="8"
          md="8"
          class="subContainer virtualScrollBar"
          v-scroll="onScroll"
        >
          <DisplayHomete
            v-for="post in posts"
            :key="post.post_id"
            :postList="post"
          />
        </v-col>

        <v-divider vertical></v-divider>

        <v-col class="ma-0 pa-0"> </v-col>
      </v-row>
    </v-container>
    <div ref="observe_element"></div>
  </v-app>
</template>
<style>
.mainContainer {
  max-width: 1200px;
  width: 100%;
  height: 100%;
}
.subContainer {
  width: 100%;
}
.leftMenuContent {
  position: sticky;
  top: 0px;
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
import SideMenu from "../components/leftMenu/SideMenu.vue"
import DisplayHomete from "../components/mainMenu/DisplayHomete.vue";
import Alert from "../components/util/Alert.vue";
import PostHomete from "../components/util/PostHomete.vue";
import axios from "axios";

export default {
  name: "Top",
  computed: {
    isVisiblePostHomete() {
      return this.$store.getters.isVisiblePostHomete;
    },
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  data() {
    return {
      posts: [],
      scrolledBottom: false,
    };
  },
  components: {
    PostHomete,
    DisplayHomete,
    SideMenu,
    Alert,
  },
  methods: {
    isLoginCheck: function () {
      this.$store.dispatch("toFalseLogin");
      localStorage.clear("firstLogin");
      setTimeout(() => {
        this.$store.dispatch("alertLogout");
      }, 500);
    },
  },
  created() {
    if (this.$cookies.isKey("expire") == true) {
      this.$store.dispatch("toTrueLogin");
      if (!localStorage.getItem("firstLogin")) {
        setTimeout(() => {
          this.$store.dispatch("alertLogin");
        }, 1500);
      }
      localStorage.setItem("firstLogin", true);
    } else {
      this.$store.dispatch("toFalseLogin");
    }

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

    window.onload = () => {
      this.$store.dispatch("toFalseAlertPost");
      this.$store.dispatch("toInvisiblePostHomete");
    };
  },
};
</script>
