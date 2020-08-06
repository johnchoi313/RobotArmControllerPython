import socket    #Needed to send and receive network control communications.
                 #More info: https://wiki.python.org/moin/UdpCommunication
				 
import threading #Used for concurrent robot communication with other processes. 
                 #More info: https://docs.python.org/2/library/threading.html
       
import time      #Used to create delays for proper timing of robot actions.
                 #More info: https://docs.python.org/2/library/time.html

import sys       #Used for certain specific calls to the system.
                 #More info: https://docs.python.org/2/library/sys.html

import asyncio   #Another type of threading for asynchronous multi-processing.
                 #More info: https://docs.python.org/3/library/asyncio-task.html

import json      #Needed to format robot control messages. 
                 #More info: https://docs.python.org/3/library/json.html
                      
import json      #Needed to format robot control messages. 
                 #More info: https://docs.python.org/3/library/json.html

import requests  #Needed to send HTTP requests. 
                 #More info: https://requests.readthedocs.io/en/master/

IP = "192.168.1.155"
PORT = "8000"
username = "Bob"
password = "123"
robotID = 0

# SET COMMANDS
def SetPosition(x, y, z, speed = 100):
    d = {'username': username, 'password': password, 'robotID':robotID, 
         'speed':speed, 'position':{'x':x,'y':y,'z':z}}
    r = requests.post("http://" + IP + ":" + PORT + "/GetPosition", data = json.dumps(d), timeout=1)
    print(r.json())

def SetRotation(x, y, z, speed = 100):
    d = {'username': username, 'password': password, 'robotID':robotID, 
         'speed':speed, 'rotation':{'x':x,'y':y,'z':z}}
    r = requests.post("http://" + IP + ":" + PORT + "/GetRotation", data = json.dumps(d), timeout=1)
    print(r.json())

def Translate(x, y, z, speed = 100, local = False):
    d = {'username': username, 'password': password, 'robotID':robotID, 
         'speed':speed, 'local':local, 'position':{'x':x,'y':y,'z':z} }
    r = requests.post("http://" + IP + ":" + PORT + "/Translate", data = json.dumps(d), timeout=1)
    print(r.json())

def Rotate(x, y, z, speed = 100, local = False):
    d = {'username': username, 'password': password, 'robotID':robotID, 
         'speed':speed, 'local':local, 'rotation':{'x':x,'y':y,'z':z} }
    r = requests.post("http://" + IP + ":" + PORT + "/Rotate", data = json.dumps(d), timeout=1)
    print(r.json())

# GET COMMANDS
def GetPosition():
    d = {'username': username, 'password': password, 'robotID':robotID}
    r = requests.post("http://" + IP + ":" + PORT + "/GetPosition", data = json.dumps(d), timeout=1)
    print(r.json())

def GetRotation():
    d = {'username': username, 'password': password, 'robotID':robotID}
    r = requests.post("http://" + IP + ":" + PORT + "/GetRotation", data = json.dumps(d), timeout=1)
    print(r.json())

