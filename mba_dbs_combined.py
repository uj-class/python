
from dbs_module import dbs
from mba_module import mba

# let the user decide - mba or dba

def compute():
	option = input("Enter mba or dbs: ")

	a = int( input("enter 1st number:") )
	b = int( input("enter 2nd number:") )

	if(option == "mba"):
		var = mba(a, b)
	else:
		var = dbs(a, b)


	print(f"The result is: {var}")

cont = "yes"
while cont == "yes":
	compute()
	cont=input("Do you want to continue: (yes/no)")
	if cont == "yes":
		print("continuing...")
