<template>
  <div id="artBoard" style="background-color: floralwhite">
    <div style="height: 100%; width: 100%; overflow: auto">
      <Login />
      <v-app-bar
        ref="lpHeader"
        id="lpHeader"
        elevation="0"
        flat
        fixed
        floating
        hide-on-scroll
        color="transparent"
      >
        <div id="lpTitle" class="text-h4 font-weight-bold" @click="toTop">
          homete…
        </div>
        <div id="lpBtns">
          <button id="lpBtnSignup" @click="login">Googleで登録する</button>
        </div>
      </v-app-bar>
      <div id="lpBoard">
        <div
          id="lpContent"
          class="amber lighten-4"
          style="
            display: flex;
            flex-flow: column;
            justify-content: center;
            align-items: center;
          "
        >
          <div
            v-text="lpTxt1"
            style="font-size: 40px; text-align: center; font-weight: 600"
          ></div>
          <img src="/assets/HOMETE_LP1.png" style="width: 40%" />
        </div>
      </div>

      <div id="lpBoard">
        <div
          id="lpContent"
          class="amber lighten-4"
          style="
            display: flex;
            flex-flow: column;
            justify-content: center;
            align-items: center;
          "
        >
          <div
            v-text="lpTxt2"
            style="font-size: 30px; text-align: center; font-weight: 600"
          ></div>
          <img src="/assets/HOMETE_LP2.png" style="width: 40%" />
          <div
            id="lpBubble"
            style="top: 25%; left: 10%"
            v-text="lpTxt2_1"
          ></div>
          <div
            id="lpBubble"
            style="top: 25%; right: 10%"
            v-text="lpTxt2_2"
          ></div>
          <div id="lpBubble" style="top: 50%; left: 4%" v-text="lpTxt2_3"></div>
          <div
            id="lpBubble"
            style="top: 50%; right: 4%"
            v-text="lpTxt2_4"
          ></div>
          <div
            id="lpBubble"
            style="top: 75%; left: 10%"
            v-text="lpTxt2_5"
          ></div>
          <div
            id="lpBubble"
            style="top: 75%; right: 10%"
            v-text="lpTxt2_6"
          ></div>
          <div style="top: 8%; right: 3%" id="lpSubTitle">SOCIAL</div>
        </div>
      </div>

      <div id="lpBoard">
        <div
          id="lpContent"
          class="amber lighten-4"
          style="
            display: flex;
            flex-flow: column;
            justify-content: center;
            align-items: center;
          "
        >
          <div
            v-text="lpTxt3"
            style="
              font-size: 30px;
              text-align: center;
              margin-bottom: 2%;
              margin-top: 3%;
              font-weight: 600;
            "
          ></div>
          <div
            style="
              display: flex;
              justify-content: space-around;
              align-items: center;
              margin: 0 auto;
              width: 80%;
            "
          >
            <div id="lpShape3">
              かわいい絵を描けた
              <img
                src="/assets/HOMETE_LP3.png"
                style="width: 100%; margin-top: 20px"
              />
            </div>
            <div id="lpShape3">
              ほしかったものが買えた
              <img
                src="/assets/HOMETE_LP4.png"
                style="width: 100%; margin-top: 20px"
              />
            </div>
            <div id="lpShape3">
              今日も自炊してえらい！
              <img
                src="/assets/HOMETE_LP5.png"
                style="width: 100%; margin-top: 20px"
              />
            </div>
          </div>
          <div style="top: 8%; left: 3%" id="lpSubTitle">WHEN TO USE</div>
        </div>
      </div>

      <div id="lpBoard">
        <div
          id="lpContent"
          class="amber lighten-4"
          style="display: flex; justify-content: center; align-items: center"
        >
          <v-col cols="6">
            <DisplayPosts
              id="lpPostSample"
              v-for="samplePost in samplePosts"
              :key="samplePost.post_id"
              :postList="samplePost"
              :isSample="true"
            />
          </v-col>
          <v-col cols="5" style="height: 100%">
            <PostForm
              id="lpPostFormSample"
              :sampleLabel="`いろんなことを投稿しよう！`"
            />
          </v-col>
          <div id="arrow_box1" v-text="h2uTxt1"></div>
          <div id="arrow_box2" v-text="h2uTxt2"></div>
          <div style="top: 8%; right: 3%" id="lpSubTitle">HOW TO USE</div>
        </div>
      </div>

      <div id="lpBoard">
        <div
          id="lpContent"
          class="amber lighten-4"
          style="display: flex; justify-content: center; align-items: center"
        >
          <div style="width: 50%; transform: scale(1.2)">
            <div
              v-text="lpTxt4"
              style="font-size: 30px; text-align: center; font-weight: 600"
              id="lpSpeechBubble"
            ></div>
          </div>
          <img src="/assets/HOMETE_LP6.png" style="width: 40%" />
          <div style="top: 8%; left: 3%" id="lpSubTitle">FRIENDRY</div>
        </div>
      </div>

      <div id="lpBoard">
        <div
          id="lpContent"
          class="amber lighten-4"
          style="display: flex; justify-content: center; align-items: center"
        >
          <img src="/assets/HOMETE_LP7.png" style="width: 50%" />
          <div style="width: 38%; font-size: 30px; font-weight: 600">
            <div>ちょっとの喜びを</div>
            <div style="transform: translateX(35%)">HOMETEと一緒に</div>
          </div>
          <button
            id="lpBtnSignup"
            style="
              position: absolute;
              right: 15%;
              bottom: 25%;
              transform: scale(1.5);
            "
            @click="login"
          >
            Googleで登録する
          </button>
        </div>
      </div>

      <v-footer id="lpFooter">
        <div id="lpFooterBtns">
          <v-btn
            id="lpFooterBtn"
            plain
            text
            :ripple="false"
            @click="toExplanation"
          >
            ご利用ガイド
          </v-btn>
          <v-btn
            id="lpFooterBtn"
            plain
            text
            :ripple="false"
            @click="toQuestionAnswer"
          >
            Q & A
          </v-btn>
          <v-btn
            id="lpFooterBtn"
            plain
            text
            :ripple="false"
            @click="toUserPolicy"
          >
            利用規約
          </v-btn>
          <v-btn
            id="lpFooterBtn"
            plain
            text
            :ripple="false"
            @click="toPrivacyPolicy"
          >
            プライバシーポリシー
          </v-btn>
        </div>
        <div>©2022 by HOMETE</div>
      </v-footer>
    </div>
  </div>
