import datetime
class Person:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    def show(self):
        print(f'{self.name} is {self.height} and has {self.weight}kg and {self.age}years old.')

    @classmethod
    def from_birth(cls, name, height, weight, age):
        return cls(name, height, weight, datetime.datetime.now().year - age)

    @staticmethod
    def is_adult(age):
        if age < 18:
            print('No')
        else :
            print('Yes')

p1 = Person.from_birth('asal',151,60,2003)
Person.is_adult(12)
p1.show()