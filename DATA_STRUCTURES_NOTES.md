DATA STRUCTURE CLASSIFICATION AND APPLICATIONS

Data structures are divided into two broad categories:
a)Primitive Data Structures
Examples: Integer, Float, Character, String, Boolean
Code Illustration (Python):
num = 42          # Integer
pi = 3.14         # Float
letter = 'A'      # Character
name = "Dancun"   # String
flag = True       # Boolean

2. Non-Primitive Data Structures
Linear – Static: Array
Fixed size, contiguous memory.
Pythonclass StaticArray:
    def __init__(self, size):
        self.data = [None] * size
        self.count = 0

    def insert(self, val, idx):
        if 0 <= idx < len(self.data) and self.count < len(self.data):
            self.data[idx] = val
            self.count += 1

    def traverse(self):
        return [x for x in self.data if x is not None]

arr = StaticArray(5)
arr.insert(10, 0)
arr.insert(20, 2)
print(arr.traverse())  # [10, 20]
Used for: pixel grids, lookup tables
Reason: O(1) random access
Linear – Dynamic: Linked List
Pythonclass Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def display(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res

ll = LinkedList()
ll.append(10)
ll.append(20)
print(ll.display())  # [10, 20]
Used for: playlists, browser history
Reason: dynamic size, fast insert/delete
Linear – Dynamic: Stack (LIFO)
Pythonclass Stack:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None

s = Stack()
s.push("Back")
s.push("Forward")
print(s.peek())  # Forward
print(s.pop())   # Forward
Used for: undo, function call stack
Reason: natural last-in-first-out
Linear – Dynamic: Queue (FIFO)
Pythonfrom collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, item): self.q.append(item)
    def dequeue(self): return self.q.popleft() if self.q else None

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1
Used for: print queue, task scheduling
Reason: first-in-first-out order
Non-Linear: Tree
Pythonclass TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
inorder(root)  # 2 1 3
Used for: file folders, organization charts
Reason: represents hierarchy
Non-Linear: Graph
Pythonclass Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def display(self): return self.adj

g = Graph()
g.add_edge("Nairobi", "Mombasa")
g.add_edge("Nairobi", "Kisumu")
print(g.display())
Used for: maps, social connections
Reason: models any relationship
