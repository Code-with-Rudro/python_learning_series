#chapter -5 
# day-5 python learning series  
# Dictionary :
# dictionary is a container it will store data in key value pair, dictionary are mutable(changeable),
#ex -
mark = {
    "kiran" : 10,
    "rudra" : 20,
    "pramod" : 22
}
print(mark)

# properties of dictionary :
# 1. it is unordered,
# 2. it is mutable,
# 3. it is indexed,
# 4. cannoct containe duplicate values.

#empty dictionary :
empty_dict = {}

# dictionary methods :
# 1.items()
mark.items()

#keys()
mark.keys()

#values()
mark.values()

#update()
mark.update({"kiran": "siva"})

print(mark.get("kiran")) # print none
print(mark["pramod"]) # it print error
print(mark["kiran"])

#Set in python :
# set is a container it will store diffrent type of data type, set are immutable(unchangeable), set are unordered, set cannot contain duplicate values.
#ex - 
s = {1,2,"jeneel",True}
#empty set :
empty_set = set()

# properties of sets :-

    # 1. set are unordered
    # 2. set are unindexed
    # 3. there is no way to change items in sets.
    # 4. set are cannot containe duplicate values.


# Set methods :

#add() helps to add 
set1={10,20,30,40,"rudra"}

set1.add(2)
print(set1)

#union():-
st1 = {1,2,3,4}
st2 = {3,4,5,6,7}
print(st1.union(st2))

#intersectuon :-
print(st1.intersection(st2))






#chapter - 5
#PQS-1
# write a program to create a dictionary of hindi words with values as their english translation, provide user with an option to look it up!
lang ={
    "english" : "hello evryone",
    "odiya" : "bholo aocho ki",
    "telugu" : "ela unnaru guru",
    "hindi" : "kese ho"
}

voice = input("enter your language : ")
print(lang[voice])

#PQS-2
# write a program by taking 5 input from the user and print unipue values ?

user_name = set()
ads = int(input("enter your 1st value :"))
user_name.add(ads)

ads = int(input("enter your 2st value :"))
user_name.add(ads)

ads = int(input("enter your 3st value :"))
user_name.add(ads)
 
ads = int(input("enter your 4st value :"))
user_name.add(ads)

ads = int(input("enter your 5st value :"))
user_name.add(ads)

print(user_name)


#PQS-3
#write a empty dictionary and alows friends to add their favorite colour as ther values,  name as their key, and print the dictionary?
fav_item = {}

name = input("enter your name :")
colour = input("enter your favorite colour")

fav_item.update({name : colour})
print(fav_item)