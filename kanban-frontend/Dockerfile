# use node 16 alpine image
FROM node:18.16.1-slim

# create work directory in app folder
WORKDIR /app

# copy over package.json files
COPY package.json /app/
COPY package-lock.json /app/

# install all depencies
RUN npm ci && npm cache clean --force

# copy over all files to the work directory
ADD . /app

# build the project
RUN npm run build

# expose the host and port 3000 to the server
ENV NITRO_HOST 0.0.0.0
ENV NITRO_PORT 3000
ENV BACK4APP_URL=${BACK4APP_URL}
ENV BACK4APP_APPID=${BACK4APP_APPID}
ENV BACK4APP_RESTAPIKEY=${BACK4APP_RESTAPIKEY}
ENV KANBANDATA_URL=${KANBANDATA_URL}

EXPOSE 3000

# run the build project with node
ENTRYPOINT ["node", ".output/server/index.mjs"]