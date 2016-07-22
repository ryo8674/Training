#!/usr/bin/env python
#-*- coding: utf-8; -*-

import sys

# argvs = sys.argv
# arg = int(argvs[1])

arg = int(input())

def old_primes(arg):
    counter = 0
    primes = [2]
    if arg ==2:
        primes=[]
    def is_prime(arg):
        nonlocal counter
        counter += 1
        if arg % 2 == 0:
            return False
        else:
            for i in range(3, arg, 2):
                counter += 1
                if arg % i == 0:
                    return False
            return True
    for n in range(3, arg):
        if is_prime(n):
            primes.append(n)
        else:
            pass
    print(len(primes))
    # print(primes)
    # print('len:', len(primes))
    # print('counter:', counter)


def main():
    old_primes(arg)


if __name__ == '__main__':
    main()
