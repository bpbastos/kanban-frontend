FROM node:lts-alpine

ARG NODE_VERSION=lts
ARG BACK4APP_URL=${BACK4APP_URL}
ARG BACK4APP_APPID=${BACK4APP_APPID}
ARG BACK4APP_RESTAPIKEY=${BACK4APP_RESTAPIKEY}
ARG KANBANDATA_URL=${KANBANDATA_URL}

WORKDIR /app

RUN apk --no-cache add openssh g++ make python3 git

COPY package.json /app/
COPY package-lock.json /app/

RUN npm ci && npm cache clean --force

ADD . /app

RUN echo BACK4APP_URL=${BACK4APP_URL} > .env
RUN echo BACK4APP_APPID=${BACK4APP_APPID} >> .env
RUN echo BACK4APP_RESTAPIKEY=${BACK4APP_RESTAPIKEY} >> .env
RUN echo KANBANDATA_URL=${KANBANDATA_URL} >> .env

RUN chmod a+x entrypoint.sh

RUN npm run build

ENV HOST 0.0.0.0
ENV PORT 3000
EXPOSE 3000

ENTRYPOINT ["/app/entrypoint.sh"]