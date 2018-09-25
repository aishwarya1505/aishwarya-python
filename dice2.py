#exiquting random numbers
import random
while True:
	x=input("press r to roll and q to quit")
	if(x=='r'):
		print (random.randint(1,6))
	else:
		print("bye!")
		exit()