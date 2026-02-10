# 1. LINKED LIST (Dynamic)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2. STACK (LIFO)
stack = []
stack.append("A") # Push
stack.pop()        # Pop

# 3. QUEUE (FIFO)
from collections import deque
queue = deque(["Task1", "Task2"])
queue.popleft() # Dequeue
