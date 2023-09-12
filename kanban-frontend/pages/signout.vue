<script setup>
import { useUserStore } from '@/store/user';

const user = useUserStore();

user.logout();

console.log(user.token)

await navigateTo('/signin')

definePageMeta({
    layout: "empty"
});
</script>