import turtle
m=turtle.Turtle()
def square():
    for i in range(4):
         m.forward(100)
         m.right(90)
for i in range(72):
    square()
    m.right(5)