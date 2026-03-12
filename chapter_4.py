#CHAPTER 4
# day-4 python learning series
# LIST METHOD      |    TUPLE METHOD

#list method :
#list is a container it will store diffrent type of data type, list are mutable(changeable),
list1 = ["harry", "kiran", 3, True]
#methods
#append 
print(list1.append("rudra"))
#remove
print(list1.remove("kiran"))
#pop()
print(list1.pop(2))
#short
list2  = [1,20,3,4,54,7,11]
list2.sort()
print(list2)


#tuple method :
#tuple is a container it will store diffrent type of data type, tuple are immutable(unchangeable),
list3 = ("pramod", "gorav", 542, False)

print(list3)







#chapter-4
#PQS-1
#store 7 frouts ina list given by the user?
fruit = []
a = input("enter your 1st frute name :")
fruit.append(a)
a = input("enter your 2st frute name :")
fruit.append(a)
a = input("enter your 3st frute name :")
fruit.append(a)
a = input("enter your 4st frute name :")
fruit.append(a)
a = input("enter your 5st frute name :")
fruit.append(a)
a = input("enter your 6st frute name :")
fruit.append(a)
a = input("enter your 7st frute name :")
fruit.append(a)
print(fruit)

#PQS-2
#sorted the 6 student mark input given by the user ?

student = []
st = int(input("enter the 1st student mark :"))
student.append(st)
st = int(input("enter the 2st student mark :"))
student.append(st)
st = int(input("enter the 3st student mark :"))
student.append(st)
st = int(input("enter the 4st student mark :"))
student.append(st)
st = int(input("enter the 5st student mark :"))
student.append(st)
st = int(input("enter the 6st student mark :"))
student.append(st)

print(student)
student.sort()
print(f"sorted student mark : {student}")

#PQS-3
# check the tuple is iommutable or not 
# tuple =(1,2,3,4,)
# tuple.append(5) # it will give error because tuple is immutable
# print(tuple)

#PQS -4
# SUM of tudent mark ?
print(f"sum of student marks : {sum(student)}")
#PQS-5
#count the 10 in student mark ?
print(f"count the 10 in student list: {student.count(10)}")