</template>

<style>
#lpHeader {
  z-index: 2;
  padding: 20px;
  transition: transform 0.5s;
}
#lpHeader .v-toolbar__content {
  height: 48px !important;
  width: 100%;
  justify-content: space-between;
}

#lpTitle {
  margin: 0;
  padding: 0;
  color: #494854;
}
#lpSubTitle {
  position: absolute;
  writing-mode: vertical-rl;
  border-left: black solid 5px;
  font-size: 40px;
  font-weight: 700;
}
#lpBtns {
  margin-left: auto;
}
#lpBtnSignup {
  font-size: 15px;
  color: floralwhite;
  border-radius: 28px;
  padding: 5px 15px;
  font-weight: 500;
  background-color: rgb(139 143 210);
  border: 3px solid rgb(139 143 210);
  transition: background-color 0.2s, color 0.2s;
}
#lpBtnSignup:hover {
  background-color: rgba(139, 143, 210, 0.25);
  color: #494854;
}

#lpBoard {
  display: flex;
  justify-content: center;
  width: 100vw;
  height: 100vh;
  min-width: 1114px;
}
#lpContent {
  position: relative;
  width: 90%;
  height: 90%;
  margin: auto 0;
  border-radius: 50px;
  padding: 5%;
}
#lpContent div {
  white-space: pre-line;
}

#lpPostSample {
  margin: 0;
  padding: 0;
  transform: scale(0.85);
  margin-left: 10%;
}
#lpPostFormSample {
  margin: 0 auto;
  padding: 0;
  width: 70%;
  top: 30%;
}
#lpPostFormSample #formArea .v-input {
  border-radius: 24px;
  height: 200px;
}
#lpPostFormSample #formArea .v-input .v-input__control .v-input__slot {
  height: 200px;
}
#lpPostFormSample
  #formArea
  .v-input
  .v-input__control
  .v-input__slot
  .v-text-field__slot
  #mdPostForm {
  height: 180px !important;
}
#lpShape3 {
  height: 60vh;
  width: 30%;
  border-radius: 30px;
  background-color: floralwhite;
  margin: 20px;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  font-size: 17px;
  font-weight: 500;
  text-align: center;
}

