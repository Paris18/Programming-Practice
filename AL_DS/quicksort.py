lista = [int(i) for i in input("").split(" ")]


# def partision

def quicksort(l,low,high):
	j = low
	i = low-1
	pi = high

	while (j < high):
		if l[j] < l[pi]:
			i += 1
			l[i],l[j] = l[j],l[i]
		j += 1

	if (low < high):
		i += 1
		l[i],l[pi] = l[pi],l[i]
		quicksort(l,i+1,high)
		quicksort(l,low,i-1)

	return l


'''


def partision(l,low,high):
	i = low-1
	pi = l[high]

	for j in range(low,high):
		if l[j] < pi:
			i += 1
			l[i],l[j] = l[j],l[i]

	i += 1
	l[i],l[high] = pi,l[i]
	return i

def quicksort(l,low,high):
	if (low < high):
		i = partision(l,low,high)
		quicksort(l,i+1,high)
		quicksort(l,low,i-1)

	# return l
quicksort(lista,0,len(lista)-1)

for i in lista:
	print(i,end=" ")

'''


print(quicksort(lista,0,len(lista)-1))

