<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import {
  getAuth,
  GoogleAuthProvider,
  signInWithRedirect,
  onAuthStateChanged,
  getIdToken,
} from "firebase/auth";

import axios from "axios";

export default {
  name: "LoginLoading",
  computed: {
    logged() {
      return this.$store.getters.logged;
    },
  },
  data() {
    return {
      message: "Login",
    };
  },
  created() {
    const auth = getAuth();

    onAuthStateChanged(auth, (user) => {
      if (user) {
        const { currentUser } = getAuth();
        getIdToken(currentUser, true).then((token) => {
          axios
            .get("/account/login", {
              headers: {
                Authorization: `${token}`,
              },
              withCredentials: true,
            })
            .then(() => {
              this.$store.dispatch("loggedIn");
              this.$store.dispatch("invisibleLogin");
              this.message = "Success!";
            })
            .catch(() => {
              this.$store.dispatch("loggedOut");
              this.message = "Error!";
            });
        });
      } else {
        this.message = "Login…";
      }
    });
  },
  updated() {
    if (this.logged) {
      this.$router.push("/");
    }
    else {
      const auth = getAuth();
      const provider = new GoogleAuthProvider();

      provider.setCustomParameters({
        prompt: "select_account",
      });

      signInWithRedirect(auth, provider);
    }
  },
};
</script>
