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
            .post(
              "/account/login",
              {
                //ここJWTからとれるからGETでいいと思う
                email: user.email,
              },
              {
                headers: {
                  Authorization: `${token}`,
                },
                withCredentials: true,
              }
            )
            .then(() => {
              this.$store.dispatch("toTrueLogin");
              this.$store.dispatch("toInvisibleLoginWindow");
              this.message = "Success!";
            })
            .catch(() => {
              this.$store.dispatch("toFalseLogin");
              this.message = "Error!";
            });
        });
      } else {
        this.message = "Login…";
      }
    });
  },
  updated() {
    if (this.$store.getters.isLogin) {
      this.$router.push("/");
    } else {
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
