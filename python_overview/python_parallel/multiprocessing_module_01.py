import os
from multiprocessing import Process

'''
(multiprocess) Process is a program (e.g. Python) in execution and provides all resources to execute it
    Runs in own virtual memory address space
    Has executable code, handles to system objects, a security context, a unique process identifier, environment variables …
    Has at least one thread (main thread)

One program may involve several processes.

(threading) Thread
    ‘Lightweight process’, can be thought of as subtasks of a process that can run in parallel
    Shares all resources, e.g., memory, with other threads of the same process


'''


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print('\t{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))

if __name__ == '__main__':
    '''
    This is really similar to our threading module examples, but here we trigger actual processes for each task
    We make a list of processes by adding each proc into procs, procs.append(proc)
    then we start the process, that will run our doubler function
    
    '''
    numbers = [5, 10, 15, 20, 25]
    procs = []
    print('Initializing processes...')
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start() # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start
    print('Starting Processes:')
    for proc in procs:
        proc.join()

# Reference: https://dzone.com/articles/python-201-a-tutorial-on-threads