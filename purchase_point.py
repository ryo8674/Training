
# 0:food:5pt/100
# 1:book:3pt/100
# 2:wear:2pt/100
# 3:other:1pt/100

n = int(raw_input())
point = 0
genre = 0
price = 0

if n >= 1 and n <= 1000:
    for i in range(n):
        input_lines = raw_input()
        input_lines = input_lines.split()
        genre = int(input_lines[0])
        price = int(input_lines[1])
        if price % 10 == 0 and (price >= 10 and price <= 10000):
            if genre == 0:
                point += ((price/100)*5)
            elif genre == 1:
                point += ((price/100)*3)
            elif genre == 2:
                point += ((price/100)*2)
            elif genre == 3:
                point += (price/100)
            else:
                point += 0
        else:
            point += 0
        # print genre,price,i,point
    print point
else:
    print "Error"
