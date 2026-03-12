#chapter-9
# file handling in python :
# file handling is a process of reading and writing files. Python provides built-in functions to handle files.
#ex -
# open a file in write mode

# st = "this is my fisrt file handling program in python"
# file = open("example.txt", "w")
# file.write(st)
# file.close()

# open a file in read mode

f = open("example.txt", "r")
data = f.read()
print(data)
f.close()

#we can written this with usuing "with" in py:

with open("example.txt") as f:
    print(f.read())
 #here we don't use close model

#r - is used to write the file
#ex -
f = open("example.txt", "r")
data = f.read()
print(data)
f.close()
#  w - is used to write the file
f = open("example.txt", "w")
f.write("this is a new line")
f.close()

# a - is used to append the file
f = open("example.txt", "a")
f.write("\nthis is a new line") 
f.close()
# x - is used to create a new file and write the file
f = open("newfile.txt", "x")
f.write("this is a new file")
f.close()
# t - is used to open the file in text mode
f = open("example.txt", "rt")
data = f.read() 
print(data)
f.close()
# b - is used to open the file in binary mode
f = open("example.txt", "rb")
data = f.read()
print(data)
f.close()








#chapter-9


# #pqs-1
# #write a program to check the content "hello" in the test file or not?
st1 = "hello world i am hero"
f1 = open("poem.txt","w")
f1.write(st1)
f1.close()


f = open("poem.txt")
exist = f.read()
if("hello" in exist):
    print("the hello word exests in the text file")
else:
    print("the hello word is not exests in the text file")
f.close()

# pqs-2
# write a program to store high score in a text file and update it when user get higher score than the previous one?
# the program write in @hiscore_file_game.py file
# pass

# pqs-3
# the program write in @file_io_test.py file
#pass

