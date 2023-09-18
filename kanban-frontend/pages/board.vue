<template>
  <div>
    <div class="pb-8">
      <BoardSwitcher />
    </div>
  </div>
</template>
<script setup>
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/store/user';

const { user } = storeToRefs(useUserStore())

definePageMeta({
    layout: "default",
});
</script>