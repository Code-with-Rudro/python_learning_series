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