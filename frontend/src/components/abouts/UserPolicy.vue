<template>
  <div class="aboutContainer">
    <div class="aboutGroupTitle">
      <div v-twemoji style="width: 20px; margin-right: 5px; margin-top: 12px">
        📑
      </div>
      <h3 v-twemoji class="aboutTitleTxt" style="margin: 10px">利用規約</h3>
    </div>
    <v-divider style="margin: 10px" />
    <div v-html="markedContent"></div>
  </div>
</template>

<script>
import twemoji from "twemoji";
import { marked } from "marked";
import policy from "@/assets/user-policy.md";
export default {
  name: "UserPolicy",
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
