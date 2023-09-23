// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/color-mode',
    '@pinia/nuxt',
    '@pinia-plugin-persistedstate/nuxt',
    '@vueuse/nuxt',
    '@nuxtjs/apollo'
  ], 
  colorMode: {
    preference: 'corporate', // default theme
    dataValue: 'theme', // activate data-theme in <html> tag
  },  
  piniaPersistedstate: {
    cookieOptions: {
      sameSite: 'strict',
    },
    storage: 'cookies'
  }, 
  build: {
    transpile: [
      'pinia-plugin-persistedstate',
      'tslib'
    ]
  },    
  apollo: {
    clients: {
      default: {
        httpEndpoint: "http://localhost:8000/graphql",
      }
    },
  }, 
  runtimeConfig: {
    NUXT_SECRET: process.env.NUXT_SECRET,
    BACK4APP_URL: process.env.BACK4APP_URL,
    BACK4APP_APPID: process.env.BACK4APP_APPID,
    BACK4APP_RESTAPIKEY: process.env.BACK4APP_RESTAPIKEY,
    public: {
      KANBANDATA_URL: process.env.KANBANDATA_URL
    }
  },
  vite: {
    server: {
      hmr: {
        protocol: 'ws',
        host: 'localhost'
      }
    }
  } 
})
