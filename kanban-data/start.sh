#!/bin/bash
export PARSE_SERVER_URL=https://parseapi.back4app.com 
export PARSE_SERVER_APPID=HRWNwQna34QIpbOEsyukGs3Qzph7zehNOk6v1xMe 
export PARSE_SERVER_RESTAPIKEY=gDqBC29FAnKs2WDbLcWqhzXNsMKaH7gZgzph9BUb 

uvicorn app:app --reload --host 0.0.0.0