def mba(a, b):
#MBA - Multiply by Addition
	x = 0
	i = 0

	while(i < b):
			x = x + a
			i += 1

	return x

############################

def dbs(a, b):
#DBS - Divide by Substract

	x = a
	i = 0

	while(x != 0):
			x = x-b
			i += 1
			
	return i

###########################

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

compute()

while 1:
	cont=input("Do you want to continue: (yes/no)")
	if(cont == "yes"):
		compute()
		continue
	else:
		break
	print('continuing...')
