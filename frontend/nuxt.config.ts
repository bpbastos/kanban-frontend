// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss'
  ],  
  runtimeConfig: {
    NUXT_SECRET: process.env.NUXT_SECRET,
    BACK4APP_URL: process.env.BACK4APP_URL,
    BACK4APP_APPID: process.env.BACK4APP_APPID,
    BACK4APP_RESTAPIKEY: process.env.BACK4APP_RESTAPIKEY,
  }
})
