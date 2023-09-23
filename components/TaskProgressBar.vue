<template>
    <div class="flex justify-stretch items-center space-x-1 m-2" v-show="totalTasks > 0">
        <div class="badge badge-md font-semibold" :class="totalTasks == totalTasksDone ? 'badge-success' : 'badge-info'">
            <svg class="fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="19">
                <path fill="none" d="M0 0h24v24H0z"></path>
                <path
                    d="M4 3h16a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm1 2v14h14V5H5zm6.003 11L6.76 11.757l1.414-1.414 2.829 2.829 5.656-5.657 1.415 1.414L11.003 16z">
                </path>
            </svg>
            <p class="tracking-wider">{{ totalTasksDone }}/{{ totalTasks }}</p>
        </div>
        <progress v-if="showProgressBar" class="progress shadow-2xl"
            :class="totalTasks == totalTasksDone ? 'progress-success' : 'progress-info'" :value="totalTasksDone"
            :max="totalTasks"></progress>
    </div>
</template>
  
<script setup>
const props = defineProps({
    totalTasks: Number,
    totalTasksDone: Number,
    showProgressBar: Boolean,
    showBadge: Boolean
})
</script>