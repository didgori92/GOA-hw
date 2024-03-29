from turtle import *
speed(40)
width(7)


#house1
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

#door
forward(35)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)

#roof
penup()
goto(100, 100)
pendown()

color("brown")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()

#windows


penup()
goto(10, 30)
pendown()
left(210)
width(3)
color("black")
forward(30)
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(15)

penup()
goto(90, 30)
pendown()
forward(15)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
right(90)

#house2
penup()
goto(-200, 0)
pendown()
color("black")
width(7)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)


forward(35)
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)

penup()
goto(-200, 100)
pendown()

color("brown")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()

penup()
goto(-290, 30)
pendown()
width(3)
color("black")
right(150)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(15)

penup()
goto(-225, 30)
pendown()
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(15)

#tree1

penup()
goto(-115, 0)
pendown()
color("brown")
right(90)
begin_fill()
forward(90)
right(90)
forward(30)
right(90)
forward(90)
right(90)
forward(30)
end_fill()
penup()
goto(-100, 130)
pendown()
begin_fill()
color("green")
circle(40, 360)
end_fill()

#sun
penup()
goto(0, 400)
pendown()
color("yellow")
begin_fill()
circle(70, 360)
end_fill()

#road
penup()
goto(300, -100)
pendown()
color("black")
forward(700)
right(90)
forward(50)
right(90)
forward(700)
right(90)
forward(50)

#house3
penup()
goto(0, -300)
pendown()
width(7)
right(180)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

color("brown")
begin_fill()
right(30)
forward(100)
right(120)
forward(100)
end_fill()
color("black")
penup()
goto(35, -300)
pendown()
right(210)
forward(50)
right(90)
forward(30)
right(90)
forward(50)

width(3)
penup()
goto(10, -250)
pendown()
forward(30)
left(90)
forward(15)
left(90)
forward(30)
left(90)
forward(15)

penup()
goto(90, -250)
pendown()
left(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(15)



exitonclick()