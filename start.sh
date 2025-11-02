#!/bin/bash
  
export DB_HOST=localhost
export DB_PORT=3306
export DB_USERNAME=root
export DB_PASSWORD=123456
export DB=school

export DOMAIN='https://'

#python启动
PYTHONPATH=`pwd`
python main.py

#uvicorn启动
#uvicorn main:app --reload
#gunicorn -k uvicorn.workers.UvicornWorker --bind "127.0.0.1:8000"  main:app --daemon
#gunicorn -k uvicorn.workers.UvicornWorker --bind "127.0.0.1:8000"  main:app
#gunicorn -c gunicorn.conf.py -k uvicorn.workers.UvicornWorker  main:app --daemon

echo 'ok'


