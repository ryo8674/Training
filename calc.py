# #add
# add x to y : x+y
# x added to y : y+x
# x plus y : x+y

# #sub
# subtract x from y : y-x
# x minus y : x-y

# #mul
# x times y : x*y
# x multiplied by y : x*y
# twice x : 2*x

# #div 
# divide x by y : x/y
# x divides y : y/x
# half of x : x/2

num ={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,
"eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
"sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90,
"hundred":100,"thousand":1000,"million":1000000}

#input
str_spl = []
l = raw_input()
str_spl=l.split()

x = 0
y = 0
tmp = 0
str_tmp = 0

result = 0

#--------------------ADD---------------------#
# add x to y : x+y
# x added to y : y+x
# x plus y : x+y

if ('added' in l) == True:
	for i in str_spl:
		if i == 'added':
			continue
		if i == 'to':
			result += x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result + x
	

if str_spl[0] == 'add':
	for i in str_spl:
		if i == 'add':
			continue
		if i == 'to':
			result += x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result + x
	

if ('plus' in l) == True:
	for i in str_spl:
		if i == 'plus':
			result += x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result + x
	


#--------------------MIN---------------------#
# subtract x from y : y-x
# x minus y : x-y

if str_spl[0] == 'subtract':
	for i in str_spl:
		if i == 'subtract':
			continue
		if i == 'from':
			result = -x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result + x
	

if ('minus' in l) == True:
	for i in str_spl:
		if i == 'minus':
			result = x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result - x
	

#--------------------MUL---------------------#
# x times y : x*y
# x multiplied by y : x*y
# twice x : 2*x

if ('times' in l) == True:
	for i in str_spl:
		if i == 'times':
			result = x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result * x
	

if ('multiplied' in l) == True:
	for i in str_spl:
		if i == 'multiplied':
			continue
		if i == 'by':
			result += x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result * x
	

if str_spl[0] == 'twice':
	for i in str_spl:
		if i == 'twice':
			continue
		elif(i == 'and'):
			tmp = x
			x = 0
			str_tmp = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x =  num[i] * x
			str_tmp = num[i]
	x = x + tmp
	result = 2*x
	

#--------------------DIV---------------------#
# divide x by y : x/y
# x divides y : y/x
# half of x : x/2

if str_spl[0] == 'divide':
	for i in str_spl:
		if i == 'divide':
			continue
		if i == 'by':
			result = x
			x = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = result / x
	

if ('divides' in l) == True:
	for i in str_spl:
		if i == 'divides':
			x = y
			y = 0
			tmp = 0
			str_tmp = 0
			continue
		if(i == 'and'):
			tmp = y
			y = 0
		 	continue
		else:
			if y == 0:
				y = num[i]
			else:
				if (str_tmp > num[i]):
					y = y + num[i]
				elif (str_tmp < num[i]):
					y = y * num[i]
			str_tmp = num[i]
	y = y + tmp
	result = y / x
	

if str_spl[0] == 'half':
	for i in str_spl:
		if i == 'half':
			continue
		if i == 'of':
			continue		
		if(i == 'and'):
			tmp = x
			x = 0
		 	continue
		else:
			if x == 0:
				x = num[i]
			else:
				if (str_tmp > num[i]):
					x = x + num[i]
				elif (str_tmp < num[i]):
					x = x * num[i]
			str_tmp = num[i]
	x = x + tmp
	result = x/2

print result