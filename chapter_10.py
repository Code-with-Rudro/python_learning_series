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


#static method :
# static methods are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance (self) or the class (cls). They are typically used for utility functions that do not require access to instance or class data.
#ex -
class emp3:
    company = "tcs"
    @staticmethod
    def info1():
        print("this is a static method")
emp3.info1()
print(emp3.company)

#constructor :
# a constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object. In python, the constructor is defined using the __init__ method.
#ex -
class emp4:
    def __init__(self, name, age):
        self.name = name
        self.age = age
emp4_obj = emp4("rudra", 18)
print(emp4_obj.name, emp4_obj.age)







#chapter-10
#practice questions :
# pqs-1
#create a class (programmer) and pritn few proggramer working at microsoft?

class programmer:
    company = "Microsoft"
    def __init__(self, name, lang, salary):
        
       self.name = name 
       self.lang = lang
       self.salary = salary

person01 = programmer("rudra","python",1200000)

print(person01.company,person01.name,person01.lang,person01.salary)

person02 = programmer("kiran","python",2000000)
print(person02.company,person02.name,person02.lang,person02.salary)

print(person01.company,person01.name,person01.lang,person01.salary)

person03= programmer("pramod", "java", 1300000)

print(person03.company,person03.name,person03.lang,person03.salary)


#pqs-2
#create a class (calculator) and print the sum, square, cube of a number?

class calculator:
    def __init__(self, n):
        self.n = n


    def square(self):
        print(f"the square is: {self.n*self.n}")
    def qube(self):
        print(f"the qube is: {self.n*self.n*self.n}")

cl = calculator(5)
cl.square() 
cl.qube()


#pqs-3
#add a static method in the above calculator class to greet the user?

class satic:
    @staticmethod
    def prnt():
        print("hello everyone!")

p = satic()
p.prnt()

#pqs-4
# write a program and create a class (train) to book tickets and getstatus and get fare information?

class train:
    def __init__(self,tr_name,tr_num,tr_price,tr_st,tr_from,tr_to):
        self.tr_name = tr_name
        self.tr_num = tr_num
        self.tr_price = tr_price
        self.tr_st = tr_st
        self.tr_from = tr_from
        self.tr_to = tr_to
    
    def booktc(self):
        print(f"the {self.tr_num} superFast  {self.tr_name} train ticket price {self.tr_price} : booked successfully , thank you for booking, enjoy your journy ")
     
    def getstatus(self):
        print(f"the train number{self.tr_num}, superFast express {self.tr_name} from {self.tr_from} to {self.tr_to} ticket price{self.tr_price}  w/l list is{self.tr_st}, thank you!")
    
    def fare(self):
        print(f"the total price of ticket is : train number {self.tr_num}, superFast {self.tr_name}, ticket price{self.tr_price}, gst {self.tr_price - 1.8}, total {self.tr_price * 1.8}. thank you!")

vandeBharat = train("vande bharat", 25495, 2500, "28 W/l", "vishakhapatnam", "hydrabad")
vandeBharat.booktc()
vandeBharat.getstatus()
vandeBharat.fare()

