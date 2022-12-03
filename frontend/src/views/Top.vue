<template>
  <v-app class="artBoard blue-grey lighten-5">
    <Header />
    <v-overlay
      :value="overlayState == 'login'"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <CommonOverlay
        usage="login"
        titleTxt="HOMETE"
        firstMsg="ここに適当なサービスの説明とようこそ的な文章"
        btnTxt="Googleでログイン"
        descriptionTxt="ここに注意事項的な文章"
        :onClick="logIn"
      />
    </v-overlay>
    <v-overlay
      :value="overlayState == 'deletePost'"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <CommonOverlay
        usage="deletePost"
        titleTxt="本当に削除しますか？"
        firstMsg="この投稿はタイムライン、あなたのヒストリーから削除されます。"
        btnTxt="削除する"
        :onClick="deletePost"
      />
    </v-overlay>
    <v-overlay
      :value="overlayState == 'reportPost'"
      :light="true"
      :dark="false"
      :z-index="999"
    >
      <CommonOverlay
        usage="reportPost"
        titleTxt="注意"
        firstMsg="この投稿を管理者に通報します。"
        btnTxt="通報する"
        :onClick="reportPost"
      />
    </v-overlay>
    <div>
      <Alert />
      <v-row justify="center" class="contentsFlex mx-auto my-auto" no-gutters>
        <v-col cols="3">
          <LeftMenu class="SideMenuSticky" />
        </v-col>
        <v-col cols="6">
          <TimeLine />
        </v-col>
        <v-col cols="3">
          <RightMenu class="SideMenuSticky" />
        </v-col>
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
.SideMenuSticky {
  position: sticky;
  top: 0;
  flex-wrap: nowrap;
  margin: 0;
  padding: 0;
}
</style>


<script>
import CommonOverlay from "@/components/Account/CommonOverlay.vue";
import LeftMenu from "@/components/leftMenu/LeftMenu.vue";
import TimeLine from "@/components/mainContents/TimeLine.vue";
import RightMenu from "@/components/rightMenu/RightMenu.vue";
import Alert from "@/components/util/Alert.vue";
import Footer from "@/components/util/Footer.vue";
import Header from "@/components/util/Header.vue";

export default {
  name: "Top",
  computed: {
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    },
    overlayState() {
      return this.$store.getters.overlayState;
    },
  },
  components: {
    CommonOverlay,
    LeftMenu,
    TimeLine,
    RightMenu,
    Alert,
    Footer,
    Header,
  },
  mounted() {
    window.onload = () => {
      this.$store.dispatch("invisiblePostForm");
      this.$store.dispatch("invisibleCommonOverlay");
      this.$store.dispatch("toTimeLine");
    };
  },
  methods: {
    logIn: function () {
      this.$router.push("/login");
    },
  },
};
</script>
