<template>
  <div class="aboutContainer">
    <div class="aboutGroupTitle">
      <div v-twemoji style="width: 20px; margin-right: 5px; margin-top: 12px">
        💡
      </div>
      <h3 v-twemoji class="aboutTitleTxt" style="margin: 10px">よくある質問</h3>
    </div>
    <v-divider style="margin: 10px" />
    <p class="aboutText">準備中...</p>
  </div>
</template>

<script>
import twemoji from "twemoji";
export default {
  name: "QuestionAnswer",
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
