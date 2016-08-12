# coding: utf-8
#input : n
#		 "answer correct answer"
#output : point

import difflib
def dif_count(l):
	count = 0
	for i in l:
		if "+" in i:
			count += 1
	return count

input_lines = int(raw_input())
point = 0
d = difflib.Differ()

if (input_lines >= 1 and input_lines <= 1000):
	for i in range(input_lines):
		input_words = raw_input()
		input_words = input_words.split()
		dif = list(d.compare(input_words[0],input_words[1]))
		if len(input_words[0])==len(input_words[1]):
			if (input_words[0]==input_words[1]):
				point += 2
			elif dif_count(dif)==1:
				point += 1
	print point

else:
	print("Error")
