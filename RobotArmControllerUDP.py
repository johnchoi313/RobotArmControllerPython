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
                      
UDP_IP = "127.0.0.1"
UDP_PORT = 9000
MESSAGE = "Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
           
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #(Internet, UDP)                               
#sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))

def sendPosition(x, y, z):
  data = {
    "position": { "x":x,"y":y,"z":z }
  }
  jsonMessage = json.dumps(data)
  sock.sendto(jsonMessage.encode('utf-8'), (UDP_IP, UDP_PORT))

def sendRotation(x, y, z):
  data = {
    "rotation": { "x":x,"y":y,"z":z }
  }
  jsonMessage = json.dumps(data)
  sock.sendto(jsonMessage.encode('utf-8'), (UDP_IP, UDP_PORT))

sendPosition(1,2,3)  
  

