import sys
import time
import pickle
from pathlib import Path

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

db = []

def main():
    #check_ifFileExist()
    setup_Class()

def check_ifFileExist():    
    config = Path('C:\\Users\\ttostado\\Documents\\GitHub\\Python\\dbseri')
    if config.is_file():
        print("files exists, tranfering data to local db")
        unpickle_stuff()
    else:
        #dbfile = open('dbseri', 'ab')
        setup_Class()

def setup_Class():
    print(sys.platform)
    person1 = Person("James", 9)
    person2 = Person("Dad", 42)
    print(person1.name, " ", person1.age)
    print("adding name to db")
    db.append(person1)
    db.append(person2)
    pickle_stuff()

def pickle_stuff():
    print("starting pickling process")
    dbfile = open('dbseri', 'ab')  
    pickle.dump(db, dbfile)
    dbfile.close() 
    print("pickling was successful")
    unpickle_stuff()

def unpickle_stuff():
    print("starting to unpickle")
    f = open('dbseri', 'rb')
    db = pickle.load(f)
    print("unpickling was successful")
    print("printing info from database")
    for obj in db:
         print(obj.name)
        
if __name__ == "__main__":
    print(time.clock())
    main()
