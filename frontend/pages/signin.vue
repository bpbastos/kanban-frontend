<template>
    <div class="h-screen flex items-center justify-center">
        <div class="card w-96 bg-primary-content shadow-xl">
            <div class="card-body">
                <h1 class="text-3xl font-semibold text-center text-gray-700">Kanban App</h1>
                <div class="divider">Login</div>
                <div>
                    <form class="space-y-4">
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Username</span>
                            </label>
                            <input type="text" placeholder="Informe o Username"
                                class="input input-bordered input-primary w-full max-w-xs" />
                        </div>
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Senha</span>
                            </label>
                            <input type="password" placeholder="Informe a Senha"
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
// This will work in both `<script setup>` and `<script>`
definePageMeta({
    layout: "empty",
    auth: false
});
</script>