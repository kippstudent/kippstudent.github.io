from gopigo import *
import time

def move_right():
  enc_tgt(1,0,14)
  time.sleep(.1)
  right()
  time.sleep(2)

def move_left():
  enc_tgt(0,1,14)
  time.sleep(.1)
  left()
  time.sleep(2)
  
while us_dist(15) > 20:
  fwd()
stop()
servo(180)
if us_dist(15) > 20:
  move_right()
else:
  servo(0)
  if us_dist(15) > 20:
