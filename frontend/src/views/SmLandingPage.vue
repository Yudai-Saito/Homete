<template>
  <div id="artBoard" style="background-color: floralwhite">
    <Login />
    <v-app-bar
      ref="smLpHeader"
      id="smLpHeader"
      elevation="0"
      flat
      fixed
      floating
      color="transparent"
    >
      <div id="smLpTitle" class="text-h5 font-weight-bold" @click="toTop">
        homete…
      </div>
      <button id="smLpBtnSignup" @click="login">Googleで登録する</button>
    </v-app-bar>
    <div id="smLpBoard">
      <div
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
        "
      >
        <div
          v-text="smLpTxt1"
          style="font-size: 30px; text-align: center; font-weight: 600"
        ></div>
        <img src="/assets/HOMETE_LP1.png" style="width: 75%" />
      </div>
    </div>
    <div id="smLpBoard">
      <div
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
        "
      >
        <div
          v-text="smLpTxt2"
          style="
            font-size: 30px;
            text-align: center;
            font-weight: 600;
            margin-bottom: auto;
            margin-top: 5%;
          "
        ></div>
        <div
          id="smLpBubble"
          style="top: 19%; left: 20%"
          v-text="smLpTxt2_1"
        ></div>
        <div
          id="smLpBubble"
          style="top: 35%; right: 25%"
          v-text="smLpTxt2_2"
        ></div>
        <div
          id="smLpBubble"
          style="top: 52%; right: 23%"
          v-text="smLpTxt2_3"
        ></div>
        <div id="smLpSmallBubble"></div>
        <div id="smLpSmallBubble"></div>
        <img
          src="/assets/HOMETE_LP2.png"
          style="bottom: 3%; width: 75%; position: absolute; right: -5%"
        />
      </div>
    </div>
    <div id="smLpBoard">
      <div
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
        "
      >
        <div
          v-text="smLpTxt3"
          style="font-size: 30px; text-align: center; font-weight: 600"
        ></div>
        <div
          style="
            display: flex;
            justify-content: space-around;
            align-items: center;
          "
        >
          <v-carousel
            cycle
            interval="10000"
            height="400"
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item>
              <div id="smLpShape3">
                かわいい絵を描けた
                <img
                  src="/assets/HOMETE_LP3.png"
                  style="width: 60%; margin-top: 10px"
                />
              </div>
            </v-carousel-item>
            <v-carousel-item>
              <div id="smLpShape3">
                ほしかったものが買えた
                <img
                  src="/assets/HOMETE_LP4.png"
                  style="width: 60%; margin-top: 10px"
                />
              </div>
            </v-carousel-item>
            <v-carousel-item>
              <div id="smLpShape3">
                今日も自炊してえらい！
                <img
                  src="/assets/HOMETE_LP5.png"
                  style="width: 60%; margin-top: 10px"
                />
              </div>
            </v-carousel-item>
          </v-carousel>
        </div>
      </div>
    </div>
    <div id="smLpBoard">
      <div
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
        "
      >
        <DisplayPosts
          id="smLpPostSample"
          v-for="samplePost in samplePosts"
          :key="samplePost.post_id"
          :postList="samplePost"
          :isSample="true"
        />
      </div>
    </div>
    <div id="smLpBoard">
      <div
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
        "
      >
        <div
          v-text="smLpTxt4"
          style="font-size: 30px; text-align: center; font-weight: 600"
        ></div>
        <img src="/assets/HOMETE_LP6.png" style="width: 60%" />
      </div>
    </div>
    <div id="smLpBoard">
      <div
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-items: center;
        "
      >
        <div
          style="
            width: 95%;
            font-size: 30px;
            text-align: center;
            font-weight: 600;
            transform: translateX(-50px);
          "
        >
          <div style="transform: translateX(45px)">ちょっとの喜びを</div>
          <div style="transform: translateX(85px)">HOMETEと一緒に</div>
        </div>
        <img src="/assets/HOMETE_LP7.png" style="width: 70%" />
        <button
          id="smLpBtnSignup"
          style="
            right: 3%;
            bottom: 20%;
            padding: 5px 15px;
            transform: scale(1.5) translateX(40px);
          "
          @click="login"
        >
          Googleで登録する
        </button>
      </div>
    </div>
    <v-footer id="smLpFooter">
      <div id="smLpFooterBtns">
        <v-btn
          id="smLpFooterBtn"
          plain
          text
          :ripple="false"
          @click="toExplanation"
        >
          ご利用ガイド
        </v-btn>
        <v-btn
          id="smLpFooterBtn"
          plain
          text
          :ripple="false"
          @click="toQuestionAnswer"
        >
          Q & A
        </v-btn>
        <v-btn
          id="smLpFooterBtn"
          plain
          text
          :ripple="false"
          @click="toUserPolicy"
        >
          利用規約
        </v-btn>
        <v-btn
          id="smLpFooterBtn"
          plain
          text
          :ripple="false"
          @click="toPrivacyPolicy"
        >
          プライバシーポリシー
        </v-btn>
      </div>
      <div style="font-size: 15px">©2022 by HOMETE</div>
    </v-footer>
  </div>
