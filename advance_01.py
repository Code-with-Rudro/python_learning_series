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
