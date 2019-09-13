# python2.7 to exec in aix server

import sys
import os

try:
    os.nice(19)
except:
    exit()

bigfile = sys.argv[1]

with open(bigfile) as bf:
   actual_line = bf.readline()
   count_line = 1
   while actual_line:
       print("Line {}: {}".format(count_line, actual_line.strip()))
       actual_line = bf.readline()
       count_line += 1
