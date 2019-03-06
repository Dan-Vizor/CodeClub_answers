#!/usr/bin/python3
from turtle import *
from func import *
import time

penup()
left(90)
forward(50)
right(90)
back(150)
color("black")
rect(300, 200, False)

forward(150)
right(90)
forward(150)
left(90)

pendown()
color("red")
begin_fill()
circle(50)
end_fill()

time.sleep(5)