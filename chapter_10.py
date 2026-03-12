#CHAPTER-10
# object-oriented programming in python :
# object-oriented programming is a programming paradigm that uses objects and classes to design and develop applications. It is based on the concept of "objects", which can contain data and code that manipulates that data.

#class and object :
# class is a blueprint for creating objects. An object is an instance of a class. A class can have attributes (data) and methods (functions) that operate on the data. An object can have its own unique attributes and methods, but it also inherits the attributes and methods of the class.
#ex-
class emo:
    name = "rudra"
    age = 18
    salary = 1800000

person = emo()
print(person.name,person.age,person.salary)

#instance variable and class variable :
# instance variable is a variable that is defined inside a method and belongs to the object. It is used to store data that is unique to each object. A class variable is a variable that is defined inside a class and belongs to the class. It is used to store data that is shared among all objects of the class.
#in python we take first instance variable and then class variable.

 
#ex :-

class emp1:
    company = "google" # class variable
    name = "rudra"
    domine = "python"

prsn = emp1()
prsn.age = 18 # instance variable
print(prsn.company,prsn.name, prsn.domine, prsn.age)

prsn2 = emp1()
prsn2.age = 20 # instance variable
print(prsn2.company,prsn2.name, prsn2.domine, prsn2.age)

#self parameter :
# self refers to the instance of the class. It is used to access the attributes and methods of the class in python. It is the first parameter of any method in a class and it is used to refer to the object itself.
#ex -
class emp2:
    company  = "capgemini"
    def info(self):
        print(f"the company name is : {self.company}")

prsn3 = emp2()
prsn3.info()    
print(prsn3.company)
