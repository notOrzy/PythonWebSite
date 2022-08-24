import turtle
import time
import logging
logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')
tur = turtle.Turtle()
var = input("Entrez un nombre! ")
var2 = input("Quelle type de forme ? ")
if var2 == 'triangle':
	tur.forward (var) # draw base
	tur.left (120)
	tur.forward (var)
	tur.left (120)
	tur.forward (var)
	tur.done ()
	time.sleep(10)
if var2 == 'cercle':
	tur.circle(var)
	time.sleep(5)