#!/bin/sh
APP_PATH=/app
echo > .env
echo BACK4APP_URL=$BACK4APP_URL >>.env
echo BACK4APP_APPID=$BACK4APP_APPID >> .env
echo BACK4APP_RESTAPIKEY=$BACK4APP_RESTAPIKEY >> .env
echo KANBANDATA_URL=$KANBANDATA_URL >> .env
echo NUXT_SECRET=$NUXT_SECRET >> .env

sleep 5

export $(cat .env | egrep -v '#|^$' | xargs) && node .output/server/index.mjs