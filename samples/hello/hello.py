#!/usr/bin/env python

from __future__ import print_function
import sys

print("I'm python.")
sys.stdout.flush()
name = sys.stdin.readline().rstrip()[4:-1]
print("Nice to meet you, {}.".format(name))
sys.stdout.flush()
