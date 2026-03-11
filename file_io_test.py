word = "donkey"

with open("poem.txt", "r") as f:
   content = f.read()

contentnew = content.replace(word, "#####")

with open("poem.txt", "w") as f:
   f.write(contentnew)