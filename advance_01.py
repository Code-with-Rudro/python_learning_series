#Chapter-12

#Advance Python Programming

#walrus operator:
#The walrus operator (:=) is a new assignment expression introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression. This can be useful for reducing code redundancy and improving readability.
#ex-
# without walrus operator
n = int(input("Enter a number: "))
if n > 10:
    print(f"{n} is greater than 10")

# with walrus operator
if (n := int(input("Enter a number: "))) > 10:
    print(f"{n} is greater than 10")


#types definations:
#type hints are added using the colon(:) syn for variable and the -> syn for function return tyoe.

# ex:-

from typing import List 

numbers : list[int] = [1,2,3,4]

print(numbers)

#this annotations helps to making the code self documenting and allow devlopers to understand the data structures used at a glance.


#MATCH catch :
# its involvs matching a variable against several cases using this "case " keyword.
# match catch is a powerful tool for handling complex data structures and control flow in a more readable and maintainable way.

def status(st):
    match st:
        case 100:
            return "lower value"
        case 200:
            return "middle value"
        case 500:
            return "higher value"
        case _:
            return "none"

print(status(100))



#dictionary merging:
#In python 3.9 and later, you can merge two dictionaries using the | operator. This allows you to combine the key-value pairs of two dictionaries into a single dictionary.
# ex-
dict1 = {"a": 1,"b":2}
dict2 = {"c": 3,"d":4}
merged_dict = dict1 | dict2
print(merged_dict)



# with statement: 
#The with statement is used to wrap the execution of a block of code with methods defined by a context manager. This allows you to manage resources such as file handling, database connections, and locks in a more efficient and cleaner way. The with statement ensures that the resources are properly acquired and released, even if an error occurs within the block.


#ex:
try:

    with(
       open("hiscore.txt") as f1,
       open("io_test.txt") as f2

):

       hiscore = f1.read()
       io_test = f2.read()
    print(hiscore)
    print(io_test)
except FileNotFoundError:
       print("not found")

#exception handling:
#Exception handling is a mechanism in Python to handle errors and exceptions that may occur during the execution of a program. It allows you to gracefully handle errors and prevent your program from crashing. The main components of exception handling in Python are try, except, else, and finally blocks.
#ex:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    print(f"The result of {num1} divided by {num2} is {result}.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")

#exception handling allows you to write more robust and error-resistant code by anticipating and managing potential errors that may arise during program execution.

#except block can be used to catch specific exceptions and handle them accordingly, while the else block can be used to execute code that should only run if no exceptions were raised. The finally block is useful for cleaning up resources or performing actions that must occur regardless of whether an exception was raised or not.
#else block is executed only if the try block does not raise an exception. It is used to specify code that should run when the try block succeeds without any errors. The else block is optional and can be omitted if not needed.
#finally block is executed regardless of whether an exception was raised or not. It is typically used for cleanup actions, such as closing files or releasing resources, that must occur regardless of the outcome of the try block. The finally block is optional and can be omitted if not needed.


#if __name__ == "__main__":
#The if __name__ == "__main__": is a common idiom in Python that is used to check whether a script is being run directly or imported as a module. When a Python script is run, the special variable __name__ is set to "__main__". If the script is imported as a module, __name__ is set to the name of the module. By using this condition, you can ensure that certain code only runs when the script is executed directly, and not when it is imported as a module in another script. This is often used to include test code or to prevent certain code from running when the script is imported.
#ex:

def func():
    print("hello my friends")
    if __name__ == "__main__":
        print("we arre running main dircty")
        func()
        print(__name__)
print(__name__)

#global keyword:
#The global keyword in Python is used to declare that a variable inside a function is global, meaning it can be accessed and modified outside of the function. By default, variables defined inside a function are local to that function and cannot be accessed outside of it. However, by using the global keyword, you can indicate that a variable should be treated as a global variable, allowing you to read and modify its value from within the function.
#ex:
x = 10
def modify_global():
    global x
    x += 5
    print(f"Inside function, x = {x}")
modify_global()
print(f"Outside function, x = {x}")


#enumerate function:
#The enumerate function in Python is a built-in function that allows you to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of the current item. It returns an enumerate object that produces pairs of index and value for each item in the sequence. This can be useful when you need to access both the index and the value of items during iteration.
#ex:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")


#list comprehension:
#List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for list comprehension is [expression for item in iterable if condition]. This can make your code more readable and efficient compared to using traditional loops for creating lists.
#ex:
squares = [x**2 for x in range(10)]
print(squares)
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)




#chapter-12
#practice questions:
# pqs-1

#write a code useing enumirate function to print table of n and stored in a table.txt file.

n= int(input("enter your number for table: "))

table1 = [n*i for i in range(1,11)]

with open("table.txt", "a") as f1:
    f1.write(f"the table of {n} is : {str(table1)}\n")

print(f"the table of {n} is : {str(table1)}\n")
