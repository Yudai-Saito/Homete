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
      <div id="smLpTitle" class="text-h6 font-weight-bold" @click="toTop">
        homete…
      </div>
      <div id="smLpBtns">
        <v-btn
          id="smLpBtnNomal"
          plain
          text
          :ripple="false"
          @click="scrollToAbout"
          >hometeとは</v-btn
        >
        <v-btn
          id="smLpBtnNomal"
          plain
          text
          :ripple="false"
          @click="scrollToGuide"
          >使い方</v-btn
        >
        <v-btn
          id="smLpBtnNomal"
          plain
          text
          :ripple="false"
          @click="scrollToQuestion"
          >よくある質問</v-btn
        >
        <button id="smLpBtnSignup" @click="login">Googleで登録する</button>
      </div>
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
        <div v-text="smLpTxt1"></div>
        <img src="/assets/HOMETE_LP1.png" style="width: 60%" />
      </div>
    </div>
    <div id="smLpBoard" ref="about">
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
        <div v-text="smLpTxt2"></div>
        <img src="/assets/HOMETE_LP2.png" style="width: 60%" />
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
        <div v-text="smLpTxt3"></div>
        <DisplayPosts
          id="smLpPostSample"
          :postList="samplePost"
          :isSample="true"
        />
      </div>
    </div>
    <div id="smLpBoard" ref="guide">
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
        <div v-text="smLpTxt4"></div>
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
              <div id="smLpShape4">
                かわいい絵を描けた
                <img
                  src="/assets/HOMETE_LP3.png"
                  style="width: 60%; margin-top: 10px"
                />
              </div>
            </v-carousel-item>
            <v-carousel-item>
              <div id="smLpShape4">
                ほしかったものが買えた
                <img
                  src="/assets/HOMETE_LP4.png"
                  style="width: 60%; margin-top: 10px"
                />
              </div>
            </v-carousel-item>
            <v-carousel-item>
              <div id="smLpShape4">
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
    <div id="smLpBoard" ref="question">
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
        <div v-text="smLpTxt5" style="width: 75%"></div>
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
        <div style="width: 65%">
          <div>日常にちょっとした喜びを</div>
          <div style="transform: translateX(110px)">HOMETEと一緒に</div>
        </div>
        <img src="/assets/HOMETE_LP7.png" style="width: 70%" />
        <button
          id="smLpBtnSignup"
          style="position: absolute; right: 3%; bottom: 20%; padding: 5px 15px"
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
html {
  scroll-behavior: smooth;
}
#smLpHeader {
  z-index: 2;
  padding: 20px;
  transition: transform 0.5s;
}
#smLpHeader .v-toolbar__content {
  height: 48px !important;
  width: 100%;
  justify-content: space-between;
  padding: 0px 3px;
  transform: translateX(-5px);
}

#smLpTitle {
  margin: 0;
  padding: 0;
  color: #494854;
}
#smLpBtns {
  text-align: right;
  font-size: 5px;
  display: flex;
  margin-left: 5px;
}
#smLpBtnNomal {
  font-size: 5px;
  transform: scale(0.8);
  min-width: 0px;
  padding: 0;
}
#smLpBtnNomal .v-btn__content {
  opacity: 0.75;
}
#smLpBtnSignup {
  color: floralwhite;
  border-radius: 28px;
  font-weight: 500;
  background-color: #3e2723;
  border: 3px solid #3e2723;
  transition: background-color 0.2s, color 0.2s;
  transform: scale(0.8);
  min-width: 100px;
}
#smLpBtnSignup:hover {
  background-color: transparent;
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
  width: 90vw;
  height: 90vh;
  margin: auto 0;
  border-radius: 10%;
}
#smLpContent div {
  white-space: pre-line;
}

#smLpPostSample {
  width: 100%;
  margin: 0;
}
#smLpShape4 {
  border-radius: 30px;
  background-color: floralwhite;
  margin: 20px;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  height: 50vh;
}

#smLpFooter {
  flex-flow: column;
  height: 150px;
  background-color: transparent;
  justify-content: center;
}
#smLpFooterBtns {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin: 20px 0;
}
#smLpFooterBtn {
  font-size: 5px;
  padding: 0 8px !important;
}
</style>


<script>
import DisplayPosts from "@/components/mainContents/DisplayPosts.vue";
import Login from "@/components/overlays/Login.vue";

// $grid-breakpoints を JavaScript のオブジェクトとして取得
const gridBreakpoints = { xs: 0, sm: 600, md: 960, lg: 1495, xl: 1904 };

export default {
  name: "LandingPage",
  components: {
    DisplayPosts,
    Login,
  },
  beforeCreate() {
    if (window.matchMedia(`(min-width: ${gridBreakpoints.sm}px)`).matches) {
      this.$router.push("/contact");
    }
  },
  data() {
    return {
      scrollY: 0,
      visibleStartY: 0,
      smLpTxt1: `HOMETEのキャッチコピー的なやつ`,
      smLpTxt2: `あなたのがんばりを
      誰かがリアクションでほめてくれる的な
      どんなサービスなのか的な文章`,
      samplePost: {
        contents: "こんなサービスができたよ！",
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
      smLpTxt3: `日常のどんなことでも
      ほめてもらえる的な文章`,
      smLpTxt4: `こんなときにHOMETE使えるよ的なやつ`,
      smLpTxt5: `匿名で投稿できて匿名でリアクションをもらえるよ
      あなたに酷いコメントは届かないよ`,
    };
  },
  methods: {
    login: function () {
      this.$store.dispatch("visibleLoginOverlay");
    },
    toTop: function () {
      this.$store.dispatch("invisibleMenu");
      this.$store.dispatch("toTimeLine").then(() => {
        this.$router.push("/");
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
    scrollToAbout() {
      this.$refs.about.scrollIntoView();
    },
    scrollToGuide() {
      this.$refs.guide.scrollIntoView();
    },
    scrollToQuestion() {
      this.$refs.question.scrollIntoView();
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
