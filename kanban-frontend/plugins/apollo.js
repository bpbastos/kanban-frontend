import { useUserStore } from "@/store/user";
import { createHttpLink, from, InMemoryCache, ApolloClient } from '@apollo/client/core';
import { setContext } from '@apollo/client/link/context'
import { provideApolloClient } from '@vue/apollo-composable'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig();
  const { user } = useUserStore();

  const httpLink = createHttpLink({
    uri: config.public.KANBANDATA_URL,
  });

  // authentication headers
  const authLink = setContext(async (_, { headers }) => {
    return {
      headers: {
        ...headers,
        'X-User-Id': 's8OfY9OBAE'/*user.id* testando ...*/
      },
    };
  });

  // Cache implementation
  const cache = new InMemoryCache();

  // Create the apollo client
  const apolloClient = new ApolloClient({
    link: from([authLink, httpLink]),
    cache,
  });

  provideApolloClient(apolloClient);

  nuxtApp._apolloClients.default = apolloClient
});
