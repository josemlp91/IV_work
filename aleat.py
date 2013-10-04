#!/usr/bin/python
import random

num = random.randint(1,100)

num_usu = -1
cont=0

while (num_usu != num) and (cont<10):
	
	num_usu = int(raw_input())
	cont=cont+1

	if num_usu > num:
		print ("El numero buscado es menor")


	elif num_usu < num:
		print ("El numero buscado es mayor")


if (cont<10):
	print ("Correctooo, has necesitado %i intentos") % cont

else:
	print ("Has perdido")