</template>

<style>
#smLpHeader {
  z-index: 2;
  padding: 20px;
  transition: transform 0.5s;
}
#smLpHeader .v-toolbar__content {
  height: 48px !important;
  width: 100%;
  justify-content: space-between;
}

#smLpTitle {
  margin: 0;
  padding: 0;
  color: #494854;
}
#smLpBtns {
  margin-left: auto;
}
#smLpBtnSignup {
  font-size: 15px;
  color: floralwhite;
  border-radius: 28px;
  padding: 5px 15px;
  font-weight: 500;
  background-color: rgb(139 143 210);
  border: 3px solid rgb(139 143 210);
  transition: background-color 0.2s, color 0.2s;
}
#smLpBtnSignup:hover {
  background-color: rgba(139, 143, 210, 0.25);
  color: #494854;
}

#smLpBoard {
  display: flex;
  justify-content: center;
  width: 100vw;
  height: 100vh;
}
#smLpContent {
  position: relative;
  width: 90%;
  height: 90%;
  margin: auto 0;
  border-radius: 50px;
  padding: 5%;
}
#smLpContent div {
  white-space: pre-line;
}

#smLpPostSample {
  margin: 0;
  padding: 0;
  transform: scale(0.9);
}
#smLpPostFormSample {
  margin: 0 auto;
  padding: 0;
  width: 70%;
  top: 30%;
}
#smLpPostFormSample #formArea .v-input {
  border-radius: 24px;
  height: 200px;
}
#smLpPostFormSample #formArea .v-input .v-input__control .v-input__slot {
  height: 200px;
}
#smLpPostFormSample
  #formArea
  .v-input
  .v-input__control
  .v-input__slot
  .v-text-field__slot
  #mdPostForm {
  height: 180px !important;
}
#smLpShape3 {
  height: 333px;
  border-radius: 30px;
  background-color: floralwhite;
  margin: 20px;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  font-weight: 500;
  text-align: center;
}

#smLpBubble {
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
#smLpSmallBubble {
  position: absolute;
  background-color: floralwhite;
  padding: 25px;
  border-radius: 50%;
  height: 25px;
  width: 100px;
  display: flex;
  justify-content: center;
  flex-flow: column;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
  bottom: 25%;
  left: 30%;
}
#smLpSpeechBubble {
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
#smLpSpeechBubble::before {
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
#smLpSpeechBubble::after {
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

#smLpFooter {
  flex-flow: column;
  height: 150px;
  background-color: transparent;
  justify-content: center;
  width: 100vw;
  min-width: 1114px;
}
#smLpFooterBtns {
  display: flex;
  justify-content: space-around;
  width: 75%;
  margin: 20px 0;
}
#smLpFooterBtn {
  width: 25%;
  font-size: 15px;
}
</style>



<script>
import DisplayPosts from "@/components/mainContents/DisplayPosts.vue";
import Login from "@/components/overlays/Login.vue";

export default {
  name: "LandingPage",
  components: {
    DisplayPosts,
    Login,
  },
  data() {
    return {
      scrollY: 0,
      visibleStartY: 0,
      smLpTxt1: `誰かにほめてもらえる
      優しいSNS`,
      smLpTxt2: `こんなSNS
      あったらいいのにな`,
      smLpTxt2_1: `ちょっとしたことでも
      ほめてもらいたい`,
      smLpTxt2_2: `嫌な返信が来たら
      どうしよう`,
      smLpTxt2_3: `もっと疲れない
      SNSがあったらいいのに`,
      smLpTxt3: `こんなときに
      HOMETEは使えるよ`,
      smLpTxt4: `匿名で投稿できて
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
