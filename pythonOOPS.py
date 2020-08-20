# We generally use class method to create factory methods.
# Factory methods return class object (similar to a constructor) for different use cases.
# We generally use static methods to create utility functions.

# Creates class Car
class Car:

    # create class attributes
    name = "c200"
    make = "mercedez"
    model = 2008
    car_count = 0

    def __init__(self):
        Car.car_count +=1
        print(Car.car_count)

    # create class methods
    def start(self, name, make, model):
        print ("Engine started")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    @classmethod
    def stop(self):
        Car.car_count += 1
        print ("Engine switched off")

    @staticmethod
    def get_class_details():
        print('This is a static car class')
        Car.car_count += 1
        print(Car.car_count)

    @staticmethod
    def get_squares(a, b):
        return a * a, b * b

    def __str__(self):
        return 'Car class object'

# print(Car.get_squares(3, 5))

# Creates car_a object of Car class
car_a = Car()
# print(car_a)

# Creates car_b object of car class
car_b = Car()

# car_a.start("Corrola", "Toyota", 2015)
# print(car_a.name)
# print(car_a.car_count)
#
# car_b.start("City", "Honda", 2013)
# print(car_b.name)
# print(car_b.car_count)

# Car.get_class_details()
# Python program to demonstrate
# use of class method and static method.



## STATIC vs CLASS METHOD
# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         # a class method to create a Person object by birth year.
#
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def fromBirthYea(name, year):
#         return (name, date.today().year - year)
#
#         # a static method to check if a Person is adult or not.
#
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
#
# print(person1.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(22))