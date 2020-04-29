'''
the queue library provides an easy implementation od queues. We have to standard architectures
FIFO - First-In-First-Out
LIFO - Last-In-First-Out
'''

# FIFO
import queue

q = queue.Queue()
'''
By default the queue implementation uses First-In-First-Out (FIFO)
    So, the first element to enter our queue will be the one to get out when we pick them
'''
print('FIFO Queue - INSERT')
for i in range(5):
    print('\tPlacing item {} in the queue'.format(i))
    q.put(i)

print('FIFO Queue - REMOVE')
while not q.empty():
    print('\tRemoving item {} from the queue'.format(q.get()))

# LIFO
import queue

q = queue.LifoQueue()
'''
In a LIFO implementation the last element to enter the queue will be the first one to get out.
'''
print('\nLIFO Queue - INSERT')
for i in range(5):
    print('\tPlacing item {} in the queue'.format(i))
    q.put(i)

print('LIFO Queue - REMOVE')
while not q.empty():
    print('\tRemoving item {} from the queue'.format(q.get()))