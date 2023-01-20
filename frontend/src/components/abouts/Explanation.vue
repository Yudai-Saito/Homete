<template>
  <div class="aboutContainer">
    <div class="aboutGroupTitle">
      <div v-twemoji style="width: 20px; margin-right: 5px; margin-top: 12px">
        🔰
      </div>
      <h3 v-twemoji class="aboutTitleTxt">HOMETEの使い方</h3>
    </div>
    <v-divider />
    <p class="aboutText">使い方の説明</p>
  </div>
</template>

<script>
import twemoji from "twemoji";
export default {
  name: "Explanation",
  directives: {
    twemoji: {
      inserted(el) {
        el.innerHTML = twemoji.parse(el.innerHTML, {
          folder: "svg",
          ext: ".svg",
          base: "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/",
        });
      },
    },
  },
};
</script>
