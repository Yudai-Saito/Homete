self.addEventListener("fetch", () => {});

//メッセージを受け取ったとき
self.addEventListener("message", function (event) {
  switch (event.data) {
    case "updateCache":
      event.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
          return cache.addAll(urlsToCache);
        })
      );
      break;
  }
});
