<template>
  <v-card
    :loading="loading"
    :disabled="loading"
    outlined
    id="formTxtCard"
    class="rounded-xl"
  >
    <div
      v-show="!logged"
      style="height: 100%; width: 100%; position: absolute; z-index: 999"
      @click.stop="plzLogin"
    ></div>
    <template slot="progress">
      <v-progress-linear
        color="#4169e1"
        height="5"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-form id="formArea" v-model="isValid" ref="forms">
      <v-textarea
        id="mdPostForm"
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
      <label id="ECM_CheckboxInput"
        ><input
          id="ECM_CheckboxInput-Input"
          type="checkbox"
          value="true"
          v-model="private_posts"
        /><span id="ECM_CheckboxInput-DummyInput"></span
        ><span id="ECM_CheckboxInput-LabelText"
          >リアクションを見せない</span
        ></label
      >
      <v-card-actions>
        <v-btn
          id="postBtn"
          class="ml-auto mt-auto mb-1 mr-1"
          :disabled="!isValid || loading"
          @click="submit"
          elevation="0"
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
<style lang="scss">
@media (max-width: map-get($grid-breakpoints, md)) {
  #formArea .v-textarea {
    height: 250px;
  }
  #formArea .v-textarea .v-input__control .v-input__slot {
    height: 220px;
  }
  #formArea
    .v-textarea
    .v-input__control
    .v-input__slot
    .v-text-field__slot
    textarea {
    height: 200px !important;
  }
}
#formTxtCard {
  display: flex;
  width: 100%;
  margin: auto 12px;
  padding: 0;
  overflow: hidden;
  border: solid rgba(0, 0, 0, 0.25) 1px !important;
}
#formArea {
  margin: auto 0;
  padding: 0;
  height: 100%;
  width: 100%;
}
.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)
  > .v-input__control
  > .v-input__slot {
  padding: 0 !important;
}
.v-application--is-ltr .v-textarea.v-text-field--enclosed .v-text-field__slot {
  margin: 0 !important;
}
.v-textarea label {
  margin-left: 15px !important;
}
.v-textarea textarea {
  margin: 0 !important;
  margin: 15px !important;
  margin-bottom: 0 !important;
  padding: 0 !important;
  height: 40vh !important;
}
#postBtn {
  width: 60% !important;
  border-radius: 20px !important;
  font-size: 18px !important;
  border: solid rgba(0, 0, 0, 0.1) 1px !important;
}
#postBtn span {
  color: #494854 0.75;
}

/* 以下チェックボックスのスタイル */
#ECM_CheckboxInput {
  padding: 8px;
  padding-bottom: 0;
  display: flex;
  align-items: center;
  cursor: pointer;
}
#ECM_CheckboxInput-Input {
  margin: 0;
  width: 0;
  opacity: 0;
}
#ECM_CheckboxInput:hover > #ECM_CheckboxInput-DummyInput {
  background: #dddddd !important;
  border: solid 1px rgba(0, 0, 0, 0.5);
}
#ECM_CheckboxInput-Input:focus + #ECM_CheckboxInput-DummyInput {
  background: #dddddd !important;
  border: solid 1px rgba(0, 0, 0, 0.5);
}
#ECM_CheckboxInput-Input:checked + #ECM_CheckboxInput-DummyInput {
  border: solid 1px rgba(0, 0, 0, 0.25);
  background: #ffffff;
}
#ECM_CheckboxInput-Input:checked + #ECM_CheckboxInput-DummyInput::before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJmZWF0aGVyIGZlYXRoZXItY2hlY2siPjxwb2x5bGluZSBwb2ludHM9IjIwIDYgOSAxNyA0IDEyIj48L3BvbHlsaW5lPjwvc3ZnPg==")
    no-repeat center;
  background-size: contain;
}
#ECM_CheckboxInput-DummyInput {
  position: relative;
  top: 0;
  left: 0;
  display: block;
  width: 16px;
  min-width: 16px;
  height: 16px;
  min-height: 16px;
  border: solid 1px rgba(0, 0, 0, 0.25);
  background: #ffffff;
  border-radius: 4px;
}
#ECM_CheckboxInput-LabelText {
  margin-left: 4px;
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
      private_posts: false,
    };
  },
  computed: {
    forms() {
      const required = (v) => !!v || "";
      const inputFormat = (v) =>
        v.length <= 400 || "400文字以下で入力してください!";

      const inputRules = [required, inputFormat];

      return { inputRules };
    },
    displayPostForm() {
      return this.$store.getters.displayPostForm;
    },
    logged() {
      return this.$store.getters.logged;
    },
  },
  methods: {
    submit: function () {
      this.loading = true;

      axios
        .post(
          "/posts",
          {
            contents: this.formTxt,
            private: this.private_posts,
          },
          {
            withCredentials: true,
          }
        )
        .then((res) => {
          //ユーザーが投稿したデータを受け取ってupdatePostsに追加していく
          this.$store.commit("addUserUpdatePosts", res.data.user_posts);

          //スマホ用に投稿用コンポーネントの非表示
          this.$store.dispatch("invisiblePostForm");
          this.$store.dispatch("alertPostSuccess");
        })
        .catch(() => {
          this.$store.dispatch("alertError");
        });
      this.loading = false;
      this.formTxt = "";
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
    plzLogin: function () {
      this.$store.dispatch("visiblePlzLoginOverlay");
    },
  },
};
</script>
