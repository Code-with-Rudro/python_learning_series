#chapter-7
# loops in python :
# for loop :
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#ex -
for i in range(1,11):
    print(i)

# while loop :
# while loop is used to execute a block of code as long as the condition is true.   
#ex -
i = 1
while i<=10:
    print(i)
    i+=1
#break statement :
# The break statement is used to exit the loop when a certain condition is met. It can be used in both for and while loops.
for i in range(1,11):
    if i == 5:
        break
    print(i)
#continue statement :
# The continue statement is used to skip the current iteration of the loop and move to the next iteration. It can be used in both for and while loops.
for i in range(1,11):
    if i == 5:
        continue
    print(i)
#pass statement :
# The pass statement is used as a placeholder for future code. It does nothing and is used when a statement is required syntactically but no code needs to be executed.
for i in range(1,11):
    if i == 5:
        pass
    print(i)
    