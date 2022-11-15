<template>
  <v-container fluid>
    <v-card
      :loading="loading"
      :disabled="form || loading"
      outlined
      class="formTxtCard"
    >
      <v-btn icon plain @click="closeCard" class="my-1 ml-1">
        <v-icon color="black"> mdi-close </v-icon>
      </v-btn>
      <template slot="progress">
        <v-progress-linear
          color="#4169e1"
          height="5"
          indeterminate
        ></v-progress-linear>
      </template>
      <v-form v-model="isValid" ref="form">
        <v-btn
          icon
          plain
          @click="clearText"
          class="float-right mt-2 mr-2"
          v-show="detectInput"
        >
          <v-icon small color="glay"> mdi-close-circle </v-icon>
        </v-btn>
        <v-textarea
          label="なにを褒めてもらう？"
          solo
          flat
          auto-grow
          rows="3"
          v-model="formTxt"
          @input="inputText"
          counter="100"
          :rules="forms.inputRules"
        ></v-textarea>
        <v-divider class="mx-4"></v-divider>
        <v-card-actions>
          <v-btn
            :disabled="!isValid || loading"
            class="info ml-auto"
            @click="submit"
            elevation="0"
            rounded
          >
            投稿する
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>
<style>
.formTxtCard {
  position: sticky;
  width: 500px;
  bottom: 200px;
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
  },
};
</script>
