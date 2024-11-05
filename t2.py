import sys
import turtle
import math

def pythagorean_tree(t, order, branch_length=100, angle=45):
	if order == 0:
		return

	left_h = None
	left_p = None

	rigth_h = None
	right_p = None

	for i in range(4):
		t.forward(branch_length)
		if i == 0:
			left_h = t.heading()
			left_p = t.position()
		if i == 1:
			rigth_h = t.heading()
			right_p = t.position()
		t.right(90)

	if left_h is not None and left_p is not None:
		t.penup()
		t.setheading(left_h)
		t.goto(left_p)
		t.pendown()
		t.left(45)
		pythagorean_tree(t, order - 1, branch_length / math.sqrt(2))
		
	if rigth_h is not None and right_p is not None:
		t.penup()
		t.setheading(rigth_h)
		t.goto(right_p)
		t.left(135)
		t.forward(branch_length / math.sqrt(2))
		t.right(90)
		t.pendown()
		pythagorean_tree(t, order - 1, branch_length / math.sqrt(2))

def draw_pythagorean_tree(order):
	window = turtle.Screen()
	window.bgcolor("white")

	t = turtle.Turtle()
	t.speed(0)
	t.left(90)

	t.penup()
	t.goto(-50, -150)
	t.pendown()

	pythagorean_tree(t, depth)

	t.hideturtle()
	window.mainloop()

depth = 5
if len(sys.argv) > 1:
	try:
		parsed = int(sys.argv[1])
	except:
		pass
	else:
		if parsed >= 0:
			depth = parsed
draw_pythagorean_tree(depth)