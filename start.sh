#!/usr/bin/env bash

BRRS_MYSQL_USER=brrs_dev BRRS_MYSQL_PWD=Brrs_dev_pwd123! BRRS_MYSQL_HOST=localhost BRRS_MYSQL_DB=brrs_dev_db BRRS_TYPE_STORAGE=db BRRS_API_HOST=0.0.0.0 BRRS_API_PORT=5001 python3 -m api.v1.app &
BRRS_MYSQL_USER=brrs_dev BRRS_MYSQL_PWD=Brrs_dev_pwd123! BRRS_MYSQL_HOST=localhost BRRS_MYSQL_DB=brrs_dev_db BRRS_TYPE_STORAGE=db BRRS_API_HOST=0.0.0.0 BRRS_API_PORT=5000 python3 -m web_dynamic.auth
