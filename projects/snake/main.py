from tkinter import Tk, Frame, Canvas, Button, Label, IntVar, ALL 
import random  

x, y = 15, 15 
direction = ""
position_x = 15
position_y = 15 
position_food = (15, 15)
position_snake = [(75, 75)]
new_position = [(15, 15)]


def coordenates_snake():
	global direction, position_snake, x, y, new_position