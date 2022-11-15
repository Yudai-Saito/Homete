<template>
  <v-col class="rightMenu">
    <div class="postBtn" @click="clickPost">
      <button class="postBtnTxt"><v-icon>mdi-pen-plus</v-icon>投稿する</button>
    </div>
    <div class="ruleBtn">
      <button class="ruleBtnTxt">利用規約</button>
    </div>
  </v-col>
</template>
<style>
.rightMenu {
  display: flex;
  flex-flow: column;
  height: 100vh;
  min-height: 100vh;
  max-height: 100vh;
  margin: 0;
  padding: 0;
}
.postBtn {
  margin-left: auto;
  margin-top: 60vh;
  text-align: center;
  width: 175px;
  height: 75px;
  border-radius: 30px;
  background-color: #cfd8dc;
  box-shadow: 1px 3px 2px 1px rgba(0, 0, 0, 0.3);
}
.postBtnTxt {
  font-size: 18px;
  line-height: 75px;
}
.ruleBtn {
  margin-left: auto;
  margin-top: 15vh;
  text-align: center;
  width: 105px;
  height: 20px;
  border-radius: 30px;
  background-color: #cfd8dc;
  box-shadow: 1px 3px 2px 1px rgba(0, 0, 0, 0.3);
}
.ruleBtnTxt {
  font-size: 12px;
  line-height: 20px;
}
</style>

<script>
export default {
  name: "RightMenu",
  computed: {
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    },
  },
  methods: {
    clickPost: function(){
      if(this.logged() == true){
        this.$store.dispatch("visiblePostForm");
      }
      else{
        //ログインを促すポップアップやオーバーレイ
      }
    },
  },
};
</script>
