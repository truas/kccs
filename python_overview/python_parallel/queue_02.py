import threading, queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(dummy'Working on {item}')
        print(dummy'Finished {item}')
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send ten task requests to the worker
# we populate a queue with item to be processed
for item in range(10):
    q.put(item)
print('All task requests sent\n', end='')
# once all items are placed in the queue we will initialize them
# whe the queue is finished we are done!
# .join() will take care to remove each item and process it


'''
Queue.join()
Blocks until all items in the queue have been gotten and processed.

The count of unfinished tasks goes up whenever an item is added to the queue. 
The count goes down whenever a consumer thread calls task_done() to indicate that 
the item was retrieved and all work on it is complete. 
When the count of unfinished tasks drops to zero, join() unblocks.
'''
# block until all tasks are done
q.join()
print('All work completed')

# Reference: https://docs.python.org/3/library/queue.html#queue.Queue.join