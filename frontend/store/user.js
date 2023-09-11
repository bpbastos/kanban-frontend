import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
 
  state: () => {
    return {
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
      token: ""
    };
  },
  actions: {
    async login({ _username, _password }) {
      const config = useRuntimeConfig();  
      console.log(useRuntimeConfig().BACK4APP_URL)        
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

      if (response.ok && response.objectId) {
        const token = useCookie("token");
        token.value = response.sessionToken;
        this.id = response.objectId;
        this.username = response.username;
        this.token = response.sessionToken;
      } else {

      }
    },
    async register(_username, _email, _password) {
      const config = useRuntimeConfig().public; 
      const response = await $fetch(`${config.BACK4APP_URL}/users`, {
        method: "POST",
        body: {
          username: _username,
          email: _email,
          password: _password
        },
        headers: {
          Accept: "application/json",
          "X-Parse-Application-Id": config.BACK4APP_APPID,
          "X-Parse-REST-API-Key": config.BACK4APP_RESTAPIKEY,
          "X-Parse-Revocable-Session": 1,
        },
      });

      if (response.ok && !response.error) {
        const token = useCookie("token");
        token.value = response.sessionToken;
        this.id = response.objectId;
        this.username = response.username;
        this.token = response.sessionToken;
      } else {
        $toast.show(response.error);       
      }
    },
  },
});