#lpBubble {
  position: absolute;
  background-color: floralwhite;
  padding: 25px;
  border-radius: 50%;
  height: 110px;
  width: 270px;
  display: flex;
  justify-content: center;
  flex-flow: column;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
}
#lpSpeechBubble {
  position: relative;
  padding: 25px;
  background-color: #f6b167;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  flex-flow: column;
  text-align: center;
  height: 200px;
  width: 400px;
  right: -10%;
  top: -75px;
  margin-left: auto;
  margin-right: 5%;
}
#lpSpeechBubble::before {
  content: "";
  position: absolute;
  display: block;
  border-radius: 50%;
  background-color: #f6b167;
  right: 5%;
  bottom: 5%;
  width: 45px;
  height: 45px;
}
#lpSpeechBubble::after {
  content: "";
  position: absolute;
  display: block;
  border-radius: 50%;
  background-color: #f6b167;
  right: 2%;
  bottom: 1%;
  width: 25px;
  height: 25px;
}
#arrow_box1 {
  position: absolute;
  width: 270px;
  height: 110px;
  background: floralwhite;
  text-align: center;
  border: 1px solid #f6b167;
  color: #000;
  font-size: 20px;
  font-weight: 500;
  border-radius: 22px;
  -webkit-border-radius: 22px;
  -moz-border-radius: 22px;
  display: flex;
  justify-content: center;
  flex-flow: column;
  top: 13%;
  right: 13%;
  -webkit-filter: drop-shadow(5px 5px 5px #7f483a);
  -moz-filter: drop-shadow(5px 5px 5px #7f483a);
  -ms-filter: drop-shadow(5px 5px 5px #7f483a);
  filter: drop-shadow(5px 5px 5px #7f483a);
}
#arrow_box1:after,
#arrow_box1:before {
  border: solid transparent;
  content: "";
  height: 0;
  width: 0;
  pointer-events: none;
  position: absolute;
  top: 100%;
  left: 71%;
}
#arrow_box1:after {
  border-color: rgba(0, 153, 255, 0);
  border-top-width: 19px;
  border-bottom-width: 19px;
  border-left-width: 15px;
  border-right-width: 15px;
  margin-left: -15px;
  border-top-color: floralwhite;
}
#arrow_box1:before {
  border-top-width: 20px;
  border-bottom-width: 20px;
  border-left-width: 16px;
  border-right-width: 16px;
  margin-left: -15.5px;
  border-top-color: #f6b167;
}

#arrow_box2 {
  position: absolute;
  width: 250px;
  height: 110px;
  background: floralwhite;
  text-align: center;
  border: 1px solid #f6b167;
  color: #000;
  font-size: 20px;
  font-weight: 500;
  border-radius: 22px;
  -webkit-border-radius: 22px;
  -moz-border-radius: 22px;
  display: flex;
  justify-content: center;
  flex-flow: column;
  top: 32%;
  right: 42%;
  -webkit-filter: drop-shadow(5px 5px 5px #7f483a);
  -moz-filter: drop-shadow(5px 5px 5px #7f483a);
  -ms-filter: drop-shadow(5px 5px 5px #7f483a);
  filter: drop-shadow(5px 5px 5px #7f483a);
}
#arrow_box2:after,
#arrow_box2:before {
  border: solid transparent;
  content: "";
  height: 0;
  width: 0;
  pointer-events: none;
  position: absolute;
  top: 0%;
  left: 98%;
  transform: rotate(12deg);
}
#arrow_box2:after {
  border-color: rgba(0, 153, 255, 0);
  margin-left: -256px;
  border-top-color: floralwhite;
  border-top-width: 20px;
  border-bottom-width: 10px;
  border-left-width: 14px;
  border-right-width: 10px;
}
#arrow_box2:before {
  border-top-width: 20px;
  border-bottom-width: 10px;
  border-left-width: 14px;
  border-right-width: 10px;
  margin-left: -258px;
  border-top-color: #f6b167;
  margin-top: -1px;
}

#lpFooter {
  flex-flow: column;
  height: 150px;
  background-color: transparent;
  justify-content: center;
  width: 100vw;
  min-width: 1114px;
}
#lpFooterBtns {
  display: flex;
  justify-content: space-around;
  width: 75%;
  margin: 20px 0;
}
#lpFooterBtn {
  width: 25%;
  font-size: 15px;
}
</style>


