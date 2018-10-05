import random
d={1:'R',2:'P',3:'S'}
c=d[random.randint(1,3)]
while(1):
  p=input("enter'R','P,'S'")
  print("computer",c)
  if(c==p):
   print("tie")
  elif((c=='R'and p=='S') or(c=='P'and p=='R') or(c=='S'and p=='p')):
   print("computer win")
  else:
   print("player win")
   
    
    output
    cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'R
computer win
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'R
computer P
computer win
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'S
computer P
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'R
computer R
tie
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'P
computer S
player win
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'R
computer R
tie
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'S
computer P
player win
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'R
computer P
computer win
cl316@soetcse:~/aishwarya$ python3 spc.py
enter'R','P,'S'p
computer P
player win

    
