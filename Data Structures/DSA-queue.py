# queue using linked list
class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class Queue:
    def __init__(self, val):
        self.head = self.tail = Node(val)
        print(f'Original Queue - ', [val], '\n')

    # checkers
    def can_pop(self) -> bool:
        if self.head == self.tail:
            return False
        return True

    # read operations
    def show(self):
        queue = []
        tnode = self.head
        while tnode:
            queue.append(tnode.val)
            tnode = tnode.next
        print('Queue -',queue, '\n')

    # create operations
    def push(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        print(f'pushed value {val}')

    def pop(self):
        if self.can_pop():
            prev = self.tail.prev
            prev.next = None
            self.tail.prev = None
            popped_val = self.tail.val
            self.tail = prev
            print(f'popped value {popped_val}')
        else:
            print(f'cannot pop value')





q = Queue(1)

q.push(2)
q.push(3)
q.show()

q.pop()
q.pop()
q.pop()
q.show()

