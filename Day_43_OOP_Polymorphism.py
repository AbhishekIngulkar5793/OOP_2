"""
Polymorphism:
- It is a combination of two words: i. poly means many
                                    ii. morph means forms
- One norm shows multiple forms, then its a polymorphism
- Best Example of polymorphism is: 'Human Nature'
Example of a string
-------------------------------------------
===========================================
a = '123'
b = '456'
print(a + b) # performs concatenation
c = 3
print(a * c) # performs repetition

print(123 + 456) # performs addition

op->

123456
123123123
579

Process finished with exit code 0
==================================================
class Sample:
    def m1(self):
        print('Empty')
    def m1(self, a, b):
        print('With 2 vars./args.')
    def m1(self, x, y, z):
        print('With 3 vars./args.')

s = Sample()
s.m1(1, 2, 3)

op->

With 3 vars./args.

Process finished with exit code 0
=============================================
class Sample:
    def m1(self, *args):
        print(sum(args))

s = Sample()
s.m1()
s.m1(10,20)
s.m1(3.5, 5.5, 4.5)
s.m1(11, 22, 33, 44, 55, 66, 77)

op->

0
30
13.5
308

Process finished with exit code 0
================================================
overloading:
def add(a, b):
    print(a + b)
def add(x, y, z):
    print(x + y + z)

add(10, 20, 30) # allowed because of last recent call
add(1, 2) # not allowed because of the last recent call
            in which 3 argument values required.

Types of Polymorphism :
1. Method Level Poly./ Method OverLoading:
- A method with same name and different arguments

Example:
class Sample:
    def m1(self):
        print('Empty')
    def m1(self, a, b):
        print('With 2 args')
    def m1(self, x, y, z):
        print('With 3 args')
---------------------------------------
- In above, only last m1 with x, y, z will be available to use
  because its the recent one
==================================================

Constructor overloading:
- It is also not possible in Python

class Sample:
    def __int__(self):
        print('Empty')
    def __init__(self, a, b):
        print('With a and b')
# Sample() its not possible
Sample(5, 6)

op->

With a and b

Process finished with exit code 0
===============================================
Operator overloading:
- It is the only possible type of overloading
-String operation:

a = '123'
b = '456'
print(a + b) # performs concatenation
c = 3
print(a * c) # performs repetition

print(123 + 456) # performs addition

op->

123456
123123123
579

Process finished with exit code 0
==============================================
- In above case ' + Operator ' shows different behaviour
===================================================
Q. What is Polymorphism ?
Q. What are different types in it?
Q. What is method level poly./method overloading?
Q. What is constructor level poly./constructor overloading?
Q. Is above 2 overloading are possible?
Q. What is operator poly./operator overloading?
=========================================================
"""
