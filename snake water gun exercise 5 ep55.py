'''a=int(input("press 1 to play\npress 0 to quit"))
while(a==1):
    
    b=input("enter snake,water or gun: ")
    if (b=="snake"):
        print("computer has selected gun ,you lose lol")
    elif(b=="water"):
        print("computer has selected snake,you lose lol")
    elif(b=="gun"):
        print("computer has selected water,you lose lol")
    else:
        print("invalid input")
    a=int(input("press 1 to play\npress 0 to quit"))
    if(a==0) :
        break
print("thank you for playing")'''
#is program main tum hamehsa haroge, ye maine khud banaya hai


'''a=int(input("press 1 to play\npress 0 to quit"))
while(a==1):
    
    b=input("enter snake,water or gun: ")
    if (b=="snake"):
        print("computer has selected water,you win lol")
    elif(b=="water"):
        print("computer has selected gun,you win lol")
    elif(b=="gun"):
        print("computer has selected snake,you win lol")
    else:
        print("invalid input")
    a=int(input("press 1 to play\npress 0 to quit"))
    if(a==0) :
        break
print("thank you for playing")'''
#is program main tum hamesha jeetoge,ye bhi maine banaya hai


#main random output through computer nahi generate karwa paya.computer ka output
#random hona chaiye naki mere thorugh controlled hona chaiye chalo seekhte hai
#ki aisa kaise kiya jaaye

import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
  
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
#ye ekdam sahi code haiaur ye bohut  efficient bhi hai aur mainatainable bhi
  #isse tum computer ke through random output bhi generate karwa sakte ho



