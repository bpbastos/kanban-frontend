FROM node:16-alpine

WORKDIR /app

RUN apk --no-cache add openssh g++ make python3 git

COPY package.json /app/
COPY package-lock.json /app/

RUN npm ci && npm cache clean --force

ADD . /app

RUN npm run build

ENV NITRO_HOST=0.0.0.0
ENV NITRO_PORT=3000
ENV BACK4APP_URL=${BACK4APP_URL}
ENV BACK4APP_APPID=${BACK4APP_APPID}
ENV BACK4APP_RESTAPIKEY=${BACK4APP_RESTAPIKEY}
ENV KANBANDATA_URL=${KANBANDATA_URL}

EXPOSE 3000

ENTRYPOINT ["node", ".output/server/index.mjs"]