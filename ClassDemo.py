'''
Main OOP Concept
Object Oriented Programming

1. Class
    - It is a group of different type of data and function.

2. Object
    - It is a instance of class.

3. Inheritance
    - The Object of one class can aquire the properties of object of another class
    is called inheritance.
    - Creating a new class from an existing class is called inheritance.
    1. Single
    2. Multilevel
    3. Multiple
    4. Hierarchical
    5. Hybrid

4. Polymorphism: ONE NAME MULTIPLE FORM :

    1. Compile Time Polymorphism - (Method Overloading) - When there is more
    than one method in a single class having the same name but with different
    number of arguments then it is called method overloading/Compile Time
    Polymorphism.
    2. Run Time Polymorphism - (Method Overriding) - When there is a same method
    prototype in your both base class and derived class and if you call that method
    using the object of derived class, then only derived class method will be called.
    So you can say that method of derived class overrides method of base class.

5. Abstraction : Data Hiding

6. Encapsulation : To bind a data and code into a single unit is called encapsulation.

'''

class Student:
    def getData(self,fname,lname):
        print("getData called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("putData called")
        print("First name : ",self.f)
        print("Last name : ",self.l)

s1=Student()
s1.getData("Rahul","Nambiar")
s1.putData()

