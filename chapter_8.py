#chapter-8
# functions in python :
# function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
#ex -
def greet(name):
    print(f"hello {name}, how are you")
greet("rudra")

#return statement :
def add(a,b):
    return a+b
result = add(10,20)
print(result)

#recrsion :
# recursion is a process in which a function calls itself directly or indirectly. The main idea behind recursion is to break down a complex problem into smaller, more manageable sub-problems.
#ex -   
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

