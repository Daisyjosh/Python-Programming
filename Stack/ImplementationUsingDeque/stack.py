from collections import deque

stack = deque()

stack.append("Daisy")
stack.append("was")
stack.append("born")
stack.append("in")
stack.append("November")
print(stack)
print(stack.pop())
print(stack)