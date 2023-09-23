import { defineStore } from "pinia";
import { useNotificationStore } from "@/store/notification";

export const useUserStore = defineStore(
  "user",
  () => {
    const user = ref({
      id: "",
      username: "",
      profilePicture: "",
      token: "",
      authenticated: false,
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
      const notification = useNotificationStore();

      const response = await $fetch("/api/signin", {
        method: "POST",
        body: JSON.stringify({
          username: _username,
          password: _password,
        }),
      });
      
      if (!response.error) {
        user.value.id = response.id;
        user.value.username = response.username;
        user.value.profilePicture = response.profilePicture;
        user.value.token = response.token;
        user.value.authenticated = response.authenticated;
        notification.success("User was successfully logged");
        return true;
      } else {
        notification.error(response.error);
        destroy();
        return false;
      }
    }

    async function register(_username, _email, _password) {
      const notification = useNotificationStore();

      const response = await $fetch("/api/signup", {
        method: "POST",
        body: JSON.stringify({
          username: _username,
          email: _email,
          password: _password,
        }),
      });

      if (!response.error) {
        user.value = response;
        notification.success("User successfully created");
        return true;
      } else {
        notification.error(response.error);
        destroy();
        return false;
      }
    }

    async function logout() {
      const notification = useNotificationStore();
      await $fetch("/api/signout", { 
        method: "POST",
        body: JSON.stringify({
          token: user.token
        }),
      });
      notification.success("User successfully logged off");
      destroy();
      return true;
    }

    return { user, register, login, logout, destroy };
  },
  { persist: true }
);
