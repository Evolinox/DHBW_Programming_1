import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightblue")

skk = turtle.Turtle()
skk.color("red")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(95)
        size = size + 5

for i in range(6, 1000, 20):
    sqrfunc(i)