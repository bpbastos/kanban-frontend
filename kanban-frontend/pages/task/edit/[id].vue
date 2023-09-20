<template>
  <div class="flex items-center justify-center w-12/12">
    <div class="card pt-[2px] bg-primary shadow-2xl w-full">
      <div class="card bg-base-200 p-4">
        <form action="form-control p-3" v-if="task">
          <div class="flex space-x-2 items-center">
            <div class="w-10/12">
              <label class="label">
                <span class="text-base label-text uppercase font-normal">TÍTULO</span>
              </label>
              <input v-model="taskTitle" type="text" placeholder="Título"
                class="w-full input input-bordered input-primary font-semibold" />
            </div>
            <div class="w-24">
              <PriorityRadioGroup :selected-priority-id="taskPriorityId" @change="changePriority" />
            </div>
          </div>
          <div class="flex space-x-2 items-start">
            <div class="w-10/12">
              <SubTasks :task-id="task.id" :subtasks="task.subtasks ?? []" :total-sub-tasks="task.totalSubTasks"
                :total-sub-tasks-done="task.totalSubTasksDone" :key="subTasksKey" @update-task="refetchTask()" />
            </div>
            <div class="w-36">
              <label class="label space-x-1">
                <span class="text-base label-text uppercase font-normal">WORKFLOW:</span>
              </label>
              <div class="badge w-full uppercase font-semibold p-3" :class="`bg-${workflowColor}`">
                {{ workflowName }}
              </div>
            </div>
          </div>
          <div class="flex space-x-2 items-start">
            <div class="w-10/12">
              <label class="label space-x-1">
                <span class="text-base label-text uppercase font-normal">DESCRIÇÃO:</span>
              </label>
              <textarea v-model="taskDescription" placeholder="Descrição"
                class="textarea textarea-primary textarea-md text-base w-full mt-2 font-semibold">
               </textarea>
            </div>
          </div>
          <div class="flex flex-col justify-end space-x-2 mt-2">
            <div>
              <div class="divider"></div>
            </div>
            <div class="flex justify-end space-x-2 mt-2">
              <button class="btn btn-neutral" @keydown.enter.exact.prevent=""
                @click.prevent="navigateTo(`/board/${task.workflow?.board?.id}`)">
                Cancelar
              </button>
              <button class="btn btn-primary" @keydown.enter.exact.prevent="" @click.prevent="updateTask">
                Salvar
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
 
<script setup>
const props = defineProps({
  id: String
})

const TASK_QUERY = gql`
   query getTask($id: ID!) {
     task(id:$id)
     {
      id
       title
       description
       totalSubTasks
       totalSubTasksDone
       workflow {
         ...on Workflow {
           id
           name
           color
           board {
           	...on Board {
              id
            }
        	 }
         }
       }
       priority {
         ...on Priority {
           id
           name
           color
         }
       }
       subtasks {
         ...on SubTask {
           id
           title
           order
           done
         }
       }
    }
  }
 `
const UPDATE_TASK_MUTATION = gql`
 mutation updateTask ($id: ID!, $title: String!, $description: String!, $priorityId: ID!) {
   updateTask(
     id: $id
     title: $title
     description: $description
     priorityId: $priorityId
   )
   { id }
 }  
 `
const route = useRoute()
const { result, refetch } = useQuery(TASK_QUERY, { id: route.params.id })
const { mutate: updateTaskMutation } = useMutation(UPDATE_TASK_MUTATION)

const subTasksKey = ref(0)
const taskTitle = ref('')
const taskDescription = ref('')
const taskPriorityId = ref('')

//Read-Only attrs
const task = computed(() => {
  taskTitle.value = result.value?.task?.title
  taskDescription.value = result.value?.task?.description
  taskPriorityId.value = result.value?.task?.priority?.id
  return result.value?.task
})

const workflowName = computed(() => result.value?.task?.workflow?.name)
const workflowColor = computed(() => result.value?.task?.workflow?.color)

const changePriority = (id) => {
  taskPriorityId.value = id
}

const refetchTask = async () => {
  await refetch()
  subTasksKey.value++
}

const updateTask = async () => {
  const res = await updateTaskMutation({
    id: task.value.id,
    title: taskTitle.value,
    description: taskDescription.value,
    priorityId: taskPriorityId.value
  })
  navigateTo(`/board/${task.value?.workflow?.board?.id}`)
}
</script>