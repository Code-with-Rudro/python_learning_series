#chapter - 11
#inheritance
#types of inheritance
#1. single inheritance
#2. multiple inheritance
#3. multilevel inheritance
#4. hierarchical inheritance
#5. hybrid inheritance

#single inheritance
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
a = A()
a.feature1()
a.feature2()
b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

#multiple inheritance
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B:
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class C(A,B):
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()

#multilevel inheritance
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class C(B):
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")
c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()


#super keyword:
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

#class method and static method in inheritance:
class A:
    e = 10
    ename = "rudra"
   
    def greet():
        print("good morning")
class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
    @classmethod
#@classmethod:
#1. it is a method which is bound to the class and not the object of the class.
#2. it can access the class variables and class methods.


    def show(cls):
        print(cls.e)

    @property
#1. it is a decorator which is used to convert a method into a property.
#2. it is used to access the method like an attribute.

    def show1(self):
        return self.ename
    @show1.setter
#setter is a decorator which is used to set the value of a property.
# it is used to set the value of a property like an attribute.
    def show1(self, name):
        self.fename = name.split()[0]
        self.lname = name.split()[1]


        
        
b = B()
b.e = 20
b.ename = "kiran seera"
print(b.ename)
b.show()


#operator overloading:
# operator overloading is a feature in python that allows us to define the behavior of an operator for a user-defined class. It is done by defining special methods in the class. These special methods are called magic methods or dunder methods.
#types of operator overloading:
#addition operator overloading 
# example: 
# the __add__ method is used to overload the addition operator. It takes two arguments, self and other. The self argument is the instance of the class and the other argument is the instance of the class that we want to add.
#the__mul__ method is used to overload the multiplication operator. It takes two arguments, self and other. The self argument is the instance of the class and the other argument is the instance of the class that we want to multiply.
#the __str__ method is used to overload the string representation of the class. It takes one argument, self. The self argument is the instance of the class. It returns a string representation of the class.
#the __len__ method is used to overload the length of the class. It takes one argument, self. The self argument is the instance of the class. It returns the length of the class.
#the __eq__ method is used to overload the equality operator. It takes two arguments, self and other. The self argument is the instance of the class and the other argument is the instance of the class that we want to compare.
#the __lt__ method is used to overload the less than operator. It takes two arguments, self and other. The self argument is the instance of the class and the other argument is the instance of the class that we want to compare.
#the __gt__ method is used to overload the greater than operator. It takes two arguments, self and other. The self argument is the instance of the class and the other argument is the instance of the class that we want to compare.
#the __sub__ method is used to overload the subtraction operator. It takes two arguments, self and other. The self argument is the instance of the class and the other argument is the instance of the class that we want to subtract.

#ex -
class A:
    def __init__(self,n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
a1 = A(10)
a2 = A(20)
print(a1 + a2)


    
        

        
#chapter-11
#practice questions:
#pqs-1
#write a method salaryafterincriment method with @property decorator with setter which changes the salary of an employee after increment?

class employes:
    salary = 12000
    incriment = 20
    @property
    def salaryafterincriment(self):
        return (self.salary + self.salary *( self.incriment/100))
    @incriment.setter

    def salaryafterincriment(self, salary):
        self.incriment = ((salary - self.salary)-1)*100

emp = employes()
print(emp.salaryafterincriment)
emp.salaryafterincriment = 15000
print(emp.incriment)