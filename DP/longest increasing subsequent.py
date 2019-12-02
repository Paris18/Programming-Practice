input_list = [int(i) for i in (input("list for longest subsequent list : ").split(" "))]

long_subsq_list = [[i] for i in input_list]

number_long_subsq_list = [1 for i in input_list]

i = 0
while(i < len(input_list)):
	j = 0
	while(j<i):
		if (input_list[j] < input_list[i] and (number_long_subsq_list[j]+1) > number_long_subsq_list[i]):
			number_long_subsq_list[i] = number_long_subsq_list[j]+1
			long_subsq_list[i] = long_subsq_list[j]+[input_list[i]]
		j += 1
	i += 1


for i in range(len(long_subsq_list)):
	print (input_list[i],long_subsq_list[i],number_long_subsq_list[i])

