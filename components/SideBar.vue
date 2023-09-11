<template>
    <div class="">
      <div class="hidden sm:block">
        <aside
          class="flex flex-col w-[120px] min-h-screen flex-shrink-0 shadow-lg py-1"
        >
          <NuxtLink
            to="/board"
            class="flex flex-col items-center justify-center py-8 hover:bg-base-300"
            active-class="border-l-2 border-primary bg-base-200"

          >
            <i class="fa-solid fa-server text-primary"></i>
            <figcaption class="mt-2">Quadros</figcaption>
          </NuxtLink>
        </aside>
      </div>
    </div>
  </template>

  