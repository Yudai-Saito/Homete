<template>
  <v-card
    id="overlayCard"
    class="mx-auto pa-2 rounded-xl"
    v-cloak
    v-click-outside="closeOverlayCard"
  >
    <div style="margin: 10px">
      <v-btn
        v-if="usage == 'login'"
        icon
        plain
        text
        id="closeOverlayBtn"
        @click="closeOverlayCard"
      >
        <v-icon color="#23282F">mdi-close</v-icon>
      </v-btn>

      <img
        v-if="usage === 'login'"
        src="/assets/homete.webp"
        style="
          width: 60%;
          position: relative;
          top: 0px;
          display: block;
          margin: 35px auto 5px;
        "
      />
      <v-card-title v-else class="justify-center" style="font-weight: 600">
        {{ titleTxt }}
      </v-card-title>
      <v-card-text style="padding: 0 16px" v-if="usage == 'deleteAccount'">
        <div
          style="
            text-align: left;
            margin: 0 auto;
            width: 330px;
            font-weight: 600;
          "
        >
          <div id="deleteAccountTxt">
            <input
              type="checkbox"
              id="check1"
              value="check1"
              v-model="checked"
            />
            <label for="check1">自分の投稿は全て消えてしまいます。</label>
          </div>
          <div id="deleteAccountTxt">
            <input
              type="checkbox"
              id="check2"
              value="check2"
              v-model="checked"
            />
            <label for="check2"
              >あげたリアクションは全て消えてしまいます。</label
            >
          </div>
          <div id="deleteAccountTxt">
            <input
              type="checkbox"
              id="check3"
              value="check3"
              v-model="checked"
            />
            <label for="check3">アカウント情報は復元できません。</label>
          </div>
        </div>
      </v-card-text>
      <v-card-text style="padding: 8px 16px">
        <div
          style="width: fit-content; margin: 0 auto"
          :style="
            usage == 'deleteAccount' ? 'font-weight:600' : 'font-weigt:normal'
          "
        >
          {{ firstMsg }}
        </div>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
          large
          @click="onClick"
          class="text-transform ma-0 pa-0 rounded-lg"
          :color="
            usage === 'login'
              ? 'white'
              : usage === 'reportPost'
              ? 'yellow'
              : 'red'
          "
          :disabled="usage == 'deleteAccount' ? btnDisable : false"
        >
          <img
            v-if="usage == 'login'"
            id="googleSvg"
            src="/assets/google-login-btn.svg"
            @click="onClick"
          />
          <div
            :style="
              usage == 'login' || usage == 'reportPost'
                ? 'color: #494854'
                : 'color: white'
            "
            id="overlayBtnTxt"
          >
            {{ btnTxt }}
          </div>
        </v-btn>
      </v-card-actions>

      <v-card-text v-if="usage == 'login'">
        <p>
          <a @click="toUserPolicy">利用規約</a>、
          <a @click="toPrivacyPolicy">プライバシーポリシー</a>
          に同意したうえでログインしてください
        </p>
      </v-card-text>
      <v-card-actions v-else class="justify-center">
        <v-btn
          style="margin-top: 10px"
          large
          @click="closeOverlayCard"
          class="text-transform ma-0 pa-0 rounded-lg"
          color="white"
        >
          <div id="overlayBtnTxt">戻る</div>
        </v-btn>
      </v-card-actions>
    </div>
  </v-card>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #overlayCard {
    width: 400px;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #overlayCard {
    width: 83%;
  }
}
#closeOverlayBtn {
  justify-content: center;
  position: absolute !important;
  right: 15px !important;
  top: 10px;
}
#overlayBtnTxt {
  margin-right: 8px;
  margin-left: 8px;
  text-transform: none;
  font-weight: 600;
}
#googleSvg {
  background-image: url("/assets/google-login-btn.svg");
}
#deleteAccountTxt label {
  font-size: 0.8rem;
  position: relative;
  top: -2px;
}
</style>

<script>
export default {
  name: "CommonOverlay",
  data() {
    return {
      checked: [],
      btnDisable: true,
    };
  },
  props: [
    "usage",
    "titleTxt",
    "firstMsg",
    "btnTxt",
    "descriptionTxt",
    "onClick",
  ],
  methods: {
    closeOverlayCard: function () {
      this.$store.dispatch("invisibleCommonOverlay");
      if (this.usage == "deleteAccount") {
        this.checked = [];
      }
    },
    toUserPolicy: function () {
      this.$store.dispatch("invisibleCommonOverlay");
      this.$store.dispatch("toUserPolicy").then(() => {
        if (this.$route.path != "/about") {
          this.$router.push("/about");
        }
      });
    },
    toPrivacyPolicy: function () {
      this.$store.dispatch("invisibleCommonOverlay");
      this.$store.dispatch("toPrivacyPolicy").then(() => {
        if (this.$route.path != "/about") {
          this.$router.push("/about");
        }
      });
    },
  },
  updated() {
    if (
      this.usage == "deleteAccount" &&
      this.checked.includes("check1") &&
      this.checked.includes("check2") &&
      this.checked.includes("check3")
    ) {
      this.btnDisable = false;
    } else {
      this.btnDisable = true;
    }
  },
};
</script>

