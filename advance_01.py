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
# 

#ex:
with(
    open("hiscore.txt") as f1,
    open("io_test.txt") as f2

):
    hiscore = f1.read()
    io_test = f2.read()
print(hiscore)
print(io_test)
