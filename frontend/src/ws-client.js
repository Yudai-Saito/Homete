import { io } from "socket.io-client";

class WSService {
  socket = null;

  connect(vm) {
    this.socket = io(process.env.VUE_APP_API_ENDPOINT, {
      withCredentials: true,
      transports: ["websocket"],
      cookie: true,
    });

    this.socket.on("new_posts", (data) => {
      let dataJson = JSON.parse(data);
      let posts = dataJson["posts"];

      let existsPosts = JSON.parse(
        JSON.stringify(vm.$store.getters.completedPost)
      );

      //投稿したモノが入っていた場合は削除して追加
      for (let i = 0; i < existsPosts.length; i++) {
        for (let j = 0; j < posts.length; j++) {
          if (posts[j].post_id == existsPosts[i].post_id) {
            posts.splice(j, 1);
            vm.$store.commit("deleteIntexCompletedPost", existsPosts[i]);
          }
        }
      }

      if (posts.length > 0) {
        vm.$store.commit("setUpdatePosts", posts);

        if (vm.$store.getters.contentsKey == "timeline") {
          vm.$store.dispatch("alertNewPost");
        }
      }
    });
  }

  disconnect() {
    if (this.socket) {
      this.socket.close();
      this.socket = null;
    }
  }
}

const ws = new WSService();
export default ws;
