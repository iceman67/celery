from celery import Celery
import time
import redis
import json

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
r = redis.Redis()

@app.task
def collect(x, y, z=0):
    app.send_task('tasks.history',args=[x,y])
    return "OK" 

@app.task
def history(x, y):
    c = r.get(x)
    r.set(x, y + int(c))
    return x

@app.task
def find(x):
    result = json.loads(r.get(x))
    print (result)
    return result
