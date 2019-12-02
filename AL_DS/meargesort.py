lista = [int(i) for i in input("").split(" ")]


def mergesort(arry):
	if(len(arry) > 1):
		mid = len(arry)//2
		L = arry[:mid]
		R = arry[mid:]

		mergesort(L)
		mergesort(R)

		i = j = k = 0

		while (i < len(L) > 0 and j <len(R)):

			if(L[i] < R[j]):
				arry[k] = L[i]
				i += 1

			else:
				arry[k] = R[j]
				j +=1 
			k += 1

		while(i <len(L)):
			arry[k] = L[i]
			k += 1
			i += 1
		while(j < len(R)):
			arry[k] = R[j]
			k += 1
			j += 1

mergesort(lista)
print(lista)


