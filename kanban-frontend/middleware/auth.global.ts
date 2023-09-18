import { useUserStore } from '~/store/user';

export default defineNuxtRouteMiddleware((to, from) => {
    const { user } = useUserStore(); 
    
    if ((user.authenticated && to?.name === 'signin') || (user.authenticated && to?.name === 'signup')) {
      return navigateTo('/board');
    }

    if (!user.authenticated && to?.name !== 'signin' && !user.authenticated && to?.name !== 'signup') {
      abortNavigation();
      return navigateTo('/signin');
    }
})