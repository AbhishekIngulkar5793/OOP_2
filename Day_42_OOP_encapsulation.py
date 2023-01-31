"""
Encapsulation in python:
- Wrapping of variables and methods together in a single
  container which is a class.
- In simple words, it/s a Data hiding.
===============================================
class Sample:
    x = 10

    def m1(self):
        print('m1')
print(x) # x and m1 is hidden from outside world
m1()
=====================================
public string place = 'Pune'

private int pin = 4545

- In other programming languages they have access modifiers
  to implement Encapsulation.
Example:
public [available to all]
private [available only inside a class]
protected [available to the class and to its Child class]
--------------------------------------
- In python we don/t have access modifiers, but
  we can implement above properties using _ underscore convention.
- public means: a variable or a method without _(underscore)
- protected means: a variable or method with _(underscore)
- private means: a var. or method with __(double underscore)
--------------------------------------------------------
class Bank:
    # public var. Place
    place = 'Pune'

    # protected var. IFSC
    _ifsc = 'SBI223344'

    # private var. password
    __password = '1234'

b = Bank()
print(b.place)
print(b._ifsc)
print(dir(b))
# print(b.__password)
# private member will be available only inside a class
# or within a class we can access private member
# BUT if we want to access a private member using an object
# then, use name mangling technique: we use a class in protected
# mode with desired __variable
print(b._Bank__password)

output:

Pune
SBI223344
['_Bank__password', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_ifsc', 'place']
1234

Process finished with exit code 0
===============================================
class Sample:
    def m1(self):
        print('Public method')

    def _m2(self):
        print('protected method')

    def __m3(self):
        print('private method')

s = Sample()
s.m1()
s._m2()
# s.__m3()
print(dir(s))
s._Sample__m3()

output:

Public method
protected method
['_Sample__m3', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_m2', 'm1']
private method

Process finished with exit code 0
==========================================
Method overriding:
- When we have a parent child relationship
- means simply we have inheritance
  and
- Parent class + child class contains method with same name
  Then,
- A method of a child overrides the method in parent class
------------------------------------------------
class Father:
    def money(self):
        print('Monet from Father')

class Chlid(Father):
    def money(self):
        print('My own salary')

c = Chlid()
c.money()

output:

My own salary

Process finished with exit code 0
------------------------------------------------




"""
