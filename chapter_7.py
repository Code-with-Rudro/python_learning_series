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








 #chapter-7
#PQS-5
#write program to print the multiplication table of a given number input by the user?

number_multi_table = int(input("enter your requerd number multiplication table number : "))

for i in range(1,11):
    print(f"{number_multi_table} x {i} = {number_multi_table*i}")

#PQS-6
# write a program to great the user start with "s"letter ?
name_list = ["harry","seera", "suraj"]

for i in name_list:
    if(i.startswith("s")):
        print(f"hello, {i}")

#PQS-7
 #write program  USEING while to print the multiplication table of a given number input by the user?
number_m = int(input("enter youur number : "))
idx = 0
while( idx<11):
    print(f"{number_m} x {idx} = {number_m*idx}")
    idx+=1
#PQS -8
#write a program to print prime numbers given by the user 2 numbers?

number_1 = int(input("enter your 1st num :"))


for i in range(1,number_1):
    if(i%2 == 0):
        print("it is not prime")
    else:
        print("prime")

# PQS-9
# write a program to find factorial of n useing for loop?

fact = int(input())

product = 0
for i in range(1,fact+1):
    product += i
print(f"factorial of {fact} is: {product}")

# PQS-10
"""
write a program to print the pattern given below :
    *
   ***
  *****
 *******
"""
n = int(input())

for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

# PQS-11
"""write a program to print the pattern given below :
  * * *
  *   *
  * * *      n=3
"""
for i in range(1,n+1):
  if(i==1 or i==n):
    print("*"*n, end="")
  else:
    print("*",end="")
    print(" "*(n-2), end="")
    print("*",end ="")
  print("")

   