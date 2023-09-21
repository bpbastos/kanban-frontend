# Dockerfile
FROM node:18.16.1-alpine

# create destination directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

# update and install dependency
RUN npm ci && npm cache clean --force
RUN npm run build

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

EXPOSE 3000 

ENTRYPOINT ["node", ".output/server/index.mjs"]