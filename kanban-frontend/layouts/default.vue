<template>
  <div class="container mx-auto max-w-screen-xl max-h-screen ">
    <PageHeader />
    <div class="flex shadow-2xl">
      <SideBar />
      <div class="py-8 px-8 w-screen">
        <div class="flex flex-col">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>