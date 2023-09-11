<template>
    <div class="container mx-auto max-w-screen-xl max-h-screen ">
      <PageHeader 
        username="yoda"
        firstName="Yoda"
        lastName="Minch"
        profilePicture="https://avatars.githubusercontent.com/u/1862395?v=4"
      />
      <div class="flex shadow-2xl">
        <SideBar />
        <main class="py-8 px-8 w-screen">
          <div class="flex flex-col">
            <slot />
          </div>
        </main>
      </div>
    </div>
</template>