#coding:utf-8
seg = {"1111110":0,"0110000":1,"1101101":2,"1111001":3,"0110011":4,
"1011011":5,"1011111":6,"1110010":7,"1111111":8,"1111011":9}

#0,8,1,5,2,3,4,6,7,9,1
lst_mirror=["1111110","1111111","0110000","1101101","1011011","1001111",
"0100111","1111101","1100110","1101111","0000110"]
#0,1,2,5,6,9,3,8,4,7,1
lst_rot = ["1111110","0110000","1101101","1011011","1111011","1011111",
"1111001","1111111","0010111","0011110","0000110"]

a = raw_input()
a = a.strip()
a = a.replace(" ","")
b = raw_input()
b = b.strip()
b = b.replace(" ","")

if (a in seg) and (b in seg):
	print "Yes"
else:
	print "No"
if (a in lst_mirror) and (b in lst_mirror):
	print "Yes"
else:
	print "No"
if (a in lst_rot) and (b in lst_rot):
	print "Yes"
else:
	print "No"
