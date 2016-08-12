input_lines = raw_input()
i = input_lines.split()
i = map(int,i)
if (i >=1 and i <= 100):
	i.append(i)
print max(i)