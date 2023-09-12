import { defineStore } from "pinia";
import { useNotificationStore } from "@/store/notification";

export const useUserStore = defineStore("user", () => {
  const user = ref({
    id: "",
    username: "",
    firstName: "",
    lastName: "",
    occupation: "",
    biografy: "",
    status: "",
    memberSince: "",
    birthday: "",
    gender: "",
    mobile: "",
    address: "",
    email: "",
    profilePicture: "",
    token: "",
  });

  async function login(_username, _password) {
    const config = useRuntimeConfig().public;
    const notification = useNotificationStore();
    try {    
      const response = await $fetch(`${config.BACK4APP_URL}/login`, {
        method: "POST",
        body: {
          username: _username,
          password: _password,
        },
        headers: {
          "Content-Type": "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Revocable-Session": 1,
        },
      });

      if (response.objectId) {
        const token = useCookie("token");
        token.value = response.sessionToken;
        this.user.id = response.objectId;
        this.user.username = response.username;
        this.user.token = response.sessionToken;
        notification.success("User was successfully logged");
      } 
    } catch (e) {
      notification.error(e.data.error);
    }    
  }

  async function register(_username, _email, _password) {
    const config = useRuntimeConfig().public;
    const notification = useNotificationStore();
    try {
      const response = await $fetch(`${config.BACK4APP_URL}/users`, {
        method: "POST",
        body: {
          username: _username,
          email: _email,
          password: _password,
        },
        headers: {
          Accept: "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Revocable-Session": 1,
        },
      });

      if (response.objectId) {
        const token = useCookie("token");
        token.value = response.sessionToken;
        this.user.id = response.objectId;
        this.user.token = response.sessionToken;
        notification.success("User successfully created");
      }
    } catch (e) {
      notification.error(e.data.error);
    }
  }

  async function logout() {
    const config = useRuntimeConfig().public;
    const notification = useNotificationStore();
    try {
      const response = await $fetch(`${config.BACK4APP_URL}/logout`, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Session-Token": this.sessionToken,
          "X-Parse-Revocable-Session": 1,
        },
      });
      this.clean();
    } catch (e) {
      notification.error(e.data.error);
    }
  }  

  function clean() {
    this.user.id = "";
    this.user.username = "";
    this.user.firstName = "";
    this.user.lastName = "";
    this.user.occupation = "";
    this.user.biografy = "";
    this.user.status = "";
    this.user.memberSince = "";
    this.user.birthday = "";
    this.user.gender = "";
    this.user.mobile = "";
    this.user.address = "";
    this.user.email = "";
    this.user.profilePicture = "";
    this.user.token = "";    
  }

  return { user, register, login, logout }
});
