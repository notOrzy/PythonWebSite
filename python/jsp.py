import turtle
import time
tur = turtle.Turtle()
var = input("Entrez un nombre! ")
var2 = input("Quelle type de forme ? ")
if var2 == 'carre':
	print('carre', var)
	time.sleep(15)
if var2 == 'cercle':
	print('cercle')
	time.sleep(15)