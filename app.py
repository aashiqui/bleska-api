# -*- coding: utf-8 -*-
import psutil
from flask import Flask , jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app) # This will enable CORS for all routes

@app.route('/api')
def hello():
    return "Hello World!"

@app.route('/api/load')
#@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def load():
    
    response={}
    response['cpu']=psutil.cpu_percent()
    # Load
    with open("/proc/loadavg", "r") as f:
        response['load']=f.read().strip()
    uptime = None
    with open("/proc/uptime", "r") as f:
        uptime = f.read().split(" ")[0].strip()
    response['uptime']=int(float(uptime))
   
    response['memory']=dict(psutil.virtual_memory()._asdict())
    return jsonify(response)


@app.route('/api/<name>')
def hello_name(name):
    return "Hello  test {}!".format(name)

if __name__ == '__main__':
    app.run()

