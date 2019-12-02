

def palindromeSubStrs(s): 
	m = dict() 
	n = len(s) 
  
	# table for storing results (2 rows for odd- 
	# and even-length palindromes 
	R = [[0 for x in range(n+1)] for x in range(2)] 

	print(R)

	# s = '@'+s+'$'
	temp=''
	for i in range(n):
		temp += '#'+s[i]

	temp = '@'+temp+'#$'

	R = [0 for x in range(len(temp))]

	C = L = H = mirr = 0

	for i in range(1,len(temp)-1):
		mirr = 2*C - i

		if i < H:
			R[i] = min(H-i,R[mirr])
			# R[i] = R[mirr]

		while (temp[i+(1+R[i])] == temp[i-(1+R[i])]):
			if ((temp[i+(1+R[i])]) != "#"):
				print (temp[i+(1+R[i])],temp[i-(1+R[i])],temp[i])
			R[i] += 1

		if ((i+R[i]) > H):
			C = i
			H = i+R[i]


		# print(temp[i],R[i])
	# print (R)
	# using zip() to map values 
	mapped = zip(temp, R) 
	  
	# converting values to print as set 
	mapped = set(mapped) 
	print(mapped)



palindromeSubStrs("ababababa") 
# print(help())