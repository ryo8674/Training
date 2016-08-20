dic = {"A":"4","E":"3","G":"6","I":"1","O":"0","S":"5","Z":"2"}

str = raw_input()
str.upper()
if len(str) <= 100:
	li = list(str)
	result = []

	for i in li:
		if i in dic:
			i = dic[i]
		result.append(i)
	str2 =''.join(result)

	print str2
else:
	print "Error"