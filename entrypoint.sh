#!/bin/sh

export $(cat /app/.env | egrep -v '#|^$' | xargs) && node /app/.output/server/index.mjs