import threading
total = 0
lock = threading.Lock()

def update_total(amount):
    """Updates the total by the given amount"""
    '''
    For each thread using update_local, it will lock the given resource, perform the task and release it
    This will prevent multiple thread accessing the same resource at the same time
    
    The is the same code as our previous example, but using the 'with lock' (pretty much the same thing as open file)
    '''
    global total
    with lock:  # lock.acquire()
        total += amount
        print('\tValue: ', total)


if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        print(my_thread.getName())
        my_thread.start()

# Reference for the code: https://dzone.com/articles/python-201-a-tutorial-on-threads from Michael Driscoll
