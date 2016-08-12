# coding: utf-8
#input :n
#output :"*" n times

from __future__ import print_function

input_lines = int(raw_input())

if (input_lines >= 1 and input_lines <= 100):
	for i in range(input_lines):
		print("*",end="")
	print("\n")
else:
	print("Error")
