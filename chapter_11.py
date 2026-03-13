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

