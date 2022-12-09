<template>
  <v-app-bar
    id="header"
    style="border-bottom: solid #00000080 1px"
    color="#BABDBE"
    fixed
    elevation="0"
  >
    <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
      <div id="hamburgerMenu" :class="{ active: isActive }" @click="toggleMenu">
        <span></span><span>Menu</span><span></span>
      </div>
      <v-col id="title" class="md-none text-h5 font-weight-bold" cols="3">
        homete…
      </v-col>
      <v-col id="contentTitle" cols="6" lg="5">
        {{ contentName }}
      </v-col>
      <v-col id="headerBtn" cols="3">
        <v-btn color="#CFD8DC" rounded @click="account" v-if="logged">
          <v-icon color="#494854">mdi-account-cog</v-icon>
          <div>アカウント</div>
        </v-btn>
        <v-btn color="#CFD8DC" rounded @click="login" v-else>
          <v-icon color="#494854">mdi-login-variant</v-icon>
          <div>ログイン</div>
        </v-btn>
      </v-col>
    </v-row>
  </v-app-bar>
</template>

<style lang="scss">
@media (min-width: map-get($grid-breakpoints, sm)) {
  // sm 以上のブレークポイントでのスタイル定義
  #title,
  #headerBtn {
    display: flex;
  }
  #hamburgerMenu {
    display: none;
  }
}
@media (max-width: map-get($grid-breakpoints, sm)) {
  // sm 以下のブレークポイントでのスタイル定義
  #title,
  #headerBtn {
    display: none;
  }
  #hamburgerMenu {
    display: block;
  }
}

#header div {
  padding: 0 !important;
}
#title {
  margin: 0;
  padding: 0;
  justify-content: center;
  color: #494854;
}
#contentTitle {
  margin: 0;
  padding: 0;
  width: 550px;
  display: flex;
  justify-content: center;
  font-size: 20px;
  font-weight: 900;
  color: #494854;
}
#headerBtn {
  margin: 0;
  padding: 0;
  justify-content: center;
}
#headerBtn button {
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
}

/*ボタン外側※レイアウトによってpositionや形状は適宜変更してください*/
#hamburgerMenu {
  position: absolute; /*ボタン内側の基点となるためrelativeを指定*/
  cursor: pointer;
  width: 45px;
  height: 45px;
  border-radius: 5px;
  border: solid #494854 1px;
  top: 5px;
  left: 5px;
}

/*ボタン内側*/
#hamburgerMenu span {
  display: inline-block;
  transition: all 0.4s; /*アニメーションの設定*/
  position: absolute;
}

#hamburgerMenu span:nth-of-type(1),
#hamburgerMenu span:nth-of-type(3) {
  height: 2px;
  background: #494854;
  width: 62%;
  left: 8px;
}

#hamburgerMenu span:nth-of-type(1) {
  top: 10px;
}

#hamburgerMenu span:nth-of-type(2) {
  top: 14px;
  left: 7px;
  font-size: 0.6rem;
  text-transform: uppercase;
  color: #494854;
}

#hamburgerMenu span:nth-of-type(3) {
  top: 30px;
}

/*activeクラスが付与されると線が回転して×になり、Menu表記をしている2つ目の要素が透過して消える*/
#hamburgerMenu.active span:nth-of-type(1) {
  top: 14px;
  left: 14px;
  transform: translateY(6px) rotate(-45deg);
  width: 30%;
}

#hamburgerMenu.active span:nth-of-type(2) {
  opacity: 0;
}

#hamburgerMenu.active span:nth-of-type(3) {
  top: 26px;
  left: 14px;
  transform: translateY(-6px) rotate(45deg);
  width: 30%;
}
/*========= レイアウトのためのCSS ===============*/

body {
  background: #f3f3f3;
  padding: 20px;
}

a {
  color: #333;
  text-decoration: none;
}

.lead {
  margin: 20px 0 0 0;
}

.btn-block {
  width: 200px;
  padding: 30px;
}
</style>

<script>
export default {
  name: "Header",
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
    contentName() {
      return this.$store.getters.contentName;
    },
  },
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    login: function () {
      this.$store.dispatch("visibleLoginOverlay");
    },
    logout: function () {
      this.$store.dispatch("loggedOut");
    },
    account: function () {
      this.$store.dispatch("toAccount");
      if (this.$route.path != "/account") {
        this.$router.push("/account");
      }
    },
    toggleMenu: function () {
      this.isActive = !this.isActive;
    },
  },
};
</script>
