import { io } from "socket.io-client";

function ws_connect() {
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
    // TODO - ここでupdate_postsに追加していく
    console.log(data);
  });
}

export default { ws_connect };
