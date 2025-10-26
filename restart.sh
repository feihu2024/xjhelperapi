ps -ef|grep gunicorn|cut -c 9-16|xargs kill -9
echo 'kill over'
#./start.sh
#echo 'restart over'
