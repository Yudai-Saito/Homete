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
        <img
          src="/assets/homete.png"
          style="width: 150px; position: relative; top: -3px; left: -15px"
        />
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
        <div id="smLPSubTitle">SOCIAL</div>
        <div id="smLPContentInner">
          <div
            v-text="smLpTxt2"
            style="font-size: 25px; font-weight: 600; margin: 5% 0"
          ></div>
          <div id="smLpBubble" style="left: 15%" v-text="smLpTxt2_1"></div>
          <div id="smLpBubble" style="right: 0%" v-text="smLpTxt2_2"></div>
          <div id="smLpBubble" style="right: -5%" v-text="smLpTxt2_3"></div>
          <div id="smLpSmallBubble"></div>
          <img
            src="/assets/HOMETE_LP2.png"
            style="width: 215px; position: relative; left: 40%; bottom: 8%"
          />
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
        <div id="smLPSubTitle">WHEN TO USE</div>
        <div id="smLPContentInner">
          <div
            v-text="smLpTxt3"
            style="font-size: 25px; font-weight: 600; margin: 5% 0"
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
                    style="width: 180px; margin-top: 10px"
                  />
                </div>
              </v-carousel-item>
              <v-carousel-item>
                <div id="smLpShape3">
                  ほしかったものが買えた
                  <img
                    src="/assets/HOMETE_LP4.png"
                    style="width: 180px; margin-top: 10px"
                  />
                </div>
              </v-carousel-item>
              <v-carousel-item>
                <div id="smLpShape3">
                  今日も自炊してえらい！
                  <img
                    src="/assets/HOMETE_LP5.png"
                    style="width: 180px; margin-top: 10px"
                  />
                </div>
              </v-carousel-item>
            </v-carousel>
          </div>
        </div>
      </div>
    </div>
    <div id="smLpBoard">
      <div
        ref="sampleContent"
        id="smLpContent"
        class="amber lighten-4"
        style="
          display: flex;
          flex-flow: column;
          justify-content: space-evenly;
          align-items: center;
          padding: 5% 0;
        "
      >
        <div id="smLPSubTitle" style="margin-left: 5%; margin-bottom: 10px">
          HOW TO USE
        </div>
        <div id="smLPContentInner" style="margin-top: 0" ref="samplePost">
          <DisplayPosts
            id="smLpPostSample"
            v-for="samplePost in samplePosts"
            :key="samplePost.post_id"
            :postList="samplePost"
            :isSample="true"
          />
          <div
            v-if="displayPostForm"
            @click="closeLPPostForm"
            style="
              z-index: 2;
              position: absolute;
              top: 0px;
              width: 100%;
              height: 100%;
              margin: auto 0;
              border-radius: 50px;
              padding: 5%;
            "
          ></div>

          <transition name="fade">
            <div
              v-show="displayPostForm"
              style="
                background-color: rgba(0, 0, 0, 0.25);
                z-index: 1;
                position: absolute;
                top: 0px;
                width: 100%;
                height: 100%;
                margin: auto 0;
                border-radius: 50px;
                padding: 5%;
              "
            >
              <transition name="slide-y-reverse">
                <PostForm
                  v-show="displayPostForm"
                  id="smLpPostFormSample"
                  :sampleLabel="`いろんなことを投稿しよう！`"
                />
              </transition>
              <div
                v-if="displayPostForm"
                id="arrow_box1sm"
                v-text="h2uTxt1"
              ></div>
            </div>
          </transition>
          <div id="arrow_box2sm" v-text="h2uTxt2"></div>
          <div
            id="postBtnFloat"
            ref="postBtn"
            style="
              position: relative;
              transition: all 0.4s ease 0s !important;
              transform: translateX(0px);
              z-index: 0;
              bottom: 15%;
              margin-left: auto;
              width: fit-content;
            "
          >
            <v-btn
              class="d-md-none"
              style="background-color: rgb(225 255 255)"
              elevation="3"
              fab
              icon
              rounded
              @click="onClickLPPostBtn"
            >
              <v-icon color="rgb(73,72,84)"> mdi-pen-plus </v-icon>
            </v-btn>
          </div>
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
        <div id="smLPSubTitle">FRIENDRY</div>
        <div id="smLPContentInner">
          <div style="width: 50%; bottom: -30px; position: relative">
            <div
              v-text="smLpTxt4"
              style="font-size: 20px; text-align: center; font-weight: 600"
              id="smLpSpeechBubble"
            ></div>
          </div>
          <img
            src="/assets/HOMETE_LP6.png"
            style="width: 300px; position: relative; right: -17%"
          />
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
        <div
          style="
            width: 95%;
            font-size: 30px;
            text-align: center;
            font-weight: 600;
          "
        >
          <div style="transform: translateX(-20px)">ちょっとの喜びを</div>
          <div style="transform: translateX(35px)">HOMETEと一緒に</div>
        </div>
        <img src="/assets/HOMETE_LP7.png" style="width: 230px" />
        <button
          id="smLpBtnSignup"
          style="
            right: 3%;
            bottom: 20%;
            padding: 5px 15px;
            transform: scale(1.35) translateX(35px);
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
  padding: 20px 0;
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
  margin-left: 20px;
}
#smLPSubTitle {
  position: relative;
  border-left: black solid 5px;
  font-size: 35px;
  font-weight: 700;
  padding: 0 15px;
  margin-top: 10%;
  margin-right: auto;
}
#smLpBtns {
  margin-left: auto;
}
#smLpBtnSignup {
  font-size: 13px;
  color: floralwhite;
  border-radius: 28px;
  padding: 5px 15px;
  font-weight: 500;
  background-color: rgb(139 143 210);
  border: 3px solid rgb(139 143 210);
  transition: background-color 0.2s, color 0.2s;
  top: -6px;
  position: relative;
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
#smLPContentInner {
  margin: auto 0;
  width: 100%;
  max-height: 85%;
}
#smLpPostSample {
  margin: 0 auto;
  padding: 0;
  transform: scale(0.85);
  width: 110%;
  height: 34%;
  max-width: 110%;
  right: 5%;
  position: relative;
}
#smLpPostFormSample {
  margin: 0 auto;
  padding: 0;
  width: 100%;
  position: absolute;
  bottom: 0;
  z-index: 5;
  right: 0;
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
  margin: 20px auto;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  font-weight: 500;
  text-align: center;
  width: 260px;
}

