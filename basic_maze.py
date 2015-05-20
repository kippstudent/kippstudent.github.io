from gopigo import *
import time
import math
set_speed(100)
set_left_speed(100)
led_on()
def move_forward(feet):
  mm= feet * float (304.8)
  steps = int (math.floor(mm / 11.34))
  enc_tgt(1,1,steps)
  time.sleep(.1)
  fwd()
  time.sleep(feet * 2)

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
  
move_forward(4)
move_right()
move_foward(3)
move_right()
move_forward(4)
