import random

def gm():
    print("Lets start the math: ")
    score = random.randint(1,99)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"the geeting score is: {score}")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

gm()