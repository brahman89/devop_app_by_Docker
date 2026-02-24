import multiprocessing

bind = "5.129.207.205:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 120
keepalive = 5