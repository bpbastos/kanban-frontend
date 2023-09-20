<template>
    <div>
      <div class="flex items-center gap-2 pb-8">
        <BoardSwitcher :key="boardSwitcherUpdate" @change="changeBoard" />
        <div class="flex flex-row w-4/12">
          <AddNewBoard :show="showAddBoardForm" @canceled="showAddBoardForm = false" @added="addedNewBoard" />
          <button class="btn btn-primary" @click.stop="showAddBoardForm = !showAddBoardForm" v-if="!showAddBoardForm">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
              class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
            </svg>
          </button>
        </div>
      </div>
      <div class="flex flex-wrap justify-strech gap-3 pb-8">
        <!-- To pass the tailwind color classes via v-bind it's needed to put the classes on safelist in tailwind.config.js file -->
        <WorkflowCard v-for="workflow in workflows" :workflow="workflow" :board-id="board.id" :key="workflow.id"
          @update-tasks="refetch()" />
      </div>
    </div>
  </template>
  <script setup>
  
  const showAddBoardForm = ref(false)
  const boardSwitcherUpdate = ref(0)
  
  const BOARD_QUERY = gql`
      query getBoard ($id: ID!) {
        board(id: $id) {
          id
          name
          workflows {
            ...on Workflow {
              id
              color
              name
              tasks {
                ...on Task {
                  id
                  title
                  totalSubTasks
                  totalSubTasksDone                
                  priority {
                    name
                    color
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
            }
          }
        }
      }
  `
  
  const route = useRoute()

  const boardId = ref(route.params.id ?? "")
    
  const { result, refetch } = useQuery(BOARD_QUERY, () => ({ id: boardId.value }))
  
  const board = computed(() => {
    return result.value?.board ?? null
  })
  
  const workflows = computed(() => {
    return result.value?.board?.workflows ?? []
  })
  
  const addedNewBoard = () => {
    boardSwitcherUpdate.value++;
    showAddBoardForm.value = false;
  }
  
  const changeBoard = (_boardId) => {
    boardId.value = _boardId
  }
  
  definePageMeta({
    layout: "default",
  });

  onMounted(()=>{
      refetch()
  })
  </script>