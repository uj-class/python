def fibonacci(n):
    
	a = 0
	b = 1
	c = 0
	i = n
	list = [] # list to store the fibonacci numbers
	# block for computing the series:
	while i != 0:

			i = i-1
			a = b
			b = c
			list.append(c)
			c = a + b 
			
	return list
