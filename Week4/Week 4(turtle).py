
import turtle
t=turtle.Pen()
t.shape("turtle")
t.color("green")
t.right(75)
t.forward(200)
t.right(105)
t.forward(100)
t.right(105)
t.forward(200)
t.clear()
t.reset()

t.color("blue")
for i in[0,1,2,3]:
    t.forward(100)
    t.up()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.down()


turtle.done()
