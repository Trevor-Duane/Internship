class Animal(object):
    pass

#Dog is an animal so, its a subclass of animal

class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):

        self.name = name

class Person(object):

    def __init__(self, name):

        self.name = name
        #person has a pet of some kind
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

#rover is  a dog

rover = Dog("Rover")

#satan is a cat

satan = Cat("Satan")

#mary is a person

mary = Person("Mary")

#mary owns a pet


mary.pet = satan

#frank is an employee
frank = Employee("Frank", 120000)

#frank owns a pet

frank.pet = rover

#flipper is a fish

flipper = Fish()
