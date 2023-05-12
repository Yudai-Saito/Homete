<template>
  <v-btn
    id="sbMenuBtn"
    @click="onClickSpringBoardMenu"
    style="color: #494854"
    depressed
    plain
    color="#FFFFFF"
  >
    <v-icon v-if="icon == 'mdiAccountCog'">{{ mdiAccountCog }}</v-icon>
    <v-icon v-else-if="icon == 'mdiLoginVariant'">{{ mdiLoginVariant }}</v-icon>
    <v-icon v-else-if="icon == 'mdiInformationVariant'">{{
      mdiInformationVariant
    }}</v-icon>
    <v-icon v-else-if="icon == 'mdiChatQuestionOutline'">{{
      mdiChatQuestionOutline
    }}</v-icon>
    <v-icon v-else-if="icon == 'mdiShieldCheck'">{{ mdiShieldCheck }}</v-icon>
    <v-icon v-else>{{ mdiShieldKeyOutline }}</v-icon>
    {{ this.labelTxt }}
  </v-btn>
</template>

<style>
#sbMenuBtn {
  width: 100%;
  height: 49px;
  padding: 0 !important;
  font-weight: 600;
}
#sbMenuBtn .v-btn__content {
  opacity: 1 !important;
  color: #333;
  justify-content: flex-start;
}
#sbMenuBtn .v-btn__content i {
  margin-right: 5px;
}
</style>

<script>
import { mdiAccountCog } from "@mdi/js";
import { mdiLoginVariant } from "@mdi/js";
import { mdiInformationVariant } from "@mdi/js";
import { mdiChatQuestionOutline } from "@mdi/js";
import { mdiShieldCheck } from "@mdi/js";
import { mdiShieldKeyOutline } from "@mdi/js";

export default {
  name: "SpringBoardMenu",
  data() {
    return {
      mdiAccountCog,
      mdiLoginVariant,
      mdiInformationVariant,
      mdiChatQuestionOutline,
      mdiShieldCheck,
      mdiShieldKeyOutline,
    };
  },
  props: ["labelTxt", "icon", "onClickSpringBoardMenu"],
};
</script>
