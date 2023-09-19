import { useUserStore } from '~/store/user';

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const { user, destroy } = useUserStore(); 

  try {
    await $fetch(`${config.BACK4APP_URL}/logout`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "X-Parse-Application-Id": config.BACK4APP_APPID,
        "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
        "X-Parse-Session-Token": user.token,
        "X-Parse-Revocable-Session": 1,
      },
    });
    destroy();
    return {
      success: true
    };
  } catch (e) {
    return {
      code: error.data.code,
      error: error.data.error,
    };
  }
});
