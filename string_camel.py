def capitalize(c):
	return(chr(ord(c)-32))

print("enter the words:")
s = input()

i = 0
for e in s:
	if i == 0:
		#capitalize(e)
		print(capitalize(e))
	else:
		print(e)
	
