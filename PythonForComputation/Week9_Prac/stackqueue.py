class Container(object):
    def __init__(self):
        self.elements = []

    @property
    def size(self):
        return len(self.elements)

    def clear(self):
        self.elements = []

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

    def __str__(self):
        return "<STACK #BOTTOM{}>".format(super(Stack, self).__str__())


class Queue(Container):
    def enqueue(self, element):
        self.elements.insert(0, element)

    def dequeue(self):
        return self.elements.pop()

    def front(self):
        return self.elements[self.size - 1]

    def __str__(self):
        return "<QUEUE #TAIL{}>".format(super(Queue, self).__str__())


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5]

    # Testing Stack
    print("Stack -- first in last out")
    s = Stack()
    for item in alist:
        s.push(item)
    print("The stack:", s)
    print("Pop the items:")
    while not s.isEmpty:
        print(s.pop(), end=" ")

    print("\n\nQueue -- first in first out")
    q = Queue()
    for item in alist:
        q.enqueue(item)
    print("The queue:", q)
    print("Dequeue the items:")
    while not q.isEmpty:
        print(q.dequeue(), end=" ")


def play_stack_Queue(st):
    S = Stack()
    Q = Queue()
    for c in st:
        if c not in "aoeui":
            S.push(c)
        else:
            Q.enqueue(c)
    ret = ""
    for i in range(max(S.size, Q.size)):
        if not S.isEmpty:
            ret += S.pop()
        if not Q.isEmpty:
            ret += Q.dequeue()
    return ret


print("\n******************\n")
print(play_stack_Queue("Stack and Queue"))
