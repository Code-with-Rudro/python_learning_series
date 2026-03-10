# #chapter-1
# # day-1 python learning seties
# import string


# print("hello world")
# print("hello")
# # hello
# # variables
# a=10
# b=20
# c=a*b
# print(c)

# #STRINGS :
# a = 10  # a is a integer 

# b = 2.5 # b is a floating point

# c = True # c is a boolean

# d = None # d is a none value

# e = "rudra" # e is a string

# #chapter-2
# #day - 2

# print(type(a))

# #input function
# name = input("enter your name")
# print (f"hello : {name}")


# #CHAPTER-3
# # day-3 python learning series
# #strings in python :

# # we can use (``), (""), ("""    """)

# str="rudra"
# print(str[3])

# #str[str_idx: end_idx]

# #nagative slicing :

# print(str[-2: -1])

# # skip value in string 

# # print(str[st_idx:end_idx:skip_size])

# print(str[0:4:1])


# # string functions :
# #length
# print(len(str))

# # ESCAPE sequences in python : 
# # \n : new line
# # \t : tab space
# #\ : escape character
# #\': single quote
# #\\ : backslash
# print("heloo every one \n my self rudra \t \"i\" am learning python \n\t by code with harry")

# #CHAPTER 4
# # day-4 python learning series
# # LIST METHOD      |    TUPLE METHOD

# #list method :
# #list is a container it will store diffrent type of data type, list are mutable(changeable),
# list1 = ["harry", "kiran", 3, True]
# #methods
# #append 
# print(list1.append("rudra"))
# #remove
# print(list1.remove("kiran"))
# #pop()
# print(list1.pop(2))
# #short
# list2  = [1,20,3,4,54,7,11]
# list2.sort()
# print(list2)


# #tuple method :
# #tuple is a container it will store diffrent type of data type, tuple are immutable(unchangeable),
# list3 = ("pramod", "gorav", 542, False)

# print(list3)

# #chapter -5 
# # day-5 python learning series  
# # Dictionary :
# # dictionary is a container it will store data in key value pair, dictionary are mutable(changeable),
# #ex -
# mark = {
#     "kiran" : 10,
#     "rudra" : 20,
#     "pramod" : 22
# }
# print(mark)

# # properties of dictionary :
# # 1. it is unordered,
# # 2. it is mutable,
# # 3. it is indexed,
# # 4. cannoct containe duplicate values.

# #empty dictionary :
# empty_dict = {}

# # dictionary methods :
# # 1.items()
# mark.items()

# #keys()
# mark.keys()

# #values()
# mark.values()

# #update()
# mark.update({"kiran": "siva"})

# print(mark.get("kiran")) # print none
# print(mark["pramod"]) # it print error
# print(mark["kiran"])

# #Set in python :
# # set is a container it will store diffrent type of data type, set are immutable(unchangeable), set are unordered, set cannot contain duplicate values.
# #ex - 
# s = {1,2,"jeneel",True}
# #empty set :
# empty_set = set()

# # properties of sets :-

#     # 1. set are unordered
#     # 2. set are unindexed
#     # 3. there is no way to change items in sets.
#     # 4. set are cannot containe duplicate values.


# # Set methods :

# #add() helps to add 
# set1={10,20,30,40,"rudra"}

# set1.add(2)
# print(set1)

# #union():-
# st1 = {1,2,3,4}
# st2 = {3,4,5,6,7}
# print(st1.union(st2))

# #intersectuon :-
# print(st1.intersection(st2))

# #chapter -6
# #conditional statements :
# # conditional statements are used to perform different actions based on different conditions.
# #relational operators :

# #    1. == : equal to
# #    2. != : not equal to
# #    3. < : less than
# #    4. > : greater than
# #    5. <= : less than or equal to
# #    6. >= : greater than or equal to

# #logical operators :
# #    1. and : returns true if both statements are true
# #    2. or : returns true if one of the statements is true  
# #    3. not : reverse the result, returns false if the result is true

# #ex - 
# employe = int(input("enter your lucky number :"))

# if(employe >= 10):
#     print("sorry bro your got regected ",employe)
# elif(employe>=5):
#     print("your miss just by small mistake",employe)
# elif(employe<5):
#     print("yha your gues the correct ",employe)
# else:
#    print("not goood choice",employe)

# #chapter-7
# # loops in python :
# # for loop :
# # for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# #ex -
# for i in range(1,11):
#     print(i)

# # while loop :
# # while loop is used to execute a block of code as long as the condition is true.   
# #ex -
# i = 1
# while i<=10:
#     print(i)
#     i+=1
# #break statement :
# # The break statement is used to exit the loop when a certain condition is met. It can be used in both for and while loops.
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)
# #continue statement :
# # The continue statement is used to skip the current iteration of the loop and move to the next iteration. It can be used in both for and while loops.
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
# #pass statement :
# # The pass statement is used as a placeholder for future code. It does nothing and is used when a statement is required syntactically but no code needs to be executed.
# for i in range(1,11):
#     if i == 5:
#         pass
#     print(i)

# #chapter-8
# # functions in python :
# # function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# #ex -
# def greet(name):
#     print(f"hello {name}, how are you")
# greet("rudra")

# #return statement :
# def add(a,b):
#     return a+b
# result = add(10,20)
# print(result)

# #recrsion :
# # recursion is a process in which a function calls itself directly or indirectly. The main idea behind recursion is to break down a complex problem into smaller, more manageable sub-problems.
# #ex -   
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


#chapter-9
# file handling in python :
# file handling is a process of reading and writing files. Python provides built-in functions to handle files.
#ex -
# open a file in write mode

st = "this is my fisrt file handling program in python"
file = open("example.txt", "w")
file.write(st)
file.close()