a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("-------")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("-------")
	print(a[6]+'|'+a[7]+'|'+a[8])
	print("-------")
playerOneTurn = True

for  in range(9):
	printboard()	
#player1 plays
	if playerOneTurn:
		p=input("player 1, choose your palce:")
		if p in a:
			a[int(p)-1]='x'
			playerOneTurn= not playerOneTurn
#player 2 plays
	else:
		p=input("player 2, choose your place:")
		if p in a:
			a[int(p)-1]= '0'
			playerOneTurn = not playerOneTurn






