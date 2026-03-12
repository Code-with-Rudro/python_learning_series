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