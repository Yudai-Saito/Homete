import { io } from "socket.io-client";

function ws_connect() {
  const socket = io(process.env.VUE_APP_API_ENDPOINT, {
    withCredentials: true,
  });

  socket.on("connect", () => {
    console.log("connect");
    socket.emit("hello", "world");
  });

  socket.io.on("error", (error) => {
    console.log(error);
  });

  socket.on("hello", (data) => {
    console.log(data);
  });
}

export default { ws_connect };
