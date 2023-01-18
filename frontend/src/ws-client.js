import { io } from "socket.io-client";

function ws_connect(vm) {
  const socket = io(process.env.VUE_APP_API_ENDPOINT, {
    withCredentials: true,
    transports: ["websocket"],
    cookie: true,
  });

  socket.on("connect", () => {
    console.log("connect");
    socket.emit("hello", "world");
  });

  socket.io.on("error", (error) => {
    console.log(error);
  });

  socket.on("new_posts", (data) => {
    let dataJson = JSON.parse(data);
    let posts = dataJson["posts"];

    Object.keys(posts).forEach((key) => {
      if (posts[key]["user_reaction"] == null) {
        posts[key]["user_reaction"] = [];
      }
    });

    let existsPosts = JSON.parse(
      JSON.stringify(vm.$store.getters.completedPost)
    );

    //投稿したモノが入っていた場合は削除して追加
    for (let i = 0; i < existsPosts.length; i++) {
      for (let j = 0; j < posts.length; j++) {
        if (posts[j].post_id == existsPosts[i].post_id) {
          posts.splice(j, 1);
          vm.$store.commit("deleteCompletedPost", existsPosts[i]);
        }
      }
    }

    if (posts.length > 0) {
      vm.$store.commit("setUpdatePosts", posts);

      vm.$store.dispatch("alertNewPost");
    }
  });
}

export default { ws_connect };
