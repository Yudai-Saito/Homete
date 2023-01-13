<template>
  <div id="artBoard" style="background-color: floralwhite">
    <Login />
    <v-app-bar
      ref="lpHeader"
      id="lpHeader"
      elevation="0"
      flat
      fixed
      floating
      color="transparent"
    >
      <div id="lpTitle" class="text-h4 font-weight-bold" @click="toTop">
        homete…
      </div>
      <div id="lpBtns">
        <v-btn id="lpBtnNomal" plain text :ripple="false" @click="scrollToAbout"
          >hometeとは</v-btn
        >
        <v-btn id="lpBtnNomal" plain text :ripple="false" @click="scrollToGuide"
          >使い方</v-btn
        >
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
        <div v-text="lpTxt1"></div>
        <img src="/assets/HOMETE_LP1.png" style="width: 40%" />
      </div>
    </div>
    <div id="lpBoard" ref="about">
      <div
        id="lpContent"
        class="amber lighten-4"
        style="display: flex; justify-content: center; align-items: center"
      >
        <div v-text="lpTxt2"></div>
        <img src="/assets/HOMETE_LP2.png" style="width: 40%" />
      </div>
    </div>
    <div id="lpBoard">
      <div
        id="lpContent"
        class="amber lighten-4"
        style="display: flex; justify-content: center; align-items: center"
      >
        <DisplayPosts
          id="lpPostSample"
          :postList="samplePost"
          :isSample="true"
        />
        <div v-text="lpTxt3"></div>
      </div>
    </div>
    <div id="lpBoard" ref="guide">
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
        <div v-text="lpTxt4"></div>
        <div
          style="
            display: flex;
            justify-content: space-around;
            align-items: center;
          "
        >
          <div id="lpShape4">
            かわいい絵を描けた
            <img
              src="/assets/HOMETE_LP3.png"
              style="width: 100%; margin-top: 20px"
            />
          </div>
          <div id="lpShape4">
            ほしかったものが買えた
            <img
              src="/assets/HOMETE_LP4.png"
              style="width: 100%; margin-top: 20px"
            />
          </div>
          <div id="lpShape4">
            今日も自炊してえらい！
            <img
              src="/assets/HOMETE_LP5.png"
              style="width: 100%; margin-top: 20px"
            />
          </div>
        </div>
      </div>
    </div>
    <div id="lpBoard">
      <div
        id="lpContent"
        class="amber lighten-4"
        style="display: flex; justify-content: center; align-items: center"
      >
        <div v-text="lpTxt5"></div>
        <img src="/assets/HOMETE_LP6.png" style="width: 40%" />
      </div>
    </div>
    <div id="lpBoard">
      <div
        id="lpContent"
        class="amber lighten-4"
        style="display: flex; justify-content: center; align-items: center"
      >
        <img src="/assets/HOMETE_LP7.png" style="width: 50%" />
        <div style="width: 33%">
          <div>日常にちょっとの喜びを</div>
          <div style="transform: translateX(80px)">HOMETEと一緒に</div>
        </div>
        <button
          id="lpBtnSignup"
          style="position: absolute; right: 15%; bottom: 25%"
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
</template>

<style>
@media (max-width: 760px) {
  #lpBtns {
    min-width: 530px;
    transform: scale(0.8);
  }
}
@media (min-width: 760px) {
  #lpBtns {
    text-align: right;
  }
}
html {
  scroll-behavior: smooth;
}
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
#lpBtnNomal {
  margin-right: 10px;
  font-size: 15px;
}
#lpBtnNomal .v-btn__content {
  opacity: 0.75;
}
#lpBtnSignup {
  font-size: 15px;
  color: floralwhite;
  border-radius: 28px;
  padding: 5px 15px;
  font-weight: 500;
  background-color: #3e2723;
  border: 3px solid #3e2723;
  transition: background-color 0.2s, color 0.2s;
}
#lpBtnSignup:hover {
  background-color: transparent;
  color: #494854;
}

#lpBoard {
  display: flex;
  justify-content: center;
  width: 100vw;
  height: 100vh;
}
#lpContent {
  position: relative;
  width: 90vw;
  height: 90vh;
  margin: auto 0;
  border-radius: 50px;
}
#lpContent div {
  white-space: pre-line;
}

#lpPostSample {
  width: 50%;
  margin: 0;
  margin-right: 50px;
}
#lpShape4 {
  height: 60vh;
  width: 22vw;
  border-radius: 30px;
  background-color: floralwhite;
  margin: 20px;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
}

#lpFooter {
  flex-flow: column;
  height: 150px;
  background-color: transparent;
  justify-content: center;
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
    if (window.matchMedia(`(max-width: ${gridBreakpoints.sm}px)`).matches) {
      this.$router.push("/smcontact");
    }
  },
  data() {
    return {
      scrollY: 0,
      visibleStartY: 0,
      lpTxt1: `HOMETEのキャッチコピー的なやつ`,
      lpTxt2: `あなたのがんばりを
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
      lpTxt3: `日常のどんなことでも
      ほめてもらえる的な文章`,
      lpTxt4: `こんなときにHOMETE使えるよ的なやつ`,
      lpTxt5: `匿名で投稿できて匿名でリアクションをもらえるよ
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
          document.getElementById("lpHeader").style.transform =
            "translateY(-100px)";
        }
      } else {
        document.getElementById("lpHeader").style.transform = "translateY(0px)";
        this.visibleStartY = newY;
      }
    },
  },
};
</script>
