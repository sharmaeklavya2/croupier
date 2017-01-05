#!/usr/bin/env python

"""Run croupier on guessing game with different parameters
and store the output in files in a directory."""

from __future__ import print_function
import os
import subprocess
import argparse


try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, 'wb')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CROUPIER_PATH = os.path.join(BASE_DIR, 'croupier.py')
GUESS_GAME_PATH = os.path.join(BASE_DIR, 'samples', 'guess')
SOLUTION_PATH = os.path.join(GUESS_GAME_PATH, 'solution.py')
JUDGE_PATH = os.path.join(GUESS_GAME_PATH, 'judge.py')

file_label_args = [
    ('default', []),
    ('empty', ['--name1=', '--name2=']),
    ('named', ['--name1=player', '--name2=computer']),
]


def create_output(dirpath):
    try:
        os.makedirs(dirpath)
    except OSError:
        pass
    for fname, label_args in file_label_args:
        with open(os.path.join(dirpath, fname + '_100.txt'), 'w') as fobj:
            solution_args = 'python {}'.format(SOLUTION_PATH)
            judge_args = 'python {} -n 100 -k 25'.format(JUDGE_PATH)
            args = ['python', CROUPIER_PATH,
                    solution_args, judge_args] + label_args
            subprocess.check_call(args, stderr=DEVNULL, stdout=fobj)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', help='path to output directory')
    args = parser.parse_args()

    create_output(args.dir)


if __name__ == '__main__':
    main()
