#!/bin/sh

export $(cat .env | egrep -v '#|^$' | xargs) && node .output/server/index.mjs