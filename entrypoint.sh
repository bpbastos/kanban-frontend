#!/bin/sh
echo BACK4APP_URL=$BACK4APP_URL >> /app/.env
echo BACK4APP_APPID=$BACK4APP_APPID >> /app/.env
echo BACK4APP_RESTAPIKEY=$BACK4APP_RESTAPIKEY >> /app/.env
echo KANBANDATA_URL=$KANBANDATA_URL >> /app/.env
echo NUXT_SECRET=$NUXT_SECRET >> /app/.env

node -r dotenv/config .output/server/index.mjs