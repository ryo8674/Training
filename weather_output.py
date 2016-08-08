#coding: utf-8

input_line = int(raw_input())

if input_line >= 0 and input_line <= 100:
	if input_line <= 30:
		print "sunny"
	elif input_line <= 70:
		print "cloudy"
	else:
		print "rainy"
else:
	print "Error"