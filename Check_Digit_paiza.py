#coding: utf-8
def validation(s):
	even = 0
	odd = 0
	for i in range(15):
		if i % 2 == 0:
			tmp = 2 * int(s[i])
			if (tmp % 10 != tmp):
			    even += (tmp % 10 + tmp / 10)
			else:
			    even += tmp
		elif i % 2 == 1:
			odd += int(s[i])
	result = 10 - (even + odd) %10
	if result == 10:
	    result = 0
	return result
	 

n = int(raw_input())
if (n > 0 and n <= 100):
	for i in range(n):
		a = raw_input()
		result = validation(a)
		print result
else:
	print "Error"