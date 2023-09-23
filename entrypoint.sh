#!/bin/sh

#export $(cat ./.env | egrep -v '#|^$' | xargs) && node /app/.output/server/index.mjs

node /app/.output/server/index.mjs