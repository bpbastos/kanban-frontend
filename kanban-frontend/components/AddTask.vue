<template>
    <div class="flex flex-col w-full">
        <input type="text" placeholder="Insira um título para tarefa..." class="input input-primary input-md" maxlength="45"
            v-model="newTaskTitle" tabindex="0" ref="newTaskTitleInput" @keyup.enter="addNewTask"
            @keyup.esc="emit('canceled')" />
        <div class="flex text-sm mt-2 gap-1">
            <button class="btn btn-xs btn-success" @click="addNewTask">
                <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
            </button>
            <button class="btn btn-xs btn-error " @click="emit('canceled')">
                <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
    </div>
</template>
  
<script setup>

const CREATE_TASK_MUTATION = gql`
  mutation addNewTask ($title: String!, $workflowId: ID!) {
      addTask(
      title: $title
      workflowId: $workflowId
    ) 
    {
      id
    }
  }
`

const props = defineProps({
    workflowId: {
        type: String,
        required: true
    },
    boardId: {
        type: String,
        required: true
    }
})


const { mutate: addNewTaskMutation } = useMutation(CREATE_TASK_MUTATION)

const newTaskTitle = ref('')
const newTaskTitleInput = ref(null)

const emit = defineEmits(['added', 'canceled'])

const addNewTask = async () => {
    if (newTaskTitle.value.trim()) {
        const res = await addNewTaskMutation({
            title: newTaskTitle.value.trim(),
            workflowId: props.workflowId
        })
        if (res) {
            emit('added', res.id)
            newTaskTitle.value = ""
        }
    }
}

//Focus the input as soon as DOM el is shown
onUpdated(() => {
    nextTick(() => {
        newTaskTitleInput.value.focus()
    });
})

</script>