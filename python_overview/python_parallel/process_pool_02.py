# ref: https://stackoverflow.com/questions/20887555/dead-simple-example-of-using-multiprocessing-queue-pool-and-locking
# ref: https://docs.python.org/dev/library/multiprocessing.html

import multiprocessing
import time

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)

def mp_worker(data):
    '''
    We use each data[] element as a pair of  process ane and the amount out time it will be processing something
        In our case we just put it to sleep
        After the time is over we release the process
    '''
    inputs, the_time = data
    print("Processs %s\tWaiting %s seconds" % (inputs, the_time))
    time.sleep(int(the_time))
    print("Process %s\tDONE" % inputs)

def mp_handler():
    p = multiprocessing.Pool(4)
    '''
    Our resource pool has only four processes, so even though data[] has a larger number of processes
        only 4 processes at a time will be running concurrently. 
        The .map() controls which data is mapped to each process available
    '''
    p.map(mp_worker, data)

if __name__ == '__main__':
    mp_handler()
