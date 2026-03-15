#chapter-13
#virtual environment:
#virtual environment is a tool that helps to keep the dependencies required by different projects in separate places, by creating virtual python environments for them. it solves the problem of version conflicts between packages and allows you to manage dependencies more efficiently. 


"""
pip install virtualenv
virtualenv env_name
source env_name/bin/activate  # for linux and mac
env_name\Scripts\activate  # for windows

.\env_name\Scripts\activate  # for windows powershell
deactivate  # to exit the virtual environment




#freeze:
#it list out the installed packages in the current environment and their versions. it is useful for sharing the environment with others or for recreating the environment on another machine.   

pip freeze > requirements.txt  # to create a requirements file with the list of installed packages and their versions
pip install -r requirements.txt  # to install the packages listed in the requirements file



#venv:
#venv is a module that comes with python 3.3 and later versions. it provides support for creating lightweight virtual environments with their own site directories, optionally isolated from system site directories. it is a simpler alternative to virtualenv and is included in the standard library.

"""


#lambda function:
#lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. it is often used for short, simple functions that are not worth defining with a full function definition.   

#syntax:
#lambda arguments: expression

#ex -
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8




#join method:
#join method is a string method that takes all items in an iterable and joins them into a single string. it is often used to concatenate a list of strings into a single string with a specified separator.
#syntax:
#separator.join(iterable)

#ex -
my_list = ['Hello', 'World', 'Python']
result = '_'.join(my_list)
print(result)  # Output: "Hello_World_Python"


#map, filter, reduce:

# map:
#map function applies a given function to all items in an iterable and returns a map object (which is an iterator). it is often used to apply a function to each item in a list or other iterable.
#syntax:
#map(function, iterable)
#ex -
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

#filter:
#filter function constructs an iterator from elements of an iterable for which a function returns true. it is often used to filter items in a list or other iterable based on a condition.
#syntax:    
#filter(function, iterable)
#ex -
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

#reduce:
#reduce function applies a rolling computation to sequential pairs of values in an iterable. it is often used to perform a cumulative operation on a list or other iterable, such as summing all the items.
#syntax:
#reduce(function, iterable)
#ex -
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

