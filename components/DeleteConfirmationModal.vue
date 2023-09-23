<template>
    <dialog ref="modal" class="modal">
        <form method="dialog" class="modal-box">
            <h3 class="font-bold text-lg">{{ title }}</h3>
            <p class="py-4">{{ message }}</p>
            <div class="modal-action">
                <!-- if there is a button in form, it will close the modal -->
                <button class="btn" @click="cancelAction">{{ btnCancelLabel }}</button>
                <button class="btn btn-error" @click="deleteAction">{{ btnDeleteLabel }}</button>
            </div>
        </form>
    </dialog>
</template>
<script setup>

const modal = ref(null)

const props = defineProps({
    title: String,
    message: String,
    btnDeleteLabel: String,
    btnCancelLabel: String,
    showModal: Boolean
})

const emit = defineEmits(['deleteClicked', 'cancelClicked'])

const deleteAction = () => {
    modal.value.close()
    emit('deleteClicked')
}

const cancelAction = () => {
    modal.value.close()
    emit('cancelClicked')
}

watch(
    () => props.showModal,
    () => {
        modal.value.showModal()
    }
)
</script>