
#####
# Step 6 - Parallel processing
#####

# I use parallel processing largely with functions. Parallel processing works by running multiple copies of the code
# but has drawbacks, such as you cannot work on the same dataset due to file read-write locks, and in some cases,
# particularly with arcpy, you cannot work in the same folder. Hence, you may need to create subfolders to work in.

# This is a very basic example of parallel processing, but it should show you the power of the tool.

import multiprocessing
import time

print "Number of CPU cores available: ", multiprocessing.cpu_count()

# From Stackoverflow: https://stackoverflow.com/questions/20887555/dead-simple-example-of-using-multiprocessing-queue-pool-and-locking

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)

def mp_worker((inputs, the_time)):
    print " Processs %s\tWaiting %s seconds" % (inputs, the_time)
    time.sleep(int(the_time))
    print " Process %s\tDONE" % inputs

def mp_handler():
    p = multiprocessing.Pool(2)#Change 2 to the number of cpu cores available - 1
    p.map(mp_worker, data)

if __name__ == '__main__':
    mp_handler()

