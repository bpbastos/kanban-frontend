<template>
  <details class="dropdown" ref="dropdown">
    <summary tabindex="0" class="btn btn-active bg-base-200 m-1 text-lg hover:bg-base-100">
      {{ selectedItem }}
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
        class="w-7 h-7 rounded-full drop-shadow-2xl bg-base-100 text-primary">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
      </svg>
    </summary>
    <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-200 rounded-box text-base">
      <li>
        <a v-for="board in boards" @click="changeSelected(board.id, board.name)">{{ board.name }}</a>
      </li>
    </ul>
  </details>
</template>
<script setup>
const props = defineProps({
  currentBoardId: {
    type: String,
    required: false
  },
})

const selectedItem = ref('')
const dropdown = ref(null)
const emit = defineEmits(['change', 'loaded'])
const router = useRouter()

const BOARDS_QUERY = gql`
    query getBoards {
        boards {
            ... on Board {
                id
                name
            }
        }
    }
  `

const { data } = useAsyncQuery(BOARDS_QUERY)

const boards = computed(() => {
  const _boards = []
  data.value?.boards?.map((b) => {
    if (props.currentBoardId==b.id) {
      selectedItem.value = b.name
    }
    _boards.push(b)
  })

  if (!props.currentBoardId)
    selectedItem.value = _boards[0]?.name ?? 'Nenhum quadro encontrado'
  
  return _boards
})


const closeDropdown = () => {
  if (dropdown.value.open)
    dropdown.value.removeAttribute('open')
}

const changeSelected = (boardId, boardName) => {
  selectedItem.value = boardName
  closeDropdown()
  emit('change', boardId)
}

onClickOutside(dropdown, (event) => {
  closeDropdown()
})

</script>