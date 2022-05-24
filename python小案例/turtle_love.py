# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/3 17:
import time
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
sizeh = 1.2
def curve():
    for ii in range(200):
        turtle.right(1)
        turtle.forward(1*sizeh)

turtle.speed(10)
turtle.color("red", "red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65*sizeh)
curve()
turtle.left(120)
curve()
turtle.forward(111.65*sizeh)
turtle.end_fill()
turtle.hideturtle()
time.sleep(10)