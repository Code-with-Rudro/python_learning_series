#chapter-1
# day-1 python learning seties
import string


print("hello world")
print("hello")
# hello
# variables
a=10
b=20
c=a*b
print(c)

#STRINGS :
a = 10  # a is a integer 

b = 2.5 # b is a floating point

c = True # c is a boolean

d = None # d is a none value

e = "rudra" # e is a string

#chapter-2
#day - 2

print(type(a))

#input function
name = input("enter your name")
print (f"hello : {name}")


#CHAPTER-3
# day-3 python learning series
#strings in python :

# we can use (``), (""), ("""    """)

str="rudra"
print(str[3])

#str[str_idx: end_idx]

#nagative slicing :

print(str[-2: -1])

# skip value in string 

# print(str[st_idx:end_idx:skip_size])

print(str[0:4:1])


# string functions :
#length
print(len(str))

# ESCAPE sequences in python : 
# \n : new line
# \t : tab space
#\ : escape character
#\': single quote
#\\ : backslash
print("heloo every one \n my self rudra \t \"i\" am learning python \n\t by code with harry")

#CHAPTER 4
# day-4 python learning series
# LIST METHOD      |    TUPLE METHOD

#list method :
#list is a container it will store diffrent type of data type, list are mutable(changeable),
list1 = ["harry", "kiran", 3, True]
#methods
#append 
print(list1.append("rudra"))
#remove
print(list1.remove("kiran"))
#pop()
print(list1.pop(2))
#short
list2  = [1,20,3,4,54,7,11]
list2.sort()
print(list2)


#tuple method :
#tuple is a container it will store diffrent type of data type, tuple are immutable(unchangeable),
list3 = ("pramod", "gorav", 542, False)

print(list3)

#chapter -5 
# day-5 python learning series  
# Dictionary :
# dictionary is a container it will store data in key value pair, dictionary are mutable(changeable),
#ex -
mark = {
    "kiran" : 10,
    "rudra" : 20,
    "pramod" : 22
}
print(mark)

# properties of dictionary :
# 1. it is unordered,
# 2. it is mutable,
# 3. it is indexed,
# 4. cannoct containe duplicate values.

#empty dictionary :
empty_dict = {}

# dictionary methods :
# 1.items()
mark.items()

#keys()
mark.keys()

#values()
mark.values()

#update()
mark.update({"kiran": "siva"})

print(mark.get("kiran")) # print none
print(mark["pramod"]) # it print error
print(mark["kiran"])

