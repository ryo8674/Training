#coding: utf-8
input_map = raw_input()
input_start = raw_input()
input_map = input_map.split()
input_start = input_start.split()
w = int(input_map[0]) - 1
h = int(input_map[1]) - 1
n = int(input_map[2])
x = int(input_start[0])
y = int(input_start[1])
for i in range(n):
	input_act = raw_input()
	input_act = input_act.split()
	act_dir = input_act[0]
	act_val = int(input_act[1])
	if act_dir == "U":
		y += act_val
		if y > h:
			y = y - h - 1
	elif act_dir == "D":
		y -= act_val
		if y < 0:
			y = y + w + 1
	elif act_dir == "R":
		x += act_val
		if x > w:
			x = x - w - 1
	elif act_dir == "L":
		x -= act_val
		if x < 0:
			x = x + w + 1
print x,y