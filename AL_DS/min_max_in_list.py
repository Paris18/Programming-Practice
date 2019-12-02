n = [20,10,18,53,16,8,21]

mx_prfit = 0
min_val = n[0]
max_val = n[1]
min_day = n[0]

for i in range(1,len(n)):
	if n[i] - min_val > mx_prfit:
		mx_prfit = n[i]-min_val
		max_val = n[i]
		min_day = min_val

	elif(n[i]<min_val):
		min_val = n[i]

print(mx_prfit,min_day,max_val)