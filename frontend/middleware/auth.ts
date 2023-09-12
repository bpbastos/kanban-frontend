// middleware/auth.ts
export default defineNuxtRouteMiddleware((to, from) => {
    console.log('From auth middleware')
})