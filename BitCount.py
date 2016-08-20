# coding:utf-8
from collections import Counter

input_lines = raw_input()
input_lines = input_lines.split()
n = int(input_lines[0])
m = int(input_lines[1])
result = 0

if (n >= 0 and n <= 100000) and (m >= 0 and m <= 17):
    #0 - n -> binary
    for i in range(n+1):
        counter = Counter(str(bin(i)))
        if counter['1'] == m:
            result += 1
    print result

else:
    print "Error"
