#!/usr/bin/env python

from __future__ import print_function
import sys


def is_in(a, b):
    print("?", a, b)
    sys.stdout.flush()
    return sys.stdin.readline().rstrip() == "in"


def guess(first, last):
    # return k given that we know it lies between first and last
    if first == last:
        return first
    else:
        mid = (first + last) // 2
        if is_in(first, mid):
            return guess(first, mid)
        else:
            return guess(mid+1, last)


def main():
    n = int(input())
    print("!", guess(1, n))


if __name__ == "__main__":
    main()
