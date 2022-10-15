module.exports = {
    productionSourceMap: false,
    pages: {
        index: {
            entry: 'src/main.js',
            title: 'HOMETE',
        }
    },
    css: {
        loaderOptions: { 
            sass: {
                additionalData: `@import "./src/scss/variables.scss"`
            }
        }
    },
    transpileDependencies: [
        'vuetify'
    ]
}
