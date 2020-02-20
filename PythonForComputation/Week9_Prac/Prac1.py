class Container():
    def __init__(self):
        self.elements = []

    @property
    def size(self):
        return len(self.elements)

    @property
    def isEmpty(self):
        return True if self.size == 0 else False

    def __str__(self):
        return str(self.elements)


class Stack(Container):
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[self.size - 1]


stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
print(stack.size)
print(str(stack))
while not stack.isEmpty:
    a = stack.pop()
    print(a)


class Queue(Container):
    def enqueue(self, element):
        self.elements.insert(0, element)

    def dequeue(self):
        return self.elements.pop()

    def front(self):
        return self.elements[self.size - 1]


queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.size)
print(str(queue))
while not queue.isEmpty:
    b = queue.dequeue()
    print(b)
print(queue.size)
