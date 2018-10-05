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