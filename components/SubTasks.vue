<template>
  <div>
    <label class="label space-x-1">
      <span class="text-base label-text uppercase font-normal">sub tarefas:</span>
    </label>
    <div>
      <TaskProgressBar :show-progress-bar="true" :total-tasks="totalSubTasks" :total-tasks-done="totalSubTasksDone" />
      <ul>
        <li v-for="subtask in subtasks" class="flex justify-between items-center mt-1 w-full p-2 hover:bg-base-200"
          @click.stop="updateSubTask(subtask.id)">
          <input type="checkbox" class="checkbox checkbox-md checkbox-success" :checked="subtask.done"
            @click.self="updateSubTask(subtask.id)" />
          <p class="w-full ml-2 font-semibold" :class="subtask.done ? 'line-through' : ''">
            {{ subtask.title }}
          </p>
          <div class="text-lg text-error font-semibold hover:bg-error hover:text-base-100"
            @click.stop="removeSubTask(subtask.id)">
            <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
        </li>
      </ul>
    </div>
    <input type="title" id="title" ref="newSubTaskTitleInput" v-model="newSubTaskTitle"
      @keydown.enter.exact.prevent="addSubTask" placeholder="Adicionar uma sub tarefa..."
      class="input input-bordered input-primary w-full mt-2 font-semibold" />
  </div>
</template>
  
<script setup>
const props = defineProps({
  taskId: {
    type: String,
    required: true
  },

  subtasks: {
    type: Array,
    required: true
  },

  totalSubTasks: {
    type: Number,
    required: true
  },

  totalSubTasksDone: {
    type: Number,
    required: true
  },

})

const ADD_SUBTASK_MUTATION = gql`
  mutation addSubTask ($title: String!, $taskId: ID!) {
    addSubTask(
      title: $title
      taskId: $taskId
    )
    {
      id
    }
  }  
  `
const MARK_SUBTASK_MUTATION = gql`
  mutation markSubTaskDone($subTaskId: ID!) {
    markSubTaskDone(
      subTaskId: $subTaskId
    )
    {
      id
    }
  }  
  `

const REMOVE_SUBTASK_MUTATION = gql`
  mutation deleteSubTask($subTaskId: ID!) {
    deleteSubTask(subTaskId: $subTaskId) { id }
  } 
  `
const emit = defineEmits(['updateTask'])

const newSubTaskTitle = ref('')
const newSubTaskTitleInput = ref(null)

const { mutate: addSubTaskMutation } = useMutation(ADD_SUBTASK_MUTATION)
const { mutate: markSubTaskMutation } = useMutation(MARK_SUBTASK_MUTATION)
const { mutate: removeSubTaskMutation } = useMutation(REMOVE_SUBTASK_MUTATION)

const addSubTask = async () => {
  if (newSubTaskTitle.value.trim().length > 0) {
    const res = await addSubTaskMutation({
      title: newSubTaskTitle.value.trim(),
      taskId: props.taskId
    })
    emit('updateTask', res.id)
    newSubTaskTitle.value = ''
  }
}

const updateSubTask = async (id) => {
  const res = await markSubTaskMutation({
    subTaskId: id,
  })
  emit('updateTask', res.id)
}


const removeSubTask = async (id) => {
  const res = await removeSubTaskMutation({
    subTaskId: id,
  })

  emit('updateTask', res.id)
}

onMounted(() => {
  nextTick(() => newSubTaskTitleInput.value.focus())
})

</script>