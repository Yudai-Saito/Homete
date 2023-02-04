const modulePath = process.env.FIREBASE_CONFIG;
eval(`import firebaseConfig from './${modulePath}';`);

export class Index {
  static init() {
    firebase.initializeApp(firebaseConfig);

    var ui = new firebaseui.auth.AuthUI(firebase.auth());

    // FirebaseUIの各種設定
    var uiConfig = {
      callbacks: {
        signInSuccessWithAuthResult: function () {
          firebase
            .auth()
            .currentUser.getIdToken(true)
            .then((idToken) => {
              axios
                .get("/auth", {
                  headers: {
                    Authorization: `${idToken}`,
                  },
                })
                .then(() => {
                  window.location.href = "/posts";
                })
                .catch(() => {
                  window.location.href = "/error";
                });
            });
          return false;
        },
        uiShown: function () {
          document.getElementById("loader").style.display = "none";
        },
      },
      signInOptions: [
        {
          provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
          customParameters: {
            prompt: "select_account",
          },
        },
      ],
      credentialHelper: firebaseui.auth.CredentialHelper.NONE,
    };
    ui.start("#firebaseui-auth-container", uiConfig);
  }
}
