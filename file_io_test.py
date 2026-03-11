word = "donkey"

with open("io_test.txt", "r") as f:
   content = f.read()

contentnew = content.replace(word, "#####")

with open("io_test.txt", "w") as f:
   print(f.write(contentnew))