#smLpBubble {
  position: relative;
  background-color: floralwhite;
  border-radius: 50%;
  height: 12%;
  width: 260px;
  display: flex;
  justify-content: center;
  flex-flow: column;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 5px;
}
#smLpSmallBubble {
  position: relative;
  background-color: floralwhite;
  border-radius: 50%;
  height: 40px;
  width: 25%;
  display: flex;
  justify-content: center;
  flex-flow: column;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
  left: 35%;
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
  height: 180px;
  width: 300px;
  right: -5%;
  margin-left: auto;
  margin-right: 5%;
}
#smLpSpeechBubble::before {
  content: "";
  position: absolute;
  display: block;
  border-radius: 50%;
  background-color: #f6b167;
  right: 69%;
  bottom: -25%;
  width: 30px;
  height: 30px;
}
#smLpSpeechBubble::after {
  content: "";
  position: absolute;
  display: block;
  border-radius: 50%;
  background-color: #f6b167;
  right: 66%;
  bottom: -55%;
  width: 18px;
  height: 18px;
}
#arrow_box1sm {
  position: absolute;
  width: 285px;
  height: 120px;
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
  bottom: 330px;
  right: 13%;
  -moz-filter: drop-shadow(5px 5px 5px #7f483a);
  -ms-filter: drop-shadow(5px 5px 5px #7f483a);
  filter: drop-shadow(5px 5px 5px #7f483a);
  z-index: 5;
}
#arrow_box1sm:after,
#arrow_box1sm:before {
  border: solid transparent;
  content: "";
  height: 0;
  width: 0;
  pointer-events: none;
  position: absolute;
  top: 100%;
  left: 71%;
}
#arrow_box1sm:after {
  border-color: rgba(0, 153, 255, 0);
  border-top-width: 19px;
  border-bottom-width: 19px;
  border-left-width: 15px;
  border-right-width: 15px;
  margin-left: -15px;
  border-top-color: floralwhite;
}
#arrow_box1sm:before {
  border-top-width: 20px;
  border-bottom-width: 20px;
  border-left-width: 16px;
  border-right-width: 16px;
  margin-left: -15.5px;
  border-top-color: #f6b167;
}

#arrow_box2sm {
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
  top: 235px;
  right: -8%;
  -webkit-filter: drop-shadow(5px 5px 5px #7f483a);
  -moz-filter: drop-shadow(5px 5px 5px #7f483a);
  -ms-filter: drop-shadow(5px 5px 5px #7f483a);
  filter: drop-shadow(5px 5px 5px #7f483a);
  transform: scale(0.9);
}
#arrow_box2sm:after,
#arrow_box2sm:before {
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
#arrow_box2sm:after {
  border-color: rgba(0, 153, 255, 0);
  margin-left: -256px;
  border-top-color: floralwhite;
  border-top-width: 20px;
  border-bottom-width: 10px;
  border-left-width: 14px;
  border-right-width: 10px;
}
#arrow_box2sm:before {
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
}
#smLpFooterBtns {
  display: flex;
  width: 100%;
  margin: 20px 0;
  flex-wrap: wrap;
}
#smLpFooterBtn {
  width: 50%;
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
      displayPostForm: false,
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
      ことを書いて投稿しよう！
      ※ここでは投稿はできないよ！`,
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
    onClickLPPostBtn: function () {
      this.displayPostForm = true;
    },
    closeLPPostForm: function () {
      this.displayPostForm = false;
    },
    handleScroll() {
      this.scrollY = window.scrollY;
    },
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  watch: {
    scrollY(newY, oldY) {
      if (newY - oldY > 0) {
        if (newY - this.visibleStartY > 400) {
          document.getElementById("smLpHeader").style.transform =
            "translateY(-100px)";
        }
      } else {
        document.getElementById("smLpHeader").style.transform =
          "translateY(0px)";
        this.visibleStartY = newY;
      }
    },
  },
};
</script>
