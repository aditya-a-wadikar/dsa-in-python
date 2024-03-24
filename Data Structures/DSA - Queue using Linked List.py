class Node:
    def __init__(self, val, next=None, prev = None):
        self.next = next
        self.val = val
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def __str__(self):
        curr = self.head
        ret_me = []
        while curr:
            ret_me.append(curr.val)
            curr = curr.next
        return f'Queue - {ret_me}'
            

    def enqueue(self, val):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val, prev=self.tail)
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def is_empty(self) -> bool:
        return not self.head

q = Queue()
print(q)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)

print(q)



q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()


print(q)
print(q.is_empty())





"""
Queue Implementation using linked list
"""