import random
i = 0 
while True:
      x = input("press r to roll and q to quit")
      if(x == "r"):
           Print(random.randint(1,6))
      elif(x == "q"):
           print("bye!")
           exit()
      else:
           print("enter a valied alphabet")
