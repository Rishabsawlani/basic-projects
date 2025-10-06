'''for i in range(1,101,1):print(i ,end=" ")if(i==50):breakelse:print("Mississippi")print("Thank you")'''#ex for break statement
'''while True:number = int(input("Enter a positive number: "))print(number)if not number > 0:break'''#ex for emaluating do while loop in python
sum=0
print("let's play kaun banega crorepati")
print("here's the first question on your screen")
print("when did india win their 1st world cup?")
ans1=[1983,1985,1987,1989]
print("options are",ans1)
a=int(input("enter your answer "))
if(a==1983):
    sum=sum+1000
    print("your answer is correct.You have won 1000 rupees")
else:
    sum=sum+0
    print("your answer is wrong.You have won 0 rupees")


print("here's the second question on your screen")
print("when did india win their 2nd world cup?")
ans2=[2001,2011,2012,2014]
print("options are",ans2)
b=int(input("enter your answer "))
if(b==2011):
    sum=sum+1000
    print("your answer is correct.You have won 1000 rupees")
else:
    sum=sum+0
    print("your answer is wrong.You have won 0 rupees")


print("here's the third question on your screen")
print("which country is the second largest")
ans3=["canada","usa","brazil","china"]
print("options are ",ans3)
c=input("enter your answer ")
if(c=="canada"):
    sum=sum+1000
    print("your answer is correct.You have won 1000 rupees")
else:
    sum=sum+0
    print("your answer is wrong.You have won 0 rupees")

print("here's the fourth question on your screen")
print("how many icc trophies south africa has won?")
ans4=[0,1,2,3]
print("options are ",ans4)
d=int(input("enter your answer "))
if(d==1):
    sum=sum+1000
    print("your answer is correct.You have won 1000 rupees")
else:
    sum=sum+0
    print("your answer is wrong.You have won 0 rupees")

print("here's the fifth question on your screen")
print("how many icc trophies australia has won?")
ans4=[6,7,8,9]
print("options are ",ans4)
e=int(input("enter your answer "))
if(e==9):
    sum=sum+1000
    print("your answer is correct.You have won 1000 rupees")
else:
    sum=sum+0
    print("your answer is wrong.You have won 0 rupees")


print("you have won ",sum," rupees")


