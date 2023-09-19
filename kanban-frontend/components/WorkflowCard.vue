<template>
    <div class="card w-[265px] max-h-screen h-full pt-[3px]" :class="`bg-${workflow.color}-400`">
      <div class="card bg-base-200 overflow-auto scrollbar scrollbar-w-1 scrollbar-thumb-primary">
        <p class="card-title text-base-content text-lg font-medium m-3">{{ workflow.name }}</p>
        <div class="card-actions justify-center ml-2 mr-2">
            <!--TaskCard v-for="task in workflow.tasks" :task="task" @deleted="updateTasks"/>
            <AddTaskForm v-show="showForm" :workflow-id="workflow.id" :board-id="boardId" @added="updateTasks" @canceled="showForm = false" /-->
        </div>
        <div class="card-actions m-3">
          <a href="#" v-show="!showForm" @click="showForm = true"
            class="flex flex-row w-full items-center text-base-content font-semibold rounded hover:bg-base-100">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
              class="w-5 h-5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
            </svg>
            <p class="ml-2">Adicionar uma tarefa</p>
          </a>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  
  /*import TaskCard from '@/components/TaskCard.vue'
  import AddTaskForm from '@/components/AddTaskForm.vue'*/
  
  const props = defineProps({
    workflow: {
      type: Object,
      required: true
    },
    boardId: {
      type: String,
      required: true
    }
  })
  
  const emit = defineEmits(['updateTasks'])
  
  const showForm = ref(false)
  
  const updateTasks = async() => {
    showForm.value = false  
    emit('updateTasks')
  }
  
  </script>