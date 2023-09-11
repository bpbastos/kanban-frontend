<template>
    <div class="h-screen flex items-center justify-center">
        <div class="card w-96 bg-primary-content shadow-xl">
            <div class="card-body justify-center">
                <h1 class="text-3xl font-semibold text-center text-gray-700">Kanban App</h1>
                <div class="divider">Cadastre-se</div>
                <div>
                    <form class="space-y-4">
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Username</span>
                            </label>
                            <input type="text" placeholder="Escolha seu username" class="input input-bordered input-primary w-full max-w-xs" />
                        </div>                        
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Email</span>
                            </label>
                            <input type="text" placeholder="Informe seu email" class="input input-bordered input-primary w-full max-w-xs" />
                        </div>
                        <div>
                            <label class="label">
                                <span class="text-base label-text">Senha</span>
                            </label>
                            <input type="password" placeholder="Defina sua senha" class="input input-bordered input-primary w-full max-w-xs" />
                        </div>
                        <div class="divider"></div>
                       <div>
                            <button class="btn btn-primary w-full">Cadastre-se</button>
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