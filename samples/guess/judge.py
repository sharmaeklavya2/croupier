#!/usr/bin/env python

from __future__ import print_function
import sys
import math
import random
import argparse


def exit_with_error(errmsg):
    print("Verdict: Wrong Answer ({})".format(errmsg), file=sys.stderr)
    sys.stderr.flush()
    sys.exit(1)


def exit_with_success(n, moves):
    score = (math.log(n, 2) + 1) / (moves + 1)
    fmtstr = "Verdict: Correct Answer (moves={}, score={})"
    print(fmtstr.format(moves, score), file=sys.stderr)
    sys.stderr.flush()
    sys.exit(0)


NMAX = 10**9


def play(n=NMAX, k=None, seed=None):
    moves = 0
    if seed is not None:
        random.seed(seed)
    k = random.randint(1, n) if k is None else k

    print(n)
    sys.stdout.flush()

    while True:
        words = sys.stdin.readline().split()
        if words[0] == '!' and len(words) == 2:
            try:
                guess = int(words[1])
            except ValueError:
                exit_with_error("Guess was not an integer")
            if guess == k:
                exit_with_success(n, moves)
            else:
                exit_with_error("Guessed {} instead of {}".format(guess, k))
        elif words[0] == '?' and len(words) == 3:
            try:
                a = int(words[1])
                b = int(words[2])
            except ValueError:
                exit_with_error("Parameters are not integers")
            a, b = min(a, b), max(a, b)
            moves += 1
            if a <= k and k <= b:
                print("in", file=sys.stdout)
            else:
                print("out", file=sys.stdout)
            sys.stdout.flush()
        else:
            exit_with_error("Invalid command or number of arguments")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=NMAX,
                        help='maximum number that can be chosen')
    parser.add_argument('-k', type=int, help='number chosen by computer')
    parser.add_argument('--seed', help='seed for the random number generator')
    args = parser.parse_args()

    play(args.n, args.k, args.seed)


if __name__ == '__main__':
    main()
