#pqs-2  file handling   chapter-9
word = "donkey"

with open("io_test.txt", "r") as f:
   content = f.read()

contentnew = content.replace(word, "#####")

with open("io_test.txt", "w") as f:
   print(f.write(contentnew))


#pqs-3
#change a list in the text file?
words = ["help","hope","me"]

with open("io_test.txt") as f:
   conten = f.read()

cont = conten.replace(word, "@@@@@"*len(words))
with open("io_test.txt", "w") as f:
   f.write(cont)