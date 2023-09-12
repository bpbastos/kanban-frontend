import { storeToRefs } from 'pinia';
import { useUserStore } from '~/store/user';

export default defineNuxtRouteMiddleware((to, from) => {
    const { setAuthenticated } = useUserStore(); 
    const token = useCookie('token'); // get token from cookies
  
    if (token.value) {
      // check if value exists
      setAuthenticated(true); // update the state to authenticated
    }
  
    // if token exists and url is /signin or /sign redirect to homepage
    if ((token.value && to?.name === 'signin') || (token.value && to?.name === 'signup')) {
      return navigateTo('/board');
    }

    // if token doesn't exist redirect to log in
    if (!token.value && to?.name !== 'signin' && !token.value && to?.name !== 'signup') {
      abortNavigation();
      return navigateTo('/signin');
    }
})