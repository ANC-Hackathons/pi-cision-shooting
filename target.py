#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import RPi.GPIO as GPIO
import Tkinter
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

class simpleapp_tk(Tkinter.Tk):
  def __init__(self, parent):
    Tkinter.Tk.__init__(self, parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.grid()

    self.entryVariable = Tkinter.StringVar()
    self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
    self.entry.grid(column=0, row=0, sticky='EW')
    self.entry.bind("<Return>", self.OnPressEnter)
    self.entryVariable.set(u"Enter text here.")

    button = Tkinter.Button(self, text=u"Start Clock", command=self.OnButtonClick)
    button.grid(column=1, row=0)

    self.labelVariable = Tkinter.StringVar()
    label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
    label.grid(column=0, row=1, columnspan=2, sticky='EW')
    self.labelVariable.set(u"Hello !")

    self.grid_columnconfigure(0, weight=1)
    self.update()
    self.geometry(self.geometry())
    self.entry.focus_set()
    self.entry.selection_range(0, Tkinter.END)

  def OnButtonClick(self):
    self.labelVariable.set(self.entryVariable.get() + " (You clicked the button !)")
    self.entry.focus_set()
    self.entry.selection_range(0, Tkinter.END)

  def OnPressEnter(self, event):
    self.labelVariable.set(self.entryVariable.get() + " (You pressed enter !)")
    self.entry.focus_set()
    self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
  app = simpleapp_tk(None)
  app.title('my application')
  app.mainloop()

#if GPIO.input(TARGET_1):
#  print 'input was HIGH'
#else:
#  print 'input was LOW'

#if GPIO.input(TARGET_2):
#  print 'input was HIGH'
#else:
#  print 'input was LOW'

#if GPIO.input(TARGET_3):
#  print 'input was HIGH'
#else:
#  print 'input was LOW'

#if GPIO.input(TARGET_4):
#  print 'input was HIGH'
#else:
#  print 'input was LOW'

#start_time = time.time()
#print 'Started timer'
#while GPIO.input(TARGET_1) == GPIO.HIGH or \
#      GPIO.input(TARGET_2) == GPIO.HIGH or \
#      GPIO.input(TARGET_3) == GPIO.HIGH or \
#      GPIO.input(TARGET_4) == GPIO.HIGH:

#  time.sleep(0.2)

#  if GPIO.input(TARGET_1):
#    print 'target 1 input was HIGH'
#  else:
#    print 'target 1 input was LOW'

#  if GPIO.input(TARGET_2):
#    print 'target 2 input was HIGH'
#  else:
#    print 'target 2 input was LOW'

#  if GPIO.input(TARGET_3):
#    print 'target 3 input was HIGH'
#  else:
#    print 'target 3 input was LOW'

#  if GPIO.input(TARGET_4):
#    print 'target 4 input was HIGH'
#  else:
#    print 'target 4 input was LOW'

#end_time = time.time()
#print 'Stopped time'
#print 'Time: ' + str(end_time - start_time)
#GPIO.cleanup()
