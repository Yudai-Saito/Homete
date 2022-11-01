<template>
  <v-container fluid>
    <v-card
      :loading="loading"
      :disabled="form || loading"
      outlined
      class="hometeCard"
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
          v-show="isInputHomete"
        >
          <v-icon small color="glay"> mdi-close-circle </v-icon>
        </v-btn>
        <v-textarea
          label="なにを褒めてもらう？"
          solo
          flat
          auto-grow
          rows="3"
          v-model="homete"
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
.hometeCard {
  position: sticky;
  width: 500px;
  bottom: 200px;
}
</style>

<script>
import axios from "axios";

export default {
  name: "PostHomete",
  data() {
    return {
      isValid: false,
      form: false,
      loading: false,
      homete: "",
    };
  },
  methods: {
    submit: function () {
      this.loading = true;

      axios
        .post(
          "/post",
          {
            post_content: this.homete,
          },
          {
            withCredentials: true,
          }
        )
        .then((res) => {
          console.log(res);
          this.$store.dispatch("toInvisiblePostHomete");
          this.alertPostVisible();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    inputText: function () {
      if (this.homete == "") {
        this.$store.dispatch("toFalseInputHomete");
      }else{
        this.$store.dispatch("toTrueInputHomete");
      }
    },
    clearText: function () {
      this.homete = "";
      this.$store.dispatch("toFalseInputHomete");
    },
    closeCard: function () {
      this.$store.dispatch("toInvisiblePostHomete");
    },
    alertPostVisible: function () {
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
    isVisiblePostHomete(){
      return this.$store.getters.isVisiblePostHomete;
    },
    isInputHomete(){
      return this.$store.getters.isInputHomete;
    },
  },
};
</script>
