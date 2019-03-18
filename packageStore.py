import sys
import pickle
from pathlib import Path

class Package:
	def __init__(self, tracking, pacType, spec, mailingClass, weight, volume):
		self._packageTracking = tracking
		self._packageType = pacType
		self._packageSpec = spec
		self._packageMailingClass = mailingClass
		self._packageWeight = weight
		self._packageVolume = volume

	@property
	def packageTracking(self):
		return self._packageTracking

	@property
	def packageType(self):
		return self._packageType

	@property
	def packageSpec(self):
		return self._packageSpec

	@property
	def packageMailingClass(self):
		return self._packageMailingClass
	
	@property
	def packageWeight(self):
		return self._packageVolume

	#@property
	def print_Database_perItem(self):
		print("| {0:>9}| {1:>8}| {2:>14}| {3:>11}| {4:>7} |{5:>6}|".format(self._packageTracking, self._packageType,
			self._packageSpec,self._packageMailingClass,self._packageWeight, self._packageVolume))	

package_Database = []	
	 
def main():
	#package_Database = []
	check_ifFileExist()
	while True:
		call_DisplayMenu()
print("Exting program, GoodBye")
		
def call_DisplayMenu():

	print("Welcome to the Package Store.")
	print("1. Print out the Database")
	print("2. Add add to the Database")
	print("3. Delete from the Database")
	print("4. Search for a package (given its tracking number)")
	print("5. Show a list of packages withina given weight range")
	print("6. Exit program, GoodBye")
	call_Validate()

def call_Validate():
	loop = True
	while loop:
		try:
			val = int(input("Please select from the following options above: "))
			loop = False
		except ValueError:
			print("Invalid Input, try again")
	call_Switch(val)

def call_Switch(val):
	if val == 1:
		print("Printing all packages in the database")
		show_package(package_Database)
	elif val == 2:
		print("Adding a package to the database")
		call_AddPackage()
	elif val == 3:
		print("Deleting package from the database")
	elif val == 4:
		print("Searching for package in the database")
	elif val == 5:
		print("Showing all packages with in wieght range")
	elif val == 6:
		print("Saving data to the database and closing program")
		pickle_stuff()
		sys.exit()
	else:
		print("Wrong option, please try again")


def check_ifFileExist():    
    config = Path('C:\\Users\\ttostado\\Documents\\GitHub\\Python\\dbseri')
    if config.is_file():
        print("files exists, tranfering data to local db")
        unpickle_stuff()


def pickle_stuff():
    print("starting pickling process")
    dbfile = open('dbseri', 'ab')  
    pickle.dump(package_Database, dbfile)
    dbfile.close() 
    print("pickling was successful")

def unpickle_stuff():
    print("starting to unpickle")
    f = open('dbseri', 'rb')
    package_Database = pickle.load(f)
    print("unpickling was successful")
    # print("printing info from database")
    # for obj in db:
    #      print(obj.name)

def show_package(package_Database):
	call_printTopLable()
	for obj in package_Database:
		obj.print_Database_perItem()
		
	print("----------------------------------------------------------------------")

def call_printTopLable():
	print("----------------------------------------------------------------------")
	print("|TRACKING #|    TYPE | SPECIFICATION |      CLASS |  WEIGHT | VOLUME |")
	print("----------------------------------------------------------------------")

def call_AddPackage():
	trackingNum = input("Please enter the package tracking number: ")
	packageType = input("Please enter the package type: ")
	packageSpec = input("Please enter the package specification: ")
	packageClass = input("Please enter the package class: ")
	packageWeight = input("Please enter the package weight: ")
	packageVolume = input("Please enter the package volume: ")
	call_ValidatePackageInfo(trackingNum,packageType,packageClass,packageWeight,packageVolume)
	package_Database.append(Package(trackingNum,packageType,packageSpec,packageClass,packageWeight,packageVolume))

def call_ValidatePackageInfo(trackingNum,packageType,packageClass,packageWeight,packageVolume):
	pass
	
if __name__ == "__main__":
	main()
#| {0:>9}| {1:>8}| {2:>14}| {3:>11}| {4:>7} |{5:>6}| format outputing