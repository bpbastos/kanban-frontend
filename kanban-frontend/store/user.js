import { defineStore } from "pinia";
import { useNotificationStore } from "@/store/notification";

export const useUserStore = defineStore("user", () => {
  const user = ref({
    id: "",
    username: "",
    profilePicture: "",
    token: "",
    authenticated: false
  });

  function destroy() {
    user.value.authenticated = false;
    user.value.id = "";
    user.value.username = "";
    user.value.email = "";
    user.value.profilePicture = "";
    user.value.token = ""; 
  }

  async function login(_username, _password) {
    const config = useRuntimeConfig().public;
    const notification = useNotificationStore();
    try {    
      const response = await $fetch(`${config.BACK4APP_URL}/login`, {
        method: "POST",
        body: JSON.stringify({
          username: _username,
          password: _password,
        }),
        headers: {
          "Content-Type": "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Revocable-Session": 1,
        },
      });

      if (response.objectId) {
        user.value.authenticated = true
        user.value.id = response.objectId;
        user.value.username = response.username;
        user.value.token = response.sessionToken;
        notification.success("User was successfully logged");
      } 
    } catch (e) {
      notification.error(e.data.error);
      destroy();
    }    
  }

  async function register(_username, _email, _password) {
    const config = useRuntimeConfig().public;
    const notification = useNotificationStore();
    try {
      const response = await $fetch(`${config.BACK4APP_URL}/users`, {
        method: "POST",
        body: JSON.stringify({
          username: _username,
          email: _email,
          password: _password,
        }),
        headers: {
          Accept: "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Revocable-Session": 1,
        },
      });

      if (response.objectId) {
        user.value.authenticated = true;
        user.value.id = response.objectId;
        user.value.token = response.sessionToken;
        notification.success("User successfully created");
      }
    } catch (e) {
      notification.error(e.data.error);
      destroy();
    }
  }

  async function logout() {
    const config = useRuntimeConfig().public;
    const notification = useNotificationStore();
    try {
      await $fetch(`${config.BACK4APP_URL}/logout`, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Session-Token": user.value.token,
          "X-Parse-Revocable-Session": 1,
        },
      });
      destroy();
    } catch (e) {
      notification.error(e.data.error);
      destroy();
    }
  }  

  return { user, register, login, logout }
}, {persist: true});
