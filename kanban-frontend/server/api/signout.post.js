export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const body = await readBody(event);
  try {
    await $fetch(`${config.BACK4APP_URL}/logout`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Parse-Application-Id": config.BACK4APP_APPID,
        "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
        "X-Parse-Session-Token": body.token,
        "X-Parse-Revocable-Session": 1,
      },
    });

    return {
      success: true
    };
  } catch (e) {
    return {
      code: e.data.code,
      error: e.data.error,
    };
  }
});
