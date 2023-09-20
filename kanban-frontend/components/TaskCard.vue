<template>
    <div class="card card-compact glass w-full shadow-2xl bg-base-100 text-xs p-2 cursor-pointer" @click="goToEditTask">
        <div class="card-actions justify-between">
            <div class="badge badge-lg font-semibold justify-start" :class="priorityColor">
                {{ priorityLabel }}
            </div>
            <button class="btn btn-xs btn-square btn-error cursor-not-allowed" @click.stop="showModal = !showModal">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
        <div>
            <p class="card-actions text-base text-base-content p-2">{{ task.title }}</p>
            <TaskProgressBar class=" ml-0 mt-0" :total-tasks="totalSubTasks" :total-tasks-done="totalSubTasksDone" />
        </div>
    </div>
    <DeleteConfirmationModal @delete-clicked="deleteTask" :show-modal="showModal" btn-cancel-label="Cancelar"
        btn-delete-label="Deletar" title="Deletar?" message="Deseja realmente deletar a tarefa?" />
</template>

<script setup>
const DELETE_TASK_MUTATION = gql`
mutation deleteTask ($id: ID!) {
    deleteTask( taskId: $id )  { id }
}
`
const { mutate: deleteTaskMutation } = useMutation(DELETE_TASK_MUTATION)

const props = defineProps({
    task: {
        type: Object,
        required: true
    }
})

const router = useRouter()
const showModal = ref(false)

const priorityLabel = computed(() => props.task.priority.name)
const priorityColor = computed(() => "badge-" + props.task.priority.color)
const totalSubTasks = computed(() => props.task.totalSubTasks)
const totalSubTasksDone = computed(() => props.task.totalSubTasksDone)

const emit = defineEmits(['deleted'])

const deleteTask = async () => {
    const deletedTask = await deleteTaskMutation({ id: props.task.id })
    if (deleteTask) {
        emit('deleted', deletedTask.id)
    }
}

const goToEditTask = () => {
    router.push({ name: 'EditTask', params: { id: props.task.id } })
}
</script>