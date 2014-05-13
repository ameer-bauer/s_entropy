#!/usr/bin/env python3
#----------------
#Name: s_entropy
#Version: 1.0.1
#Date: 2014-05-12
#----------------
# A quick script to calculate the Shannon Entropy of a file

import sys
import math
import argparse

parser = argparse.ArgumentParser(add_help=False, description='Welcome to s_entropy v1.0.1! A program which calculates the Shannon Entropy of a file.')
parser.add_argument("-h", action='store_true', help="Display verbose help.")
parser.add_argument("-s", action='store_true', help="Enable STREAM MODE, which reads the input file a block at a time.  The default block size is 4096 bytes.")
parser.add_argument("-b", nargs='?', type=int, help="Manually set the block size ,in bytes, for STREAM MODE.", metavar='# bytes')
parser.add_argument("-f", nargs='?', help="Specify an input file to calculate Shannon Entropy for.", metavar='filename')
args = parser.parse_args()

block = 4096

if args.h:
    print('Introduction to s_entropy v1.0.1:')
    print('  The s_entropy program calculates the Shannon Entropy of an input file. The')
    print('  output of this calculation is a number between 0 and 8. Where 0 represents')
    print('  the minimum, and 8 represents the maxium, amount of entropy calculated.')
    print('  For more information on Shannon Entropy please visit the following site:')
    print('    http://www.wikipedia.org/wiki/Entropy_%28information_theory%29')
    print('\nSYNTAX\n  python3 s_entropy.py [-h] [-s] [-b] [-f [filename]]')
    print('\nARGUMENTS')
    print('  -h Displays this help page.')
    print('  -s Enables STREAM MODE, which reads the input file in a block at a time')
    print('     without utilizing much memory. This method is more memory-efficient,')
    print('     allowing for files larger than available system RAM to be processed.')
    print('     The default STREAM MODE block size is 4096 bytes.')
    print('     By default, s_entropy uses RAM MODE, which reads an entire file into')
    print('     RAM before making any calculations.')
    print('  -b Sets the block size for STREAM MODE in bytes.  The default is 4096.')
    print('  -f <filename> Specifies which file to calculate Shannon Entropy for.')
    print('\nEXAMPLES\n  python3 s_entropy.py -f test.rnd')
    print('    Reads in the file test.rnd utilizing RAM MODE and then outputs the name,')
    print('    byte count, and entropy number of the input file test.rnd.')
    print('\n  python3 s_entropy -s -f file.tst')
    print('    Reads in the file file.tst utilizing STREAM MODE in 4k blocks and then')
    print('    returns name, byte count, and entropy number of the input file file.tst.')
    print('\n  python3 s_entropy -s -b 8192 -f file.tst')
    print('    Reads in the file file.tst utilizing STREAM MODE in 8k blocks and then')
    print('    returns name, byte count, and entropy number of the input file file.tst.')
    sys.exit()

if args.f:
    file_name = args.f
    freq_list = [0]*256
    byte_count = 0
    s_ent = 0.0
    with open(file_name, mode = 'rb') as f:
        if args.s:
            if args.b:
                block = args.b
            print ('STREAM MODE')
            print ('  Block Size:', block)
            print ('  Reading File:', file_name)
            while 1:
                stream = f.read(block)
                if not stream:
                    break
                for byte in stream:
                    freq_list [byte] += 1
                    byte_count += 1
        else:
            print ('RAM MODE')
            print ('  Reading File:', file_name)
            for byte in f.read(): #This loop reads the entire file into memory, faster but uses more RAM.
                freq_list [byte] += 1
                byte_count += 1
    for b in freq_list:
        if b > 0:
            p = b / byte_count
            s_ent = s_ent + (p * math.log2(p))
    s_ent = -s_ent
    print ('FILE STATISTICS')
    print ('  File Name:', file_name)
    print ('  Byte Count:', byte_count)
    print ('  Shannon Entropy:', s_ent)
    sys.exit()

parser.print_help()

