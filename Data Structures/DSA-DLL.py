class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self, val):
        self.head = self.tail = Node(val)
        print('indexing starts from 1')
        print('very first linked list -', [val], '\n')

    def check_pointers_correctness(self):
        current = self.head
        while current:
            if current.next and current.next.prev != current:
                return False
            current = current.next
        print('Linked List is correctly linked\n')
        return True

    def show(self) -> list:
        temp = self.head
        ll = []
        while temp:
            ll.append(temp.val)
            temp = temp.next
        print("Linked List -", ll, '\n')
        return ll

    def insertAtBegin(self, val) -> bool:
        new_node = Node(val)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        print(f'inserted {val} at begin')
        return True

    def insertAtIndex(self, val, index):
        if index <= 1:
            self.insertAtBegin(val)
            return

        tnode = self.head
        i = 1
        while i < index - 1 and tnode:
            tnode = tnode.next
            i += 1

        if not tnode or not tnode.next:
            self.insertAtEnd(val)
            return
        else:
            new_node = Node(val)
            new_node.next = tnode.next
            new_node.prev = tnode
            tnode.next = new_node
            print(f'inserted value {val} at index {index}')

    def insertAtEnd(self, val) -> bool:
        new_node = Node(val)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        print(f'inserted {val} at end')

    def updateIndex(self, new_val, index):
        tnode = self.head
        i = 1
        while i < index and tnode:
            tnode = tnode.next
            i += 1

        if tnode:
            old_val = tnode.val
            tnode.val = new_val
            print(f'Updated value {old_val} with {new_val}')
        else:
            print(f'Index {index} out of range')
            return False

    def updateValue(self, old_val, new_val):
        tnode = self.head
        while tnode:
            if tnode.val == old_val:
                tnode.val = new_val
                print(f'updated {old_val} with {new_val}')
                return True
            tnode = tnode.next
        print(f'value {old_val} not found')

    def deleteFirst(self):
        if self.head.next:
            tnode = self.head.next
            del_val = self.head.val
            tnode.prev = None
            self.head.next = None
            self.head = tnode
            print(f'deleted first node of value {del_val}')

    def deleteLast(self):
        if self.head != self.tail:
            tnode = self.tail.prev
            del_val = self.tail.val
            tnode.next = None
            self.tail.prev = None
            self.tail = tnode
            print(f'deleted last node of value {del_val}')

    def deleteIndex(self, index):
        if index == 1:
            self.deleteFirst()
            return
        i = 1
        tnode = self.head
        while i < index and tnode:
            tnode = tnode.next
            i += 1
        if tnode == self.tail:
            self.tail = tnode.prev
            self.tail.next = None
            tnode.prev = None
            print(f'removed value {tnode.val} from linked list')
        else:
            prev = tnode.prev
            next = tnode.next
            prev.next = next
            next.prev = prev
            tnode.prev = None
            tnode.next = None
            print(f'removed value {tnode.val} from linked list')

    def deleteValue(self, value):
        tnode = self.head
        while tnode:
            if tnode.val == value:
                if tnode == self.head:
                    self.deleteFirst()
                elif tnode == self.tail:
                    self.deleteLast()
                else:
                    prev = tnode.prev
                    next = tnode.next
                    prev.next = next
                    next.prev = prev
                    tnode.prev = None
                    tnode.next = None
                    print(f'removed value {value} from linked list')
                return True

            tnode = tnode.next

        print(f'value {value} not found')
        return False


l = DoubleLinkedList(4)

l.insertAtBegin(3)
l.insertAtEnd(5)
l.insertAtEnd(6)
l.insertAtEnd(7)
l.show()

l.insertAtIndex(22,4)
l.show()


l.updateIndex(222, 4)
l.updateValue(8, 444)
l.show()

l.deleteFirst()
l.deleteLast()
l.show()

l.deleteIndex(3)
l.deleteValue(4)
l.show()
