import RPi.GPIO as GPIO
#import Tkinter
import time

TARGET_1 = 6
TARGET_2 = 13
TARGET_3 = 19
TARGET_4 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(TARGET_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TARGET_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TARGET_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TARGET_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#class simpleapp_tk(Tkinter.Tk):
#  def __init__(self, parent):
#    Tkinter.Tk.__init__(self, parent)
#    self.parent = parent
#    self.initialize()

#  def initialize(self):
#    pass

#if __name__ == "__main__":
#  print "start main"
#  app = simpleapp_tk(None)
#  app.title('my application')
#  print "end main"

if GPIO.input(TARGET_1):
  print 'input was HIGH'
else:
  print 'input was LOW'

if GPIO.input(TARGET_2):
  print 'input was HIGH'
else:
  print 'input was LOW'

if GPIO.input(TARGET_3):
  print 'input was HIGH'
else:
  print 'input was LOW'

if GPIO.input(TARGET_4):
  print 'input was HIGH'
else:
  print 'input was LOW'

start_time = time.time()
print 'Started timer'
while GPIO.input(TARGET_1) == GPIO.HIGH or \
      GPIO.input(TARGET_2) == GPIO.HIGH or \
      GPIO.input(TARGET_3) == GPIO.HIGH or \
      GPIO.input(TARGET_4) == GPIO.HIGH:

  time.sleep(0.2)

  if GPIO.input(TARGET_1):
    print 'target 1 input was HIGH'
  else:
    print 'target 1 input was LOW'

  if GPIO.input(TARGET_2):
    print 'target 2 input was HIGH'
  else:
    print 'target 2 input was LOW'

  if GPIO.input(TARGET_3):
    print 'target 3 input was HIGH'
  else:
    print 'target 3 input was LOW'

  if GPIO.input(TARGET_4):
    print 'target 4 input was HIGH'
  else:
    print 'target 4 input was LOW'

end_time = time.time()
print 'Stopped time'
print 'Time: ' + str(end_time - start_time)
GPIO.cleanup()
