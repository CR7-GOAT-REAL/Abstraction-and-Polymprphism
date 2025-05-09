#abstraction
from abc import ABC, abstractmethod
class Abs(ABC):

  def print(self, x):
    print("The value is: ", x)

  @abstractmethod
  def task(self):
    print("we are inside Abstract class task ")

#create subclass
class Test(Abs):
  def task(self):
    print("We are inside Test class task")

test_obj = Test()
test_obj.task()
test_obj.print(204)




#animal human abstraction
from abc import ABC, abstractmethod
class Animal(ABC):


  def move(self):
      pass

class Human(Animal):
  def move(self):
      print("I can walk and run")
    
class Snake(Animal):
  def move(self):
      print("I can slither")

class Dog(Animal):
  def move(self):
      print("I can bark")

class Lion(Animal):
  def move(self):
      print("I can roar")

h1 = Human()
h1.move()

s1 = Snake()
s1.move()

d1 = Dog()
d1.move()

l1 = Lion()
l1.move()




#polymorphism
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")

#class 2
class USA():
  def capital(self):
      print("Washington D.C is the capital of USA.")
  def language(self):
      print("English is the most widely spoken language of USA.")
  def type(self):
      print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()