import multiprocessing

#并行工作进程数  核心数*2+1个
workers = multiprocessing.cpu_count() * 2 + 1
#指定每个工作者的线程数
threads = 2
#监听内网端口
bind = '127.0.0.1:8011'
#设置守护进程
deamon = 'true'
#工作模式协程
worker_class = 'gevent'
#设置最大并发量
worker_connections = 2000
#设置进程文件目录
pidfile = '/var/run/gunicorn.pid'
#日志
access_log_format = '%(t)s  "%(r)s"  %(b)s  %(s)s'
accesslog = '/var/log/gunicorn_access.log'
errorlog = '/var/log/gunicorn_error.log'
#日志级别，这个日志级别是错误日志级别，访问日志无法设置
loglevel = 'warning'

