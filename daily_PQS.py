# import pyttsx3
# engine = pyttsx3.init()
# engine.say(("enter your name"))
# engine.runAndWait()
# # print a block of lines using 
# # CHAPTER-1 
# # CHAPTER-1 PQS-1 (PRATICE QUESTION)

# print(""" Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star. """)

# # PQS-2
# # install external module using python.

# # we install pyttsx3 for TTS

# # instal pyttsx3 using pip


# #chapter-2
# # day-2 python learning 

# #PQS-1 : sun of two numbers ?

# num_a = 10
# num_b = 20

# print(num_a+num_b)

# #PQS-2 : print the reminder of num_a, num_b ?

# print(num_a%num_b)

# # PQS-3 : check the  type ?

# names =("enter your nsme : ")
# print(f"name is: {names}")
# print(type(names))


# # PQS-4 Check the conditation is true or false (a>b)?
# A_n= ("enter your 1st number:")
# secnd= ("enter your 2nd number :")
# print(A_n>secnd)

# #PQS-5 find the average of a,b?
# avg1= int(input("enter your number 1 :"))
# avg2= int(input("enter your number 2 : "))

# print("the average is :", (avg1 + avg2)/2)

# #PQS - 6 :FIND THE SQUARE OF THE  NUMBER ?

# print("the square of avg1 : ", avg1*avg1)

# # chapter-3
# #PQS 1 : 
# #write a code to great the  user ?
# user = ("say your name buddy:")
# print(f"hey {user}, how are you")

# #PQS 2 :
# #Replace the string content ?

# names = " heloo everyone how are you"
# rec = names.replace("hello", "hey")
# print(names)
# print(rec)

# #PQS 3
# # delete the how in names ?
# remove = names.replace("how", "")

# print(remove)

# #pqs 4
# # format a string using escape sequence ?

# format = "hi saksm,\n \ti hope your doing well,\n \ti am \'rudra\', i am from \"shreeya\" team, i have some doubt do you help me to feaguer it out.\n \t\t thank you, \n \t\t\tyours faithfully,\n \t\t\trudra prasad. "
# print(format)

# #chapter-4
# #PQS-1
# #store 7 frouts ina list given by the user?
# fruit = []
# a = input("enter your 1st frute name :")
# fruit.append(a)
# a = input("enter your 2st frute name :")
# fruit.append(a)
# a = input("enter your 3st frute name :")
# fruit.append(a)
# a = input("enter your 4st frute name :")
# fruit.append(a)
# a = input("enter your 5st frute name :")
# fruit.append(a)
# a = input("enter your 6st frute name :")
# fruit.append(a)
# a = input("enter your 7st frute name :")
# fruit.append(a)
# print(fruit)

# #PQS-2
# #sorted the 6 student mark input given by the user ?

# student = []
# st = int(input("enter the 1st student mark :"))
# student.append(st)
# st = int(input("enter the 2st student mark :"))
# student.append(st)
# st = int(input("enter the 3st student mark :"))
# student.append(st)
# st = int(input("enter the 4st student mark :"))
# student.append(st)
# st = int(input("enter the 5st student mark :"))
# student.append(st)
# st = int(input("enter the 6st student mark :"))
# student.append(st)

# print(student)
# student.sort()
# print(f"sorted student mark : {student}")

# #PQS-3
# # check the tuple is iommutable or not 
# # tuple =(1,2,3,4,)
# # tuple.append(5) # it will give error because tuple is immutable
# # print(tuple)

# #PQS -4
# # SUM of tudent mark ?
# print(f"sum of student marks : {sum(student)}")
# #PQS-5
# #count the 10 in student mark ?
# print(f"count the 10 in student list: {student.count(10)}")


# #chapter - 5
# #PQS-1
# # write a program to create a dictionary of hindi words with values as their english translation, provide user with an option to look it up!
# lang ={
#     "english" : "hello evryone",
#     "odiya" : "bholo aocho ki",
#     "telugu" : "ela unnaru guru",
#     "hindi" : "kese ho"
# }

# voice = input("enter your language : ")
# print(lang[voice])

# #PQS-2
# # write a program by taking 5 input from the user and print unipue values ?

# user_name = set()
# ads = int(input("enter your 1st value :"))
# user_name.add(ads)

# ads = int(input("enter your 2st value :"))
# user_name.add(ads)

# ads = int(input("enter your 3st value :"))
# user_name.add(ads)
 
# ads = int(input("enter your 4st value :"))
# user_name.add(ads)

# ads = int(input("enter your 5st value :"))
# user_name.add(ads)

# print(user_name)


# #PQS-3
# #write a empty dictionary and alows friends to add their favorite colour as ther values,  name as their key, and print the dictionary?
# fav_item = {}

# name = input("enter your name :")
# colour = input("enter your favorite colour")

# fav_item.update({name : colour})
# print(fav_item)

# #PQS-4
# #write a program to find gratest of four numbers input by the user?

# uv1 = int(input("enter your 1st mark :"))


# uv2 = int(input("enter your 2st mark :"))


# uv3 = int(input("enter your 3st mark :"))

# uv4 = int(input("enter your 4st mark :"))

# if(uv1>uv2 & uv1>uv3 & uv1>uv4):
#     print("user_values1 is greatest :", uv1)
# elif(uv2>uv1 & uv2>uv3 & uv2>uv4):
#     print("user_values2 is greatest :", uv2)
# elif(uv3>uv1 & uv3>uv2 & uv3>uv4):
#     print("user_values3 is greatest :", uv3)
# else:
#     print("user_values4 is greatest :", uv4)

# #PQS-5
# #write program to print the multiplication table of a given number input by the user?

# number_multi_table = int(input("enter your requerd number multiplication table number : "))

# for i in range(1,11):
#     print(f"{number_multi_table} x {i} = {number_multi_table*i}")

# #PQS-6
# # write a program to great the user start with "s"letter ?
# name_list = ["harry","seera", "suraj"]

# for i in name_list:
#     if(i.startswith("s")):
#         print(f"hello, {i}")

# #PQS-7
#  #write program  USEING while to print the multiplication table of a given number input by the user?
# number_m = int(input("enter youur number : "))
# idx = 0
# while( idx<11):
#     print(f"{number_m} x {idx} = {number_m*idx}")
#     idx+=1
# #PQS -8
# #write a program to print prime numbers given by the user 2 numbers?

# number_1 = int(input("enter your 1st num :"))


# for i in range(1,number_1):
#     if(i%2 == 0):
#         print("it is not prime")
#     else:
#         print("prime")

#PQS-9
# write a program to find factorial of n useing for loop?

fact = int(input())

product = 0
for i in range(1,fact+1):
    product += i
print(f"factorial of {fact} is: {product}")


