<template>
  <v-card
    outlined
    class="formTxtCard rounded-xl"
  >
    <v-btn v-show="!logged" icon plain @click="closeCard" class="my-1 ml-1">
      <v-icon color="black"> mdi-close </v-icon>
    </v-btn>

    <template slot="progress">
      <v-progress-linear
        color="#4169e1"
        height="5"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-form class="formArea" v-model="isValid" ref="forms">
      <v-btn
        icon
        plain
        @click="clearText"
        v-show="detectInput"
      >
        <v-icon small color="glay"> mdi-close-circle </v-icon>
      </v-btn>
      <v-textarea
        label="なにを褒めてもらう？"
        solo
        flat
        hide-details="auto"
        v-model="formTxt"
        @input="inputText"
        counter="400"
        :rules="forms.inputRules"
      ></v-textarea>
      <v-divider class="mx-4"></v-divider>
      <v-btn
        :disabled="!isValid || loading"
        class="info"
        @click="submit"
        elevation="0"
        rounded
      >
        投稿する
      </v-btn>
    </v-form>
  </v-card>
</template>
<style>
.formTxtCard {
  display: flex;
  width: 100%;
  margin: auto;
  padding: 0;
  overflow: hidden;
}
.formArea{
  margin: auto 0;
  padding: 0;
  height: 100%;
  width: 100%;
}
.v-textarea textarea {
  margin: 0 !important;
  padding: 0 !important;
  height: 40vh !important;
}
</style>

<script>
import axios from "axios";

export default {
  name: "PostForm",
  data() {
    return {
      isValid: false,
      loading: false,
      formTxt: "",
      detectInput: false,
    };
  },
  methods: {
    submit: function () {
      this.loading = true;

      axios
        .post(
          "/post",
          {
            post_content: this.formTxt,
          },
          {
            withCredentials: true,
          }
        )
        .then((res) => {
          console.log(res);
          this.$store.dispatch("invisiblePostForm");
          this.alertPost();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    inputText: function () {
      if (this.formTxt == "") {
        this.detectInput = false;
      } else {
        this.detectInput = true;
      }
    },
    clearText: function () {
      this.formTxt = "";
      this.detectInput = false;
    },
    closeCard: function () {
      this.$store.dispatch("invisiblePostForm");
    },
    alertPost: function () {
      this.$store.dispatch("alertPost");
    },
  },
  computed: {
    forms() {
      const required = (v) => !!v || "";
      const inputFormat = (v) =>
        v.length <= 100 || "100文字以下で入力してください！";

      const inputRules = [required, inputFormat];

      return { inputRules };
    },
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    }
  },
};
</script>
