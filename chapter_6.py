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
