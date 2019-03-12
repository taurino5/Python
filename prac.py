import sys
import time

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def setup_Class():
    print(sys.platform)
    person1 = Person("James", 9)
    print(person1.name, " ", person1.age)
    
if __name__ == "__main__":
    print(time.clock())
    setup_Class()
