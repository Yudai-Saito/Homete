module.exports = {
  productionSourceMap: false,
  pages: {
    index: {
      entry: "src/main.js",
      title: "HOMETE",
    },
  },
  transpileDependencies: ["vuetify"],
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.md$/,
          use: "raw-loader",
        },
      ],
    },
  },
};
