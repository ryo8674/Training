#count pair of x and -x
import sys

num =[]
count = 0

for line in sys.stdin:
    i = int(line)
    num.append(i)
    if i*-1 in num:
        count = count + 1
        num.remove(i)
        num.remove(-1*i)

print count
