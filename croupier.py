#!/usr/bin/env python
'Cross-connect stdin and stdout of 2 processes and show outputs from each.'

from __future__ import print_function

import os
import sys
import shlex
import subprocess
import threading
import argparse

def transfer_and_print(fd1, fd2, name='', fobj=None):
    'Transfer data from fd1 to fd2 and print to fobj'
    output_buffer = bytearray()
    while(True):
        ch = os.read(fd1, 1000)
        if ch == b'':
            break
        os.write(fd2, ch)
        output_buffer += ch
        if fobj is not None and ch[-1:] == b'\n':
            try:
                s = output_buffer.decode()
            except UnicodeDecodeError:
                s = str(bytes(output_buffer))
            s = s[:-1]
            if name:
                print("{}: {}".format(name, s), file=fobj)
            else:
                print(s, file=fobj)
            output_buffer = bytearray()

def logged_pipe(name='', fobj=None):
    if fobj is None:
        return os.pipe()
    else:
        fd1, write_end = os.pipe()
        read_end, fd2 = os.pipe()
        thread = threading.Thread(target=(lambda: transfer_and_print(fd1, fd2, name, fobj)))
        thread.daemon = True
        thread.start()
        return (read_end, write_end)

def interact(pstr1, pstr2, name1='A', name2='B', fobj=None):
    pargs1 = shlex.split(pstr1)
    pargs2 = shlex.split(pstr2)
    a_to_b = logged_pipe(name1, fobj)
    b_to_a = logged_pipe(name2, fobj)
    pa = subprocess.Popen(pargs1, stdin=b_to_a[0], stdout=a_to_b[1])
    pb = subprocess.Popen(pargs2, stdin=a_to_b[0], stdout=b_to_a[1])
    pa.wait()
    pb.wait()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('proc1', help='Command line of 1st process')
    parser.add_argument('proc2', help='Command line of 2nd process')
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
        help="Don't print output from processes")
    parser.add_argument('--name1', default='A', help='Name of 1st process')
    parser.add_argument('--name2', default='B', help='Name of 2nd process')
    args = parser.parse_args()
    fobj = None if args.quiet else sys.stdout

    interact(args.proc1, args.proc2, args.name1, args.name2, fobj)

if __name__ == '__main__':
    main()
