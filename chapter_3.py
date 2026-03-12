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