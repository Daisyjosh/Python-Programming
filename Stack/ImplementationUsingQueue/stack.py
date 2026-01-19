# get() => used to remove the element from the queue
# maxsize() => used to put the max number of items allowed in queue
# empty() => return true if queue is not empty else false
# full() => when queue is full return true
# put(x) => it is used to insert x in queue
# qsize() => gives the size of a queue

from queue import LifoQueue

stack = LifoQueue(maxsize=4)

stack.put(0)
stack.put(1)
stack.put(2)
stack.put(3)

print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())
