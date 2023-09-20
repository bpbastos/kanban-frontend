<template>
    <div class="h-screen flex items-center justify-center">
        <div class="card w-96 shadow-xl">
            <div class="card-body">
                <h1 class="text-3xl font-semibold text-center text-gray-700">Kanban App</h1>
                <div class="divider">Login</div>
                <div>
                    <div v-if="error" class="alert alert-error">
                        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>{{ error.text }}</span>
                    </div>                    
                    <form class="space-y-4" @submit.prevent="signIn">
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Username</span>
                            </label>
                            <input v-model="username"  type="text" placeholder="Informe o Username"
                                class="input input-bordered input-primary w-full max-w-xs" />
                        </div>
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Senha</span>
                            </label>
                            <input v-model="password" type="password" placeholder="Informe a Senha"
                                class="input input-bordered input-primary w-full max-w-xs" />
                        </div>
                        <div class="divider"></div>
                        <div>
                            <button class="btn btn-primary w-full">Entrar</button>
                        </div>
                        <div class="divider">OU</div>
                        <div class="flex justify-center">
                            <NuxtLink to="/signup">
                                <span class="text-blue-700 font-medium text-center w-full">Cadastre-se</span>
                            </NuxtLink>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>  
<script setup>
import { useUserStore } from '@/store/user';
import { useNotificationStore } from '@/store/notification';

const { login } = useUserStore();
const { getLastNotification } = useNotificationStore();

const password = ref('')
const username = ref('')
const error = ref('')

const signIn = async () => {
    const success = await login(username.value, password.value)

    if (success) {
        await navigateTo('/board')
    } else {
       error.value = getLastNotification()
    }
}

definePageMeta({
    layout: "empty"
});
</script>