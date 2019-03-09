def main():
	loop = True
	while loop:
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
	val = input("Please select from the following options above")

	if val == 1:
		print("option 1")
	elif val == 2:
		print("option 2")
	elif val == 3:
		print("option 2")
	elif val == 4:
		print("option 4")
	elif val == 5:
		print("option 5")
	elif val == 6:
		print("option 6")
		loop = false
	else:
		print("Wrong option, please try again")


	


if __name__ == '__main__':
	main()