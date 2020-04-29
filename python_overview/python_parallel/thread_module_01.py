import threading

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
    A function that can be used by a thread
    """
    print(threading.currentThread().getName() + '\n')
    print('Number: {0} \tValue: {1}'.format(number, str(number * 2)))
    print()

if __name__ == '__main__':
    for i in range(3):
        # Each thread will run the doubler function, using i as the argument
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()

'''
run() … specifies the threads activity, i.e. the instructions it should execute
start() … starts the thread’s activity specified in run()
join() … blocks the calling thread (typically the main thread) until the thread whose join() method is called terminates

'''


#Reference for the code: https://www.blog.pythonlibrary.org/2016/07/28/python-201-a-tutorial-on-threads/ from Michael Driscoll