<script>
import DisplayPosts from "@/components/mainContents/DisplayPosts.vue";
import PostForm from "@/components/util/PostForm.vue";
import Login from "@/components/overlays/Login.vue";

export default {
  name: "LandingPage",
  components: {
    DisplayPosts,
    PostForm,
    Login,
  },
  data() {
    return {
      scrollY: 0,
      visibleStartY: 0,
      lpTxt1: `誰かにほめてもらえる優しいSNS`,
      lpTxt2: `こんなSNSあったらいいのにな`,
      lpTxt2_1: `ちょっとしたことでも
      ほめてもらいたい`,
      lpTxt2_2: `嫌な返信が来たら
      どうしよう`,
      lpTxt2_3: `自分の投稿だと
      知られたくない`,
      lpTxt2_4: `知らない人と
      繋がるのが怖い`,
      lpTxt2_5: `あまり知り合いに
      見られたくない`,
      lpTxt2_6: `もっと疲れない
      SNSがあったらいいのに`,
      lpTxt3: `こんなときにHOMETEは使えるよ`,
      lpTxt4: `匿名で投稿できて
      誰も傷つかない優しいSNS`,
      h2uTxt1: `ここにほめてもらいたい
      ことを書いて投稿しよう！`,
      h2uTxt2: `ログインしていれば
      誰でもリアクションが
      つけられるよ！`,

      samplePosts: [
        {
          contents: "いろんなリアクションをつけてみよう！",
          created_at: "",
          icon: {
            accessories: "glasses",
            clothing_color: "orange01",
            face: "driven",
            facial_hair: "chin",
            hair_color: "variant01",
            head: "grayMedium",
            skin_color: "variant01",
          },
          name: "ほめてもんすたー",
          post_id: 0,
          post_reactions: [
            {
              count: 11,
              reaction: "👍",
            },
            {
              count: 5,
              reaction: "👀",
            },
            {
              count: 10,
              reaction: "💯",
            },
            {
              count: 3,
              reaction: "🥰",
            },
            {
              count: 7,
              reaction: "🎉",
            },
          ],
          private: 0,
          user_post: 0,
          user_reaction: ["👍", "🥰"],
        },
        {
          contents: "投稿ごとに違ったアイコンと名前が自動で設定されるよ！",
          created_at: "",
          icon: {
            accessories: "glasses",
            clothing_color: "orange01",
            face: "driven",
            facial_hair: "chin",
            hair_color: "variant01",
            head: "grayMedium",
            skin_color: "variant01",
          },
          name: "ほめてもんすたー",
          post_id: 1,
          post_reactions: [
            {
              count: 11,
              reaction: "👍",
            },
            {
              count: 5,
              reaction: "👀",
            },
            {
              count: 10,
              reaction: "💯",
            },
            {
              count: 3,
              reaction: "🥰",
            },
            {
              count: 7,
              reaction: "🎉",
            },
          ],
          private: 0,
          user_post: 0,
          user_reaction: ["👍", "🥰"],
        },
        {
          contents: "あなたの日常を投稿しよう！",
          created_at: "",
          icon: {
            accessories: "glasses",
            clothing_color: "orange01",
            face: "driven",
            facial_hair: "chin",
            hair_color: "variant01",
            head: "grayMedium",
            skin_color: "variant01",
          },
          name: "ほめてもんすたー",
          post_id: 2,
          post_reactions: [
            {
              count: 11,
              reaction: "👍",
            },
            {
              count: 5,
              reaction: "👀",
            },
            {
              count: 10,
              reaction: "💯",
            },
            {
              count: 3,
              reaction: "🥰",
            },
            {
              count: 7,
              reaction: "🎉",
            },
          ],
          private: 0,
          user_post: 0,
          user_reaction: ["👍", "🥰"],
        },
      ],
    };
  },
  methods: {
    login: function () {
      this.$store.dispatch("visibleLoginOverlay");
    },
    toTop: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toTimeLine").then(() => {
        this.$router.push("/top");
      });
    },
    toExplanation: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toExplanation").then(() => {
        this.$router.push("/about");
      });
    },
    toQuestionAnswer: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toQuestionAnswer").then(() => {
        this.$router.push("/about");
      });
    },
    toUserPolicy: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toUserPolicy").then(() => {
        this.$router.push("/about");
      });
    },
    toPrivacyPolicy: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toPrivacyPolicy").then(() => {
        this.$router.push("/about");
      });
    },
  },
};
</script>
