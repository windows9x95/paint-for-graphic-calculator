#free verion - unregistered 
#price for full version : 29.99 euro
#copyright Microsoft (c) 2020
from ion import *
from time import*
from kandinsky import *
from boot import *
c = color(0,0,0)
x = 160
y = 110
main()
fill_rect(0,0,640,480,(0,0,255))
while True:
  draw_string("Microsoft Paint for windows",5,5,(0,0,0),(0,0,255))
  draw_string("Press EXE to start",5,25,(0,0,0),(0,0,255))
  draw_string("Press 0 to exit the program",5,45,(0,0,0),(0,0,255))
  draw_string("mspaint - unregistred version",5,185,(0,0,0),(0,0,255))
  draw_string("build 200219.2",5,205,(0,0,0),(0,0,255))
  draw_string("for help, read manual",5,65,(0,0,0),(0,0,255))
  draw_string("Made for Intel(r) Atom N280",5,165,(0,0,0),(0,0,255))
  if keydown(KEY_EXE):
    break
fill_rect(0,0,640,480,(255,255,255))
while True:
  if keydown(KEY_ZERO):
    break
  if keydown(KEY_UP):
    y = y - 1
  if keydown(KEY_LEFT):
    x = x - 1
  if keydown(KEY_DOWN):
    y = y + 1
  if keydown(KEY_RIGHT):
    x = x + 1
  if keydown(KEY_SEVEN):
    fill_rect(0,0,640,480,(255,255,255))
  if keydown(KEY_SIX):
    c = color(0,0,0)
  if keydown(KEY_FOUR):
    c = color(255,255,255)
  set_pixel(x,y,c)
  sleep(0.0125)
