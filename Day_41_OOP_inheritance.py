"""
# OOP Features

1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphism

These are the pillars OOP

1. Inheritance :
- It is a property of OOP with which we can form
  a relationship among the classes.
- Where one class can be a parent and another one
  will be a child.
parent --> child

- A class parent is termed as a 'Root class'/ 'Super class'
- Whereas, a child class is termed as  a 'Derived class'/ 'Subclass

Syntax:
class Parent:
    pass
class Child(Parent):
    pass

- In above syntax, child inherited father/parent.
- Hence, child can use the members of a parent class.


Example:
class Father:
    atm_pin = 1234

    def money(self):
        print('Money of father')

class Child(Father):
    pass

# child has to inherit father class
c = Child()
print(c.atm_pin)
1234
Money of father
None

Process finished with exit code 0


output:

1234
Money of father
None

Process finished with exit code 0
---------------------------
==============================
Inheritance is of 5 different types:
1. Simple/Single level
2. Multilevel
3. Multiple
4. Hybrid
5. Hierarchical
-----------------------------------
Simple inheritance:
One Parent and One Child


Example:
class Tree:
    f1 = 'big'
    f2 = 'small'
    def m1(self):
        print('Watering')
    def m2(self):
        print('Cultivation')

class FruitTree(Tree):
    pass

f = FruitTree()
print(f.f1)
f.m1()

output:

big
Watering

Process finished with exit code 0
------------------------------------------------------
Multilevel inheritance:

parent1 --> Child(parent) --> Child

Super_parent --> Parent --> Child

Grand_Father --> Father --> Child
-------------------------------------------
class GrandFather:
    def money(self):
        print('Money from Grandpa')

class Father(GrandFather):
    def money(self):
        print('Money from Father')

class Child(Father):
    def money(self):
        print('My own salary')

c = Child()
c.money()

output:
My own salary

Process finished with exit code 0
--------------------------------------------
class Grandfather:
    def money(self):
        print('Money from Grandpa')

class Father(Grandfather):
    def money(self):
        # super().money()
        print('Money from Father')

class Child(Father):
    def money(self):
        super().money()
        print('My own salary')
        Grandfather.money(self)

c = Child()
c.money()
# How to trace the hierarchy?
# MRO: Method Resolution Order
# It will tell you a sequence of class, how ur method
# will be searched among the classes present
print(Child.mro())

print(Child.__mro__)

output:

Money from Father
My own salary
Money from Grandpa
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Grandfather'>, <class 'object'>]
(<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Grandfather'>, <class 'object'>)

Process finished with exit code 0
--------------------------------------------
Q. What is MRO?
   Why we use it?
   when we use it?
=========================================
3. Multiple inheritance:
- Multiple parents and one or more child.
----------------------------------------------
class Father:

    def m2(self):
        print('m2 from Father')
    def m1(self):
        print('m1 from Father')

class Mother:
    def m1(self):
        print('m1 from Mother')

class Child(Father, Mother):
    pass

c = Child()
c.m1()
c.m2()
print(Child.mro())

output:

m1 from Father
m2 from Father
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]

Process finished with exit code 0
===========================================
class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X, Y):
    pass
class B(Y, Z):
    pass
class C(A, B):
    pass
print(C.mro())

output:

[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.B'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]

Process finished with exit code 0
----------------------------------------------

"""


