<template>
    <div v-if="result">
        <label class="label space-x-1">
            <span class="text-base label-text uppercase font-normal">PRIORIDADE:</span>
        </label>
        <div v-for="priority in priorities" :key="priority.id" class="tooltip" :class="`tooltip-${priority.color}`"
            :data-tip="`${priority.name}`">
            <input v-if="priority.id == selectedPriorityId" @click="changePriority(priority.id)" type="radio"
                :value="priority.id" name="priority" id="priority" class="radio radio-sm m-1"
                :class="`radio-${priority.color}`" checked />

            <input v-else-if="priority.id != selectedPriorityId" @click="changePriority(priority.id)" type="radio"
                :value="priority.id" name="priority" id="priority" class="radio radio-sm m-1"
                :class="`radio-${priority.color}`" />
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    selectedPriorityId: String
})

const emit = defineEmits(['change'])

const PRIORITIRES_QUERY = gql`
query getPriority {
    priorities {
        id
        name
        color
    }
}
`

const { result } = useQuery(PRIORITIRES_QUERY)

const priorities = computed(() => result.value.priorities)

const changePriority = (id) => {
    emit('change', id)
}
</script>