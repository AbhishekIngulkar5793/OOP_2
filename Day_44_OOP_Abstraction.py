"""
Abstraction means : Information hiding
# To do Abstraction follow some rules:
- Create a normal class and inherit an ABC class in it.
- ABC means Abstract Base Class
- This ABC is available in the abc module.
- Second rule is: Abstract class contains abstract or
  non-abstract methods.
- Your normal class becomes a full abstract class only
  when it has at least one abstract method.
- How to create an abstract method ?
- Use @abstractmethod decorator above non-abstract method.
- Above decorator we can import from abc Module.
-----------------------------------------------------
from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def transaction(self): # abstract method
        pass

    def details(self): # non-abstract method/ instance method
        print('This is RBI console')
        print('secured one')
--------------------------------------------------
- Once we have an abstract class,
- implementation of its method is must.
- Means, compulsory we need to provide an  implementation
  of abstract method into child class.
- Wherever it may be inherited.
-----------------------------------------------
- We can/t instance abstract class ==> Hum abstract class ka

  object nahi bana sakte.
b = Bank()

"""


