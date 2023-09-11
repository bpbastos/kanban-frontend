// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@tailvue/nuxt'
  ],  
  runtimeConfig: {
    public: {
      NUXT_SECRET: process.env.NUXT_SECRET,
      BACK4APP_URL: process.env.BACK4APP_URL,
      BACK4APP_APPID: process.env.BACK4APP_APPID,
      BACK4APP_RESTAPIKEY: process.env.BACK4APP_RESTAPIKEY
    }
  },
})
