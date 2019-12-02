'''least comman subsequent'''

str1 = input("str1 : ")

str2 = input("str2 : ")

LCS = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]


for i in range(1,len(LCS)):
	for j in range(1,len(LCS[i])):
		if str1[j-1] == str2[i-1]:
			LCS[i][j] = LCS[i-1][j-1]+1
		else:
			LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])


print(LCS[-1][-1] )


i,j = len(str2),len(str1)
str_result = ""
# str_result = str1[-1]

while LCS[i][j] != 0:
	if LCS[i-1][j-1] == LCS[i][j]-1:
		i,j = i-1,j-1
		str_result = str_result+str1[j]
	else:
		if LCS[i-1][j] == LCS[i][j]:
			str_result = str_result+str1[j]
			i = i-1
			
		else:
			str_result = str_result+str1[j]
			j = j-1
			


print (str_result[::-1])


