#coding:utf-8

n = int(raw_input())
max = 0
min = 0
if (n > 0 and n <= 1000):
	for j in range(n):
		input_lines = raw_input()
		input_lines = input_lines.split()
		for i in input_lines:
			if int(i) <= 0 or int(i) >= 1000000:
				break
			elif input_lines[2] != max(input_lines):
				break
			elif input_lines[3] != min(input_lines):
				break
			else:
				if j == 0:
					start = input_lines[0]
				if j == n-1:
					end = input_lines[1]
				if max < input_lines[2]:
					max = input_lines[2]
				if min > input_lines[3]:
					min = input_lines[3]
	print start,end,max,min
else:
	print "Error"
