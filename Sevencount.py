#-*- utf-8 -*-#
# python3
def Seven_Cnt(n):
    cnt = 0 #counts of '7' in the number n

    while True:
        order = len(str(n)) - 1
        first_number = n // (10 ** order)
        cnt += first_number * order * 10 ** (order - 1)

        if first_number == 7:
            cnt += n - 7 * 10 ** order + 1
        elif first_number > 7 :
            cnt += 10 ** order
        else:
            cnt += 0 # do nothing

        n = n % (10 ** order)
        if n == 0:
            break

    return int(cnt)

try:
    while True:
        print(Seven_Cnt((int(input().strip().upper()))))
except EOFError:
    pass
