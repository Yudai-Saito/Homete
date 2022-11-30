<template>
  <v-app class="artBoard blue-grey lighten-5">
    <Header />
    <v-overlay :value="displayLogin" :light="true" :dark="false" :z-index="999">
      <Login />
    </v-overlay>
    <v-overlay
      :value="displayDelete"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <v-card
        width="450px"
        height="300px"
        class="mx-auto mt-5 pa-2 rounded-xl"
        v-cloak
        v-click-outside="closeDeleteCard"
      >
        <div>
          <v-btn icon plain text class="closeCardBtn" @click="closeDeleteCard">
            <v-icon color="#23282F">mdi-close</v-icon>
          </v-btn>
          <v-card-title
            style="font-weight: 700 !important"
            class="justify-center"
            >アカウント削除</v-card-title
          >
          <v-card-text
            style="
              margin-top: 10px;
              padding: 0 !important;
              text-align: center;
              font-weight: bold;
            "
          >
            <div style="text-align: left; margin: 0 auto; width: 330px">
              <div>
                <input
                  type="checkbox"
                  id="check1"
                  value="check1"
                  v-model="checked"
                />
                <label for="check1">自分の投稿は全て消えてしまいます。</label>
              </div>
              <div>
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
              <div>
                <input
                  type="checkbox"
                  id="check3"
                  value="check3"
                  v-model="checked"
                />
                <label for="check3">アカウント情報は復元できません。</label>
              </div>
            </div>
            <p style="margin-top: 20px; margin-bottom: 0 !important">
              全てにチェックをつけてアカウントを削除する
            </p>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn
              large
              @click="deleteAccount"
              class="text-transform ma-0 pa-0"
              color="error"
              :disabled="btnDisable"
            >
              <div style="padding: 0 !important" class="deleteBtnTxt">
                アカウントを削除する
              </div>
            </v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-overlay>
    <div>
      <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
        <v-col cols="3">
          <LeftMenu class="SideMenuSticky" />
        </v-col>
        <v-col class="mainContents" cols="6">
          <div class="settingContainer">
            <div class="btnTxt">
              <div
                v-twemoji
                style="width: 20px; margin-right: 5px; margin-top: 10px"
              >
                🚀
              </div>
              <h3 v-twemoji class="settingTitle">ログアウト</h3>
            </div>
            <p class="settingText">
              ログアウトします。また会える日を楽しみにしています。
            </p>
            <v-btn
              class="ma-0 pa-0 settingBtn"
              color="primary"
              x-large
              :elevation="3"
              v-on:click="logout"
            >
              <div class="btnTxt">
                <div v-twemoji style="width: 18px; margin-right: 5px">✈️</div>
                <div>ログアウト</div>
              </div>
            </v-btn>
          </div>
          <div class="settingContainer">
            <div class="btnTxt">
              <div
                v-twemoji
                style="width: 20px; margin-right: 5px; margin-top: 10px"
              >
                🗑
              </div>
              <h3 v-twemoji class="settingTitle">アカウント削除</h3>
            </div>
            <p class="settingText">
              アカウントを削除します。全ての投稿と全てのリアクションが削除されます。
            </p>
            <v-btn
              class="ma-0 pa-0 settingBtn"
              color="error"
              x-large
              :elevation="3"
              @click="displayDeleteCard"
            >
              <div class="btnTxt">
                <div v-twemoji style="width: 18px; margin-right: 5px">⚠️</div>
                <div>アカウント削除</div>
              </div>
            </v-btn>
          </div>
        </v-col>
        <v-col class="SideMenuSticky rightMenu" cols="3"></v-col>
      </v-row>
    </div>
    <Footer />
  </v-app>
</template>
<style>
.artBoard {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.contentsFlex {
  width: 100%;
  flex-wrap: nowrap;
}
.closeCardBtn {
  justify-content: center;
  position: absolute;
  left: 400px;
}
.deleteBtnTxt {
  color: #ffffff;
  margin-right: 8px;
  margin-left: 8px;
}
.SideMenuSticky {
  position: sticky;
  top: 0;
  flex-wrap: nowrap;
}
.mainContents {
  margin: 0;
  margin-top: 47px;
  margin-bottom: 20px;
  padding: 0;
  width: 550px;
  min-width: 550px;
  max-width: 550px;
}
.rightMenu {
  display: flex;
  height: 100vh;
  min-height: 100vh;
  max-height: 100vh;
  margin: 0;
  padding: 0;
}
.settingContainer {
  width: 100%;
  height: 30%;
  margin-top: 30px;
  border-top: solid black 2px;
  text-align: center;
}
.settingTitle {
  margin-top: 10px;
  color: #494854;
}
.settingText {
  font-size: 14px;
  margin: 10px 0;
  color: #494854;
}
.settingBtn {
  height: 40px !important;
}
.btnTxt {
  margin: 0 15px;
  display: flex;
  justify-content: center;
}
</style>


<script>
import Login from "@/components/Account/Login.vue";
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";
import twemoji from "twemoji";

export default {
  name: "AccountManagement",
  directives: {
    twemoji: {
      inserted(el) {
        el.innerHTML = twemoji.parse(el.innerHTML, {
          folder: "svg",
          ext: ".svg",
        });
      },
    },
  },
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    displayLogin() {
      return this.$store.getters.displayLogin;
    },
  },
  data() {
    return {
      displayDelete: false,
      checked: [],
      btnDisable: true,
    };
  },
  components: {
    Login,
    LeftMenu,
    Footer,
    Header,
  },
  methods: {
    displayDeleteCard() {
      this.displayDelete = true;
    },
    closeDeleteCard() {
      this.displayDelete = false;
      this.checked = [];
    },
    deleteAccount() {},
    logout() {},
  },
  mounted() {
    window.onload = () => {
      this.$store.dispatch("invisiblePostForm");
      this.$store.dispatch("invisibleLogin");
    };
  },
  updated() {
    if (
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
