from graphics import *
from math import *
from time import *

win = GraphWin("AdiabaticInv", 1000, 200)

Re_wall = 1000
Im_wall = 1000
R = 10
Re_ball = 10
Im_ball = 10
dt = 0.001
Dt = 0.1
u = 1
v = 30

wall = Line(Point(1000, 0), Point(1000, 200))
wall.setWidth(5)
wall.draw(win)

ball = Circle(Point(R, 200-R), R)
ball.setFill("yellow")
ball.draw(win)

n = Dt / dt
i = 0
while (Re_wall > 0):
    i = i + 1
    Re_wall = Re_wall - u*dt
    Re_ball = Re_ball + v*dt
    if (Re_ball + R > Re_wall):
        v = -2*u - v
        Re_ball = min(2*Re_wall - Re_ball, Re_wall - R)
    if (Re_ball - R < 0):
        v = -v
        Re_ball = max(R, -Re_ball)
    if (i > n):
        sleep(0.01)
        delta = floor(Re_wall - Im_wall)
        Im_wall = Im_wall + delta
        wall.move(delta, 0)
        delta = floor(Re_ball - Im_ball)
        Im_ball = Im_ball + delta
        ball.move(delta, 0)
        i = 0

win.getMouse()
win.close()