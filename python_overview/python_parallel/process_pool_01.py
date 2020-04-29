from multiprocessing import Pool # these will allow us to have a pool for our resources
import os

# we create a dummy function so each process can run it
def dummy(x):
    return x * x


if __name__ == '__main__':
    # start 5 workers process
    with Pool(processes=5) as pool:
        # print '[0,1,4,...,]'
        res = pool.apply_async(os.getpid, ())
        print('PID: \t{0} \tPoolname:{1} '.format(res.get(), pool.imap(dummy, range(10))))

        # print same number in arbitrary order
        for i in pool.imap_unordered(dummy, range(10)):
            print('Process running dummy with result: ',i) #simple power function

        # evaluate "dummy(20)" asynchronously
        res = pool.apply_async(dummy, (20,))  # runs in only one process
        print('\tPool Resource from dummy using 20 for one process: ',res.get(timeout=1))  # prints '400'

        # evaluate 'os.getpid()' asynchronously
        res = pool.apply_async(os.getpid, ())  # runs in only one process
        print('PID from our pool being used: ', res.get(timeout=1))  # prints the PID of that process
        # see that his PID will change since each time a new Pool is created

# Reference: https://docs.python.org/3/library/multiprocessing.html
# Reference: Advanced Guide to Python 3 Programming By John Hunt
