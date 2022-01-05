module.exports = {
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
