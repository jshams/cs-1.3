
class CircularBufferNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularBuffer(object):
    def __init__(self, items = None):
        self.head = None
        self.tail = None
        self.list = []
        self.size = 0
        self.length = 10
        if items is not None:
            self.list = items[:]
            self.size = len(items)
            self.head = 0
            self.tail = len(items) - 1
    
    def is_empty(self):
        if self.head == None:
            return True
        return False

    def is_full(self):
        if self.size == self.length:
            return True
        return False

    def enqueue(self, item):
        if self.is_empty():
            self.list[0] = item
            self.head = 0
        elif self.is_full():
            deq = self.list[self.head]
            self.list[self.head] = item
            self.head += 1
            if self.head == self.size:
                self.head = 0


            deq = self.list[self.head]
            self.list[self.head] = item
            self.head += 1


