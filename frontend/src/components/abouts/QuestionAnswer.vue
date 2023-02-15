<template>
  <div class="aboutContainer">
    <div class="aboutGroupTitle">
      <div v-twemoji class="aboutGroupTitleIcon">💡</div>
      <h3 v-twemoji class="aboutTitleTxt" style="margin: 10px">よくある質問</h3>
    </div>
    <v-divider style="margin: 10px" />
    <v-expansion-panels style="margin-bottom: 20px" accordion popout flat>
      <v-expansion-panel v-for="item in items" :key="item.id">
        <v-expansion-panel-header>{{ item.question }}</v-expansion-panel-header>
        <v-expansion-panel-content
          ><p
            style="white-space: pre-wrap; margin: 16px 0"
            v-text="item.answer"
          ></p
        ></v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<style>
.v-expansion-panels {
  border-radius: 10px;
}
.v-expansion-panel {
  border: solid thin rgba(0, 0, 0, 0.2);
}
.v-expansion-panel--active {
  border-radius: 20px !important;
}
.v-expansion-panel-header {
  font-weight: 500;
  font-size: 0.95rem !important;
}
.v-expansion-panel-content {
  border-top: solid thin rgba(0, 0, 0, 0.2);
  width: 90%;
  margin: 0 0 auto 12px;
}
.v-expansion-panel-content__wrap {
  padding: 0 0 12px 12px !important;
  flex: 1 1 auto !important;
  max-width: 100% !important;
}
</style>

<script>
import twemoji from "twemoji";
import { items } from "@/assets/faq.js";

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
  data() {
    return {
      items,
    };
  },
};
</script>
