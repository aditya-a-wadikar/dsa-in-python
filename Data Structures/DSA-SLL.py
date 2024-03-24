# singly linked list node
class Node:
    def __init__(self, val):
        self.val = val
        # .next will show the next Node instance
        self.next = None

# single linked list
class SinglyLinkedList:
    def __init__(self, val):
        self.head = self.tail = Node(val)

    # read
    def show(self):
        ll = []
        temp = self.head
        while temp:
            ll.append(temp.val)
            temp = temp.next
        print('Linked List -',ll, '\n')

    def find(self, val):
        '''return node of given value'''
        temp = self.head
        foundNode = None
        while temp:
            if temp.val == val:
                foundNode = temp
                break         
            temp = temp.next

        return foundNode

    # create
    def insertAtStart(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        print(f'inserted {val} at start')

    def insertAtIndex(self, val, index):
        tindex = 0
        temp = self.head
        while temp and tindex < index-1:
            temp = temp.next
            tindex += 1
        tnode = Node(val)
        tnode.next = temp.next
        temp.next = tnode
        print(f'inserted {val} at index {index}')

    def insertAtEnd(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        print(f'inserted {val} at end')
        

    # update
    def updateStart(self, val):
        print(f'updated start node value with {val}')
        self.head.val = val

    def updateValue(self, old_val, new_val):
        foundNode = self.find(old_val)
        if foundNode:
            foundNode.val = new_val
            print(f'updated value {old_val} with {foundNode.val}')
        else:
            print(f'value {old_val} not found')

    def updateIndex(self, new_val, index):
        i, temp = 0, self.head
        while temp.next and i < index-1:
            temp = temp.next
            i+=1
        old_val = temp.val
        temp.val = new_val
        print(f'updated value {old_val} with {temp.val}')

    def updateEnd(self, val):
        self.tail.val = val
        print(f'updated end node value with {val}')
        
    
    # delete
    def removeAtStart(self):
        if self.head == self.tail:
            print('cannot remove start')
        else:
            thead = self.head
            self.head = self.head.next
            thead.next = None
            print(f'removed the first node {thead.val}')
            del thead

    def removeAtIndex(self, index:int):
        if index == 1:
            self.removeAtStart()
        
        else:
            temp = self.head
            i = 1
            while i < index-1 and temp:
                temp = temp.next
                i+=1
            
            del_me = temp.next
            temp.next = temp.next.next
            print(f'removed value {del_me.val} from index {index}')
            del del_me

        
    def removeAtValue(self, val:int):
        temp = self.head
        del_me = None
        while temp.next:
            if temp.next.val == val:
                del_me = temp.next
                temp.next = temp.next.next
            temp = temp.next

        if del_me:
            print(f'removed value {del_me.val}')
            del del_me
        else:
            print(f'value {val} not found')
        
    def removeAtEnd(self):
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        removed_node = temp.next
        temp.next = None
        self.tail = temp
        print(f'removed the last node {removed_node.val}')
            
        

l = SinglyLinkedList(3)
l.show()

l.insertAtStart(4)
l.insertAtEnd(5)
l.insertAtIndex(2, 2)
l.show()

l.updateStart(11)
l.updateEnd(22)
l.show()

l.updateValue(22, 222)
l.updateIndex(33, 3)
l.show()

l.removeAtStart()
l.removeAtEnd()
l.show()

l.insertAtEnd(22)
l.insertAtEnd(33)
l.insertAtEnd(44)
l.show()

l.removeAtIndex(2)
l.show()

l.removeAtValue(22)
l.show()