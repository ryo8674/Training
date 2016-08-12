#coding:utf-8
n = int(raw_input())
count_s = 0
count_b = 0

for i in range(n):
	s = raw_input()
	if s == "strike":
		count_s += 1
		if count_s == 3:
			count_s = 0
			print "out!"
			break
		else:
			print "strike!"
	elif s == "ball": 
		count_b += 1
		if count_b == 4:
			count_b = 0
			print "fourball!"
			break
		else:
			print "ball!"
	else:
		print "Error"
