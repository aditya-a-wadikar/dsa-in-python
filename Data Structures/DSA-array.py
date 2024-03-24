class Array:
    def __init__(self, size:int):
        self.size = size
        self.length = 0
        self.array = [0] * size

    def __str__(self):
        return f"array is -{self.array[:self.length]}"

    def can_insert(self):
        return self.length < self.size

    def can_delete(self):
        return self.length > 0

    def show(self):
        print("array is -",self.array[:self.length], "\n")

    def insertAtIndex(self, val, index):
        if self.can_insert():
            for i in range(self.length-1, index-1, -1):
                self.array[i+1] = self.array[i]
            self.array[index] = val
            self.length += 1
        else:
            return OverflowError("Array is full")

    def append(self, val):
        if self.can_insert():
            self.array[self.length] = val
            self.length += 1

    def deleteIndex(self, index) -> int:
        if self.can_delete():
            ret_me = self.array[index]
            for i in range(index, self.length):
                self.array[i] = self.array[i+1]
            print(f"removed {ret_me} from index {index}")
            self.length -= 1

    def deleteValue(self, val):
        index = None
        for i in range(self.length):
            if self.array[i] == val:
                index = i

        if index is not None:
            a.deleteIndex(index)
        else:
            print(f"value {val} not found")


    def pop(self):
        ret_me = self.array[self.length-1]
        self.length-=1
        print(f"popped - {ret_me}")


        

a = Array(size=10)
a.append(11)
a.append(12)
a.append(13)
a.append(14)
a.append(15)
a.append(16)
print(a)

a.pop()
a.deleteIndex(2)
print(a)

a.deleteValue(11)
a.deleteValue(12)
print(a)


