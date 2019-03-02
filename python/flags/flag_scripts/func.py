#!/usr/bin/python3
from turtle import *

def rect(width, hight, color):
	pendown()
	if color:
		begin_fill()

	forward(width)
	right(90)
	forward(hight)
	right(90)
	forward(width)
	right(90)
	forward(hight)
	right(90)
	
	if color:
		end_fill()
	penup()