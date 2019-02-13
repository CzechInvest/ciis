import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
#check_config = True

# Logging
access_logfile = "logs/access.log"
error_logfile = "logs/error.log"

# Process name
name = "ciis_gunicorn_proces"

# SSL - http://docs.gunicorn.org/en/stable/settings.html
# keyfile = ""
# certificate = ""
# ssl_version = ""
# ...

# Security - http://docs.gunicorn.org/en/stable/settings.html#security
# limit_request_line = 4094
# limit_request_fields = 100
# limit_request_field_size = 8190

# Server mechanics
preload = False
# chdir = ""
daemon = False
pidfile = "run/ciis.pid"
# pythonpath = "/path1,/path2"

# threads vs. workers https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7
# threads = 2*multiprocessing.cpu_count()

# Server hooks
#
# def on_starting(server):
#     pass
# 
# def on_reload(server):
#     pass
# 
# def when_ready(server):
#     pass
# 
# def pre_fork(server):
#     pass
# 
# def post_fork(server):
#     pass
# 
# def post_worker_init(server):
#     pass
# 
# def worker_int(server):
#     pass
# 
# def worker_abort(server):
#     pass
# 
# def pre_exec(server):
#     pass
# 
# def pre_request(server):
#     pass
# 
# def child_exit(server):
#     pass
# 
# def worker_exit(server):
#     pass
# 
# def nworkers_chnaged(server):
#     pass
# 
# def on_exit(server):
#     pass
