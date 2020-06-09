from celery import Celery
import time
import redis
import json
import ipfshttpclient

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

r = redis.Redis()

@app.task
def collect(x, y, z=0):
    res = client.add(y)['Hash']
    app.send_task('tasks.history',args=[x,res])
  
    return "OK" 

@app.task
def history(x, y):
    c = r.get(x)
    if c == None:
       r.set(x, y)
    else:
       r.set(x,c)
    return y

@app.task
def find(x):
    result = r.get(x)
    return result.decode("utf-8")
'''
    result = json.loads(r.get(x))
    print (result)
    return json.dumps(result)
'''
@app.task
def cat(x):
    result = r.get(x)
    res = client.cat(x)
    return res.decode("utf-8")
