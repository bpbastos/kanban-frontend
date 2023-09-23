export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const body = await readBody(event);

  try {
    const response = await $fetch(`${config.BACK4APP_URL}/login`, {
      method: "POST",
      body: JSON.stringify({
        username: body.username,
        password: body.password,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-Parse-Application-Id": config.BACK4APP_APPID,
        "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
        "X-Parse-Revocable-Session": 1,
      },
    });
    console.log("Response:",response)
    console.log("Config:",config)
    if (!response.error) {
      return {
        id: response.objectId,
        username: response.username,
        token: response.sessionToken,
        profilePicture: '/images/avatar.jpg',
        authenticated: true,
      };
    }
    return {
      code: response.code,
      error: response.error,      
      authenticated: false,
    };
  } catch (error) {
    return {
      code: error.data.code,
      error: error.data.error,
    };
  }

});
