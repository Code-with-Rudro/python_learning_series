import pyttsx3
engine = pyttsx3.init()
engine.say(input("enter your name"))
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

# PQS-3 : check the input type ?

names =input("enter your nsme : ")
print(f"name is: {names}")
print(type(names))


# PQS-4 Check the conditation is true or false (a>b)?
A_n= input("enter your 1st number:")
secnd= input("enter your 2nd number :")
print(A_n>secnd)

#PQS-5 find the average of a,b?
avg1= int(input("enter your number 1 :"))
avg2= int(input("enter your number 2 : "))

print("the average is :", (avg1 + avg2)/2)

#PQS - 6 :FIND THE SQUARE OF THE INPUT NUMBER ?

print("the square of avg1 : ", avg1*avg1)
