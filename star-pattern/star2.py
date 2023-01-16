#Centred Pyramid

n=int(input("Enter number of rows: "))
for a in range(0, n):
	print(" "*(n-a-1), end="") #print n-a-1 gaps and then in same line
	print("*"*(2*a+1), end="") # print 2*a+1 stars and then in same line
	print(" "*(n-a-1))          # print n-a-1 gaps
	                           ## This loop will run n times
	                          


