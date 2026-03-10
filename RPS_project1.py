import random
cmp1 = ["r","p","s"]
computer = random.choice(cmp1)

rudra = str(input("choose your letter (r,p,s) : "))


if(computer == rudra):
  print("its a draw")
  
elif(computer == "r" and rudra =="p"):
  print("rudra win")
  
elif(computer  =="r" and rudra =="s"):
  print(" computer win !")
  
elif(computer == "p" and rudra== "r"):
  print("rudra win !")
  
elif(computer == "p" and rudra == "s"):
  print(" computer win !")
  
elif(computer == "s" and rudra == "r"):
  print(" rudra win !")
elif(computer == "s" and rudra =="p"):
  print(" computer win !")
  
else:
  print("error")