#chapter -6
#conditional statements :
# conditional statements are used to perform different actions based on different conditions.
#relational operators :

#    1. == : equal to
#    2. != : not equal to
#    3. < : less than
#    4. > : greater than
#    5. <= : less than or equal to
#    6. >= : greater than or equal to

#logical operators :
#    1. and : returns true if both statements are true
#    2. or : returns true if one of the statements is true  
#    3. not : reverse the result, returns false if the result is true

#ex - 
employe = int(input("enter your lucky number :"))

if(employe >= 10):
    print("sorry bro your got regected ",employe)
elif(employe>=5):
    print("your miss just by small mistake",employe)
elif(employe<5):
    print("yha your gues the correct ",employe)
else:
   print("not goood choice",employe)








#chapter-6
#PQS-4
#write a program to find gratest of four numbers input by the user?

uv1 = int(input("enter your 1st mark :"))


uv2 = int(input("enter your 2st mark :"))


uv3 = int(input("enter your 3st mark :"))

uv4 = int(input("enter your 4st mark :"))

if(uv1>uv2 & uv1>uv3 & uv1>uv4):
    print("user_values1 is greatest :", uv1)
elif(uv2>uv1 & uv2>uv3 & uv2>uv4):
    print("user_values2 is greatest :", uv2)
elif(uv3>uv1 & uv3>uv2 & uv3>uv4):
    print("user_values3 is greatest :", uv3)
else:
    print("user_values4 is greatest :", uv4)