<template>
    <div class="flex flex-row w-full gap-1" v-show="show">
        <div class="mr-3 w-full">
            <input type="text" placeholder="Insira um nome para o quadro..." class="input input-primary input-md w-full"
                maxlength="45" v-model="newBoardName" tabindex="0" ref="newBoardInput" />
        </div>
        <button class="btn btn-success" @click="addNewBoard">
            <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
            </svg>
        </button>
        <button class="btn btn-error " @click="emit('canceled')">
            <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
        </button>

    </div>
</template>
  
<script setup>
const newBoardName = ref('')
const newBoardInput = ref(null)

const CREATE_BOARD_MUTATION = gql`
mutation addNewBoard ($name: String!) {
    addBoard(
        board: {
            name: $name
            workflows:[
                {
                    color: "purple"
                    name: "Backlog"
                },
                {
                    color: "orange"
                    name: "Em andamento"
                },
                {
                    color: "blue"
                    name: "Em análise"
                },
                {
                    color: "green"
                    name: "Concluído"
                }
            ]            
        }    
    )
    {
  	 ...on AddBoardSuccess {
      id
    }
    ...on UserNotFound {
      code
      message
    }
  }
} 
`
const { mutate: addNewBoardMutation } = useMutation(CREATE_BOARD_MUTATION);    

const props = defineProps({
    show: Boolean
});

const emit = defineEmits(['added', 'canceled'])

const addNewBoard = async() => {
  if (newBoardName.value.trim()) {
    const res = await addNewBoardMutation({ 
      name: newBoardName.value.trim()
    })
    if (res) {
      emit('added', res.data?.addBoard?.id)
      newBoardName.value = ""   
    } 
  }    
}

//Focus the input as soon as DOM el is shown
onUpdated(() => {
    nextTick(() => {
        newBoardInput.value.focus()
    });
})
</script>