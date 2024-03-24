# lifo
class Stack:
    def __init__(self, size):
        self.array = size * [0]
        self.size = size
        self.length = 0

    # checkers
    def can_delete(self):
        if self.length > 0:
            return True
        return False

    def can_create(self):
        if self.length < self.size:
            return True
        return False

    # read operations
    def show(self):
        print('stack -',self.array[:self.length], '\n')
    
    def find(self, value):
        '''return index else None'''
        for i in range(self.length):
            if self.array[i] == value:
                return i
        return None

    # create operations
    def push(self, value):
        if self.can_create():
            self.array[self.length] = value
            print(f'pushed {value} in stack')
            self.length += 1
        else:
            print(f'eroor - stack is full')
    
    # update operations
    def update(self, old_value, new_value):
        index = self.find(old_value)
        if index is not None:
            self.array[index] = new_value
            print(f'updated {old_value} with {new_value}')
        else:
            print(f'error - {old_value} dosenot exists')

    # delete operations
    def pop(self):
        if self.can_delete():
            removed_val = self.array[self.length-1]
            self.array[self.length-1] = 0
            self.length -= 1
            print(f'removed {removed_val} from stack')
            del removed_val


s = Stack(10)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(11)
s.show()

s.update(3, 33)
s.update(4, 44)
s.show()

s.pop()
s.pop()
s.pop()
s.show()