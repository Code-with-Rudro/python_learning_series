import pyttsx3
engine = pyttsx3.init()
engine.say(("enter your name"))
engine.runAndWait()
# print a block of lines using 
# CHAPTER-1 
# CHAPTER-1 PQS-1 (PRATICE QUESTION)

print(""" Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star. """)

# PQS-2
# install external module using python.

# we install pyttsx3 for TTS

# instal pyttsx3 using pip


#chapter-2
# day-2 python learning 

#PQS-1 : sun of two numbers ?

num_a = 10
num_b = 20

print(num_a+num_b)

#PQS-2 : print the reminder of num_a, num_b ?

print(num_a%num_b)

# PQS-3 : check the  type ?

names =("enter your nsme : ")
print(f"name is: {names}")
print(type(names))


# PQS-4 Check the conditation is true or false (a>b)?
A_n= ("enter your 1st number:")
secnd= ("enter your 2nd number :")
print(A_n>secnd)

#PQS-5 find the average of a,b?
avg1= int(input("enter your number 1 :"))
avg2= int(input("enter your number 2 : "))

print("the average is :", (avg1 + avg2)/2)

#PQS - 6 :FIND THE SQUARE OF THE  NUMBER ?

print("the square of avg1 : ", avg1*avg1)

# chapter-3
#PQS 1 : 
#write a code to great the  user ?
user = ("say your name buddy:")
print(f"hey {user}, how are you")

#PQS 2 :
#Replace the string content ?

names = " heloo everyone how are you"
rec = names.replace("hello", "hey")
print(names)
print(rec)

#PQS 3
# delete the how in names ?
remove = names.replace("how", "")

print(remove)

#pqs 4
# format a string using escape sequence ?

format = "hi saksm,\n \ti hope your doing well,\n \ti am \'rudra\', i am from \"shreeya\" team, i have some doubt do you help me to feaguer it out.\n \t\t thank you, \n \t\t\tyours faithfully,\n \t\t\trudra prasad. "
print(format)

#chapter-4
#PQS-1
#store 7 frouts ina list given by the user?
fruit = []
a = input("enter your 1st frute name :")
fruit.append(a)
a = input("enter your 2st frute name :")
fruit.append(a)
a = input("enter your 3st frute name :")
fruit.append(a)
a = input("enter your 4st frute name :")
fruit.append(a)
a = input("enter your 5st frute name :")
fruit.append(a)
a = input("enter your 6st frute name :")
fruit.append(a)
a = input("enter your 7st frute name :")
fruit.append(a)
print(fruit)

#PQS-2
#sorted the 6 student mark input given by the user ?

student = []
st = int(input("enter the 1st student mark :"))
student.append(st)
st = int(input("enter the 2st student mark :"))
student.append(st)
st = int(input("enter the 3st student mark :"))
student.append(st)
st = int(input("enter the 4st student mark :"))
student.append(st)
st = int(input("enter the 5st student mark :"))
student.append(st)
st = int(input("enter the 6st student mark :"))
student.append(st)

print(student)
student.sort()
print(f"sorted student mark : {student}")
