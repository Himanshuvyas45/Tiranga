import turtle

def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range (2):
        t.forward(250)
        t.right(90)
        t.forward(70) 
        t.right(90)
    t.end_fill()


wn = turtle.Screen() 
wn.title("Tiranga") 
wn.setup(width=600, height=600)

# make Tiranga  
t = turtle.Turtle()
t.up()
t.pensize(3)
t.goto(0,-300)
t.down()
t.goto(0,200)
rectangle("#ff9933")

t.goto(0,130)
t.forward(125)
t.color("#000088")
t.circle(-35)
t.setheading(270)
t.forward(35)
t.setheading(0)
for i in range(24):
    t.forward(33)
    t.bk(33)
    t.left(15)
t.setheading(90)
t.forward(35)
t.setheading(0)

t.color("black")
t.forward(125)
t.right(90)
t.forward(70)
t.right(90)
t.forward(250)
t.right(90)
t.forward(70)
t.right(90)

t.goto(0,60)
rectangle("#128807")

# orange roket
roketthi = turtle.Turtle()
roketthi.speed(2)
roketthi.shape("triangle")
roketthi.shapesize(2)
roketthi.color("#e67e22")
roketthi.left(110)
roketthi.up()
roketthi.goto(80,-230)
roketthi.down()
roketthi.penup()
roketthi.goto(-270,300)

# blue roket
roket = turtle.Turtle()
roket.speed(2)
roket.shape("triangle")
roket.shapesize(2)
roket.color("#2980b9")
roket.left(130)
roket.up()
roket.goto(100,-230)
roket.down()
roket.penup()
roket.goto(-250,300)

# green roket
rokettow = turtle.Turtle()
rokettow.speed(2)
rokettow.shape("triangle")
rokettow.shapesize(2)
rokettow.color("#2ecc71")
rokettow.left(120)
rokettow.up()
rokettow.goto(120,-230)
rokettow.down()
rokettow.penup()
rokettow.goto(-265,300)

# jai hind
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("JAI HIND", align="center", font=("futura", 50, "bold"))

wn.mainloop()