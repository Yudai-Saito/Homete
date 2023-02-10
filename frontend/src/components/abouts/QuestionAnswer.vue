<template>
  <div class="aboutContainer">
    <div class="aboutGroupTitle">
      <div v-twemoji style="width: 20px; margin-right: 5px; margin-top: 12px">
        💡
      </div>
      <h3 v-twemoji class="aboutTitleTxt" style="margin: 10px">よくある質問</h3>
    </div>
    <v-divider style="margin: 10px" />
    <v-expansion-panels style="margin-bottom: 20px" accordion popout flat>
      <v-expansion-panel v-for="item in items" :key="item.id">
        <v-expansion-panel-header>{{ item.question }}</v-expansion-panel-header>
        <v-expansion-panel-content
          ><p style="white-space: pre-wrap" v-text="item.answer"></p
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
  font-size: 0.95rem;
}
.v-expansion-panel-content {
  border-top: solid thin rgba(0, 0, 0, 0.2);
  width: 85%;
  margin: 0 0 auto 12px;
}
.v-expansion-panel-content__wrap {
  padding: 8px 0 8px 12px;
}
</style>

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
  data() {
    return {
      items: [
        {
          id: 1,
          question: "HOMETEでできることは？",
          answer: "",
        },
        {
          id: 2,
          question: "どうしてHOMETEは生まれたの？",
          answer: `日常を誰かが見てくれて、肯定してくれて、明日も頑張ろうって思える。
そんな優しい世界を実現するために生まれました!`,
        },
        {
          id: 3,
          question: "本当に匿名なの？",
          answer: `誰かがあなたを特定することはできません!
投稿ごとにランダムなアイコンと名前が設定されるため完全匿名です!`,
        },
        {
          id: 4,
          question: "アカウント作成やログインは簡単なの？",
          answer: `Googleアカウントがあれば誰でも使えます!
面倒くさい登録はありません!`,
        },
        {
          id: 5,
          question: "不適切な投稿があったらどうなるの？",
          answer: `投稿は運営が監視しています!
不適切な投稿を発見したら削除していきます!`,
        },
        {
          id: 6,
          question: "無料で使えるの？",
          answer: `無料です!
サービス運営のために広告をつけさせてもらってます!`,
        },
        {
          id: 7,
          question: "経験値ってどうやって貯めるの？",
          answer: `投稿をしたり、リアクションを付けると経験値を獲得できます!
1日の最大獲得数は1000EXPです!`,
        },
        {
          id: 8,
          question: "経験値は何に使うの？",
          answer: `アイコンやコメント返信機能を買うことができます!
これから新しいスタンプも追加していく予定です!`,
        },
      ],
    };
  },
};
</script>
