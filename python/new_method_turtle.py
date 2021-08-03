#spiracle
import turtle
sp = turtle.Turtle()


distance = 1

for _ in range(360):
    
    sp.forward(distance)
    sp.left(30)
    distance = distance + 1
    
