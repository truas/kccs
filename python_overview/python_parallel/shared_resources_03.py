
import threading
total = 0
lock = threading.RLock()   # threading.RLock()

def do_something():
    with lock:
        print('Lock acquired in the do_something function')
    print('Lock released in the do_something function')
    return "Done doing something"

def do_something_else():
    with lock:
        print('Lock acquired in the do_something_else function')
    print('Lock released in the do_something_else function')
    return "Finished something else"

def main():
    '''
    If you try to run the code it will hang because of the locking thread placed on do_something().
    When do_something else tries to execute the resource is locked so there is no way to initialize it.
    In fact each function is locking the resource already in main()

    So when we call the first function, it finds that the lock is already held and blocks.
    The same follows for the second function.

    It will continue to block until the lock is released, which will never happen
    '''
    with lock:
        result_one = do_something()
        result_two = do_something_else()
    print(result_one)
    print(result_two)

    '''
     Change line 4 from lock = threading.Lock()   to lock = threading.RLock()
     this should allow the threads to release the resource so it can lock it again.
      
     Reference: https://docs.python.org/3/library/threading.html#threading.RLock
    '''


if __name__ == '__main__':
    main()

# If you want to see multiple threads uncomment the following block

# if __name__ == '__main__':
#     for i in range(10):
#         my_thread = threading.Thread(
#             target=main)
#         my_thread.start()

# Reference for the code: https://dzone.com/articles/python-201-a-tutorial-on-threads from Michael Driscoll
