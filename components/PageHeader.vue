<template>
    <div class="navbar min-h-0 bg-base-100 bg-gradient-to-r from-secondary from-0% via-primary via-100%">
      <div class="flex-1">
        <a class="btn btn-ghost rounded normal-case text-2xl text-primary-content">kanban</a>
      </div>
      <div class="flex-none gap-2">
        <label tabindex="0" class="btn btn-ghost btn-circle avatar online">
          <div class="w-10 rounded-full">
              <img :src="profilePicture" />
          </div>
        </label>
      </div>
    </div>
  </template>
  
  <script setup>
   
  const props = defineProps({
    username: String,
    firstName: String,
    lastName: String,
    profilePicture: String
  })
  </script>