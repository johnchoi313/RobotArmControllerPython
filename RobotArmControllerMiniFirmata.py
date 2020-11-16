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
                      
import pyfirmata #Needed to talk to Arduino directly with Standard Firmata.
                 #More info on Python: https://pypi.org/project/pyFirmata/
                 #More info on Arduino: https://www.arduino.cc/en/Reference/Firmata
                 #More info on Firmata: http://firmata.org/wiki/Main_Page

# Joint Class.
class ServoJoint:
  offset = 90  
  min = -90
  max = 90

  pos = 90.0
  toPos = 90.0
  incPos = 0.3

  def __init__(self, board, pin, offset = 90, minAngle = -90, maxAngle = 90):
    self.joint = board.get_pin('d:'+str(pin)+':s')
    self.offset = offset
    self.min = minAngle
    self.max = maxAngle

  def rotate(self, angle, speed = 0.3):
    if(angle < self.min): angle = self.min
    if(angle > self.max): angle = self.max
    self.toPos = angle
    self.incPos = speed

  def update(self):
    if(self.toPos - self.pos > self.incPos * 1.5): self.pos =  self.pos + self.incPos
    elif(self.toPos - self.pos < -self.incPos * 1.5): self.pos =  self.pos - self.incPos
    else: self.pos = self.toPos

    self.joint.write(self.pos + self.offset)

# Robot Arm Mini Class.
class RobotArmMini:
  def __init__(self, port):
    #Create a new serial connection to the Robot's Arduino UNO:
    try:
      self.board = pyfirmata.Arduino(port)
      self.J1 = ServoJoint(self.board,13, 100, -60, 60)
      self.J2 = ServoJoint(self.board,12, 85, -90, 90)
      self.J3 = ServoJoint(self.board,11, 160, -90, 10)
      self.J4 = ServoJoint(self.board,10, 90, -90, 90)
      self.J5 = ServoJoint(self.board,9, 90, -90, 90)
      self.J6 = ServoJoint(self.board,8, 90, -90, 90)
    except:
      print("Could not connect to robot at " + port + "! Exiting.")
      print("(Check USB connection to Arduino and restart program.)")
      quit()

    print("Successfully connected to robot at port " + port + ".")	  
    time.sleep(2)       #Wait two seconds to allow connection to initialize.    
    self.reset()        #Initialize all robot positions.
    
    #Create a new serial writer thread to update robot actuators continuously:
    try: 
      #begin threads to update continuously:
      self.updateThread = threading.Thread(target=self.updater, args=())
      self.updateThread.daemon = True            
      self.updateThread.start()
    except:
      print("Could not begin updater thread for serial communication! Exiting.")
      quit()
    
  def rotate(self, joint, angle):
    if(joint == 1): self.J1.rotate(angle)
    if(joint == 2): self.J2.rotate(angle)
    if(joint == 3): self.J3.rotate(angle)
    if(joint == 4): self.J4.rotate(angle)
    if(joint == 5): self.J5.rotate(angle)
    if(joint == 6): self.J6.rotate(angle)
    
  def reset(self):
    self.rotate(1, 0)
    self.rotate(2, 0)
    self.rotate(3, 0)
    self.rotate(4, 0)
    self.rotate(5, 0)
    self.rotate(6, 0)

  def updater(self):
    while True:
      self.J1.update()
      self.J2.update()
      self.J3.update()
      self.J4.update()
      self.J5.update()
      self.J6.update()
      time.sleep(0.005)

#---BEGIN HERE---#
robot = RobotArmMini('COM3')
angle = 50
sleep = 2

while(True):

  print("J1 start.")
  robot.reset()
  time.sleep(sleep)
  print("J1 moved left" + angle + "degrees.")
  robot.rotate(1, angle)
  time.sleep(sleep)
  print("J1 moved right" + angle + "degrees.")
  robot.rotate(1, -angle)
  time.sleep(sleep)
  print("J1 back to center.")
  robot.reset()
  time.sleep(sleep)

  print("J2 start.")
  robot.reset()
  time.sleep(sleep)
  print("J2 moved left" + angle + "degrees.")
  robot.rotate(2, angle)
  time.sleep(sleep)
  print("J2 moved right" + angle + "degrees.")
  robot.rotate(2, -angle)
  time.sleep(sleep)
  print("J2 back to center.")
  robot.reset()
  time.sleep(sleep)

  print("J3 start.")
  robot.reset()
  time.sleep(sleep)
  print("J3 moved left" + angle + "degrees.")
  robot.rotate(3, angle)
  time.sleep(sleep)
  print("J3 moved right" + angle + "degrees.")
  robot.rotate(3, -angle)
  time.sleep(sleep)
  print("J3 back to center.")
  robot.reset()
  time.sleep(sleep)
  
  print("J4 start.")
  robot.reset()
  time.sleep(sleep)
  print("J4 moved left" + angle + "degrees.")
  robot.rotate(4, angle)
  time.sleep(sleep)
  print("J4 moved right" + angle + "degrees.")
  robot.rotate(4, -angle)
  time.sleep(sleep)
  print("J4 back to center.")
  robot.reset()
  time.sleep(sleep)
  
  print("J5 start.")
  robot.reset()
  time.sleep(sleep)
  print("J5 moved left" + angle + "degrees.")
  robot.rotate(5, angle)
  time.sleep(sleep)
  print("J5 moved right" + angle + "degrees.")
  robot.rotate(5, -angle)
  time.sleep(sleep)
  print("J5 back to center.")
  robot.reset()
  time.sleep(sleep)
  
  print("J6 start.")
  robot.reset()
  time.sleep(sleep)
  print("J6 moved left" + angle + "degrees.")
  robot.rotate(6, angle)
  time.sleep(sleep)
  print("J6 moved right" + angle + "degrees.")
  robot.rotate(6, -angle)
  time.sleep(sleep)
  print("J6 back to center.")
  robot.reset()
  time.sleep(sleep)
  