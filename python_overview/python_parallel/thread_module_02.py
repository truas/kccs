import threading

class MyThread(threading.Thread):
    '''
    Let us have a proper class to initialize our threads
    '''
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        """Run the thread"""
        print(self.getName(), ' Calling doubler')
        doubler(self.number)

def doubler(number):
    """A function that can be used by a thread"""
    print('\tdoubler function executing for: %d' %number)
    result = number * 2
    print('\tdoubler function ended with: {}'.format(result))


if __name__ == '__main__':
    # We are giving names to our threads to identify them
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        thread = MyThread(i)  # for each value in the range we create a thread
        thread.setName(thread_names[i]) # name that thread accordingly
        thread.start()  # execute our thread
'''
run() … specifies the threads activity, i.e. the instructions it should execute
start() … starts the thread’s activity specified in run()
join() … blocks the calling thread (typically the main thread) until the thread whose join() method is called terminates

'''
#Reference for the code: https://www.blog.pythonlibrary.org/2016/07/28/python-201-a-tutorial-on-threads/ from Michael Driscoll