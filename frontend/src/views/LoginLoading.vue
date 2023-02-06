<template>
  <div class="displayDiv">
    <div class="txtDiv">
      <div class="circle"></div>
      <div class="circle"></div>
      <div class="circle"></div>
      <div class="shadow"></div>
      <div class="shadow"></div>
      <div class="shadow"></div>
      <span
        v-show="isShow"
        v-for="(t, index) in message"
        :key="index"
        class="item"
        :style="{ animationDelay: index * 20 + 'ms' }"
        v-text="t"
      />
    </div>
  </div>
</template>

<style scoped>
.v-leave-active {
  transition: opacity 1.3s ease;
}
.displayDiv {
  padding: 0;
  margin: 0;
  width: 100vw;
  height: 100vh;
  background: radial-gradient(rgb(255, 248, 225), rgb(244, 227, 192));
  display: flex;
}
.txtDiv {
  width: 300px;
  height: 90px;
  position: relative;
  margin: auto;
  text-align: center;
}
.circle {
  width: 20px;
  height: 20px;
  position: absolute;
  border-radius: 50%;
  background-color: rgb(154, 159, 229);
  left: 15%;
  transform-origin: 50%;
  animation: circle 0.5s alternate infinite ease;
  z-index: 1;
}

@keyframes circle {
  0% {
    top: 60px;
    height: 5px;
    border-radius: 50px 50px 25px 25px;
    transform: scaleX(1.7);
  }
  40% {
    height: 20px;
    border-radius: 50%;
    transform: scaleX(1);
  }
  100% {
    top: 0%;
  }
}
.circle:nth-child(2) {
  left: 45%;
  animation-delay: 0.2s;
}
.circle:nth-child(3) {
  left: auto;
  right: 15%;
  animation-delay: 0.3s;
}
.shadow {
  width: 20px;
  height: 4px;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 62px;
  transform-origin: 50%;
  z-index: -1;
  left: 15%;
  filter: blur(1px);
  animation: shadow 0.5s alternate infinite ease;
  z-index: auto;
}

@keyframes shadow {
  0% {
    transform: scaleX(1.5);
  }
  40% {
    transform: scaleX(1);
    opacity: 0.7;
  }
  100% {
    transform: scaleX(0.2);
    opacity: 0.4;
  }
}
.shadow:nth-child(4) {
  left: 45%;
  animation-delay: 0.2s;
}
.shadow:nth-child(5) {
  left: auto;
  right: 15%;
  animation-delay: 0.3s;
}
.txtDiv span {
  position: relative;
  top: 85px;
  font-size: 25px;
  letter-spacing: 10px;
  color: rgb(154, 159, 229);
  font-weight: 500;
}
@keyframes text-in {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}
.item {
  display: inline-block;
  min-width: 0.3em;
  font-size: 2rem;
  animation: text-in 0.8s cubic-bezier(0.22, 0.15, 0.25, 1.43) 0s backwards;
}
</style>

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
      message: "Login…",
      isShow: true,
      isError: false,
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
              this.$store.commit("updateAlertState", "login");
              this.$store.dispatch("loggedIn");
              this.$store.dispatch("invisibleCommonOverlay");
              this.$store.dispatch("invisibleAlert");

              this.isShow = false;
              this.message = "Success!";

              setTimeout(() => {
                this.isShow = true;
              }, 50);
            })
            .catch(() => {
              this.$store.commit("updateAlertState", "error");
              this.$store.dispatch("loggedOut");
              this.$store.dispatch("invisibleCommonOverlay");
              this.$store.dispatch("invisibleAlert");

              this.isShow = false;
              this.isError = true;
              this.message = "Error!";

              setTimeout(() => {
                this.isShow = true;
              }, 50);
            });
        });
      } else {
        this.isShow = false;
        this.message = "Login";
        setTimeout(() => {
          this.isShow = true;
        }, 50);
      }
    });
  },
  updated() {
    if (this.logged && !this.isError) {
      this.$router.push("/home");
      setTimeout(() => {
        this.$store.dispatch("alertLogin");
      }, 500);
    } else if (!this.logged && !this.isError) {
      const auth = getAuth();
      const provider = new GoogleAuthProvider();

      provider.setCustomParameters({
        prompt: "select_account",
      });

      signInWithRedirect(auth, provider);
    } else {
      setTimeout(() => {
        this.$router.push("/home");
        setTimeout(() => {
          this.$store.dispatch("alertError");
        }, 500);
      }, 2500);
    }
  },
};
</script>
