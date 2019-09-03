#import multiprocessing as mp,os
import sys 
import os
from multiprocessing import process, Manager, Pool, cpu_count
import multiprocessing

fname = sys.argv[1]
print("Number of cpu : ", cpu_count())
#fname = "input.txt"

def process_wrapper(fname, chunkStart, chunkSize, outfile="b_output.txt"):
    with open(fname) as f:
        f.seek(chunkStart)
        lines = f.read(chunkSize).splitlines()
        for line in lines:
            process(line)
            outfile = open(outfile, 'a')
            outfile.write(line+'\n')  # python will convert \n to os.linesep
            outfile.close()

def chunkify(fname,size=1024*1024):
    fileEnd = os.path.getsize(fname)
    with open(fname,'r') as f:
        chunkEnd = f.tell()
        while True:
            chunkStart = chunkEnd
            f.seek(size,1)
            f.readline()
            chunkEnd = f.tell()
            yield chunkStart, chunkEnd - chunkStart
            if chunkEnd > fileEnd:
                break

#init objects
pool = Pool()
jobs = []

#create jobs
for chunkStart,chunkSize in chunkify(fname):
    jobs.append( pool.apply_async(process_wrapper,(fname, chunkStart,chunkSize)) )

#wait for all jobs to finish
for job in jobs:
    job.wait()

#clean up
pool.close()
