// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/ui'],
  build: {
    transpile: ["@vuepic/vue-datepicker"],
  },
  colorMode: {
    preference: 'light'
  }
})