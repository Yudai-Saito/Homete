<template>
  <div class="aboutContainer">
    <div class="aboutGroupTitle">
      <div v-twemoji style="width: 20px; margin-right: 5px; margin-top: 12px">
        🔒
      </div>
      <h3 v-twemoji class="aboutTitleTxt" style="margin: 10px">
        プライバシーポリシー
      </h3>
    </div>
    <v-divider style="margin: 10px" />
    <div id="ppContent" v-html="markedContent"></div>
  </div>
</template>

<style>
#ppContent h2 {
  font-size: 18px;
}
#ppContent p,
ol {
  font-size: 15px;
  margin-bottom: 20px;
  margin-top: 5px;
}
#ppContent ol li {
  margin-bottom: 10px;
}
</style>

<script>
import twemoji from "twemoji";
import { marked } from "marked";
import policy from "@/assets/privacy-policy.md";
export default {
  name: "PrivacyPolicy",
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
  computed: {
    source() {
      return policy;
    },
    markedContent() {
      return marked(this.source);
    },
  },
};
</script>
