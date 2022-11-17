<template>
  <v-card
    :loading="loading"
		:disabled="form || loading"
    outlined
    class="formTxtCard rounded-xl"
  >
    <template slot="progress">
      <v-progress-linear
        color="#4169e1"
        height="5"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-form class="formArea" v-model="isValid" ref="forms">
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
      <label class="ECM_CheckboxInput"><input class="ECM_CheckboxInput-Input" type="checkbox"><span class="ECM_CheckboxInput-DummyInput"></span><span class="ECM_CheckboxInput-LabelText">この投稿についたリアクションをみんなに見せない</span></label>
      <v-card-actions>
      <v-btn
        class="mx-auto mt-auto mb-1"
        style="font-size: 8px;"
        @click="submit"
        elevation="0"
        rounded
        height="20px"
        color="#CFD8DC"
      >
        利用規約
      </v-btn>
      <v-btn
        class="mx-auto mt-auto mb-1"
        style="font-size: 16px;"
        :disabled="!isValid || loading"
        @click="submit"
        elevation="0"
        rounded
        height="50px"
        width="100px"
        color="#CFD8DC"
      >
        投稿する
      </v-btn>
      </v-card-actions>
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
  margin-top: 10px !important;
  margin-right: 5px !important;
  padding: 0 !important;
  height: 40vh !important;
}
/* 以下チェックボックスのスタイル */
.ECM_CheckboxInput {
  padding: 8px;
  padding-bottom: 0;
  display: flex;
  align-items: center;
  cursor: pointer;
}
.ECM_CheckboxInput-Input {
  margin: 0;
  width: 0;
  opacity: 0;
}
.ECM_CheckboxInput:hover > .ECM_CheckboxInput-DummyInput {
  background: #DDDDDD !important;
  border: solid 2px #333333;
}
.ECM_CheckboxInput-Input:focus + .ECM_CheckboxInput-DummyInput {
  background: #DDDDDD !important;
  border: solid 2px #333333;
}
.ECM_CheckboxInput-Input:checked + .ECM_CheckboxInput-DummyInput {
  border: solid 2px #333333;
  background: #FFFFFF;
}
.ECM_CheckboxInput-Input:checked + .ECM_CheckboxInput-DummyInput::before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJmZWF0aGVyIGZlYXRoZXItY2hlY2siPjxwb2x5bGluZSBwb2ludHM9IjIwIDYgOSAxNyA0IDEyIj48L3BvbHlsaW5lPjwvc3ZnPg==") no-repeat center;
  background-size: contain;
}
.ECM_CheckboxInput-DummyInput {
  position: relative;
  top: 0;
  left: 0;
  display: block;
  width: 16px;
  min-width: 16px;
  height: 16px;
  min-height: 16px;
  border: solid 2px #888888;
  background: #FFFFFF;
  border-radius: 4px;
}
.ECM_CheckboxInput-LabelText {
  margin-left: 8px;
  display: block;
  font-size: 10px;
  font-weight: bold;
  color: #494854;
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
    closeCard: function () {
      this.formTxt = "";
      this.detectInput = false;
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
        v.length <= 400 || "400文字以下で入力してください！";

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
