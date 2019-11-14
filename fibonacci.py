
n = int(input("Number To Find fibonacci : "))
F = [ None for i in range(n+1)]

def fibo(num):
	if F[num] == None:
		if num <= 1:
			F[num] = num
		else:
			F[num] = fibo(num-1)+fibo(num-2)
	return F[num]


print (fibo(n))






