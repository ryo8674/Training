def validate(mynum):
    if type(mynum) == str:
        if not mynum.isnumeric():
            return "not numeric1"
    elif not type(mynum) == int:
        return "not numeric2"

    mynum = str(mynum)

    digits = list(mynum)
    if(len(digits) != 12):
        return "not length 12"
    check_digit = int(digits.pop())
    #print("digit:" + str(check_digit))

    digits.reverse()
    #print(digits)

    s = 0
    for n in range(1, 12):
        p = int(digits[n-1])
        q = n + 1 if (n<=6) else n - 5
        s += p * q
    #print("sum:" + str(s))
    rem = s % 11
    tgt = rem if(rem <=1) else 11-rem
    #print("rem:" + str(rem))

    if rem <= 1:
        #print("check:0")
        return check_digit == 0
    else:
        #print("check:" + str(11-rem))
        return check_digit == (11 - rem)
