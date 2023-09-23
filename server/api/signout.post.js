export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const body = await readBody(event);
  try {
    const response = await $fetch(`${config.BACK4APP_URL}/logout`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Parse-Application-Id": config.BACK4APP_APPID,
        "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
        "X-Parse-Session-Token": body.token,
        "X-Parse-Revocable-Session": 1,
      },
    });
    if (!response.error) {
      return {
        success: true
      };
    }
    return {
      code: e.data.code,
      error: e.data.error
    };
  } catch (e) {
    return {
      code: e.data.code,
      error: e.data.error,
    };
  }
});
