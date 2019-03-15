import sys

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

	@property
	def print_Database_perItem(self):
		print("|    {} |  {} | ")
		pass	

package_Database = []	
	 
def main():
	#package_Database = []
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
		print("printing out database")
		show_package(package_Database)
	elif val == 2:
		print("option 2")
	elif val == 3:
		print("option 3")
	elif val == 4:
		print("option 4")
	elif val == 5:
		print("option 5")
	elif val == 6:
		print("option 6")
		sys.exit()
	else:
		print("Wrong option, please try again")

def show_package(package_Database):
	call_printTopLable()
	for x in  package_Database:
		print()
	pass

	print("----------------------------------------------------------------------")

def call_printTopLable():
	print("----------------------------------------------------------------------")
	print("|TRACKING #|    TYPE | SPECIFICATION |      CLASS |  WEIGHT | VOLUME |")
	print("----------------------------------------------------------------------")

if __name__ == '__main__':
	main()