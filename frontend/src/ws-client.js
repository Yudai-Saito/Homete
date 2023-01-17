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

    //投稿したモノが入っていた場合は削除して追加

    vm.$store.commit("setUpdatePosts", posts);

    vm.$store.dispatch("alertNewPost");
  });
}

export default { ws_connect };
