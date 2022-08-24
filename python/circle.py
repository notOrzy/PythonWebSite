import time
import turtle
turtle = turtle.Turtle()
rayon = 5
while rayon < 100:
	turtle.circle(rayon)
	rayon = rayon + 5
	print('Le cercle est a', rayon, ' de diamettre')
time.sleep(25)