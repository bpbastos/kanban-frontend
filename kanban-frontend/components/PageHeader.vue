<template>
  <div class="navbar min-h-0 bg-base-100 bg-gradient-to-r from-secondary from-0% via-primary via-100%">
    <div class="flex-1">
      <a class="btn btn-ghost rounded normal-case text-2xl text-primary-content">kanban</a>
    </div>
  <div class="flex-none gap-2">
    <div class="dropdown dropdown-end">
      <label tabindex="0" class="btn btn-ghost btn-circle avatar online">
        <div class="w-10 rounded-full">
          <img :src="profilePicture" />
        </div>
      </label>
      <ul tabindex="0" class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-primary rounded-sm w-16">
        <li>
          <a @click="logout()">Sair</a>
        </li>
      </ul>
    </div>
  </div>
</div>  
</template>
  
<script setup>
import { useUserStore } from '@/store/user';


const logout = async () => {
  const user = useUserStore();
  await user.logout()
  await navigateTo('/signin')
}


const props = defineProps({
  username: String,
  firstName: String,
  lastName: String,
  profilePicture: String
})
</script>