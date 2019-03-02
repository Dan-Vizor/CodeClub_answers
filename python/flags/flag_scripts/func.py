#!/usr/bin/python3
from turtle import *

def rect(width, hight):
	pendown()
	begin_fill()

	forward(width)
	right(90)
	forward(hight)
	right(90)
	forward(width)
	right(90)
	forward(hight)
	right(90)
	
	end_fill()
	penup()