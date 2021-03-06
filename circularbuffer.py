class CircularBuffer(object):
    def __init__(self, items = None):
        self.head = None
        self.tail = None
        self.list = [None] * 10
        self.size = 0
        self.length = 10
        if items is not None:
            self.list = items[:]
            self.size = len(items)
            self.head = 0
            self.tail = len(items) - 1
    
    # def __repr__(self):
    #     return ''.join(self.list)
    
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def is_full(self):
        if self.size == self.length:
            return True
        return False
    
    def inc_head(self):
        self.head += 1
        if self.head == self.length:
            self.head = 0
    
    def inc_tail(self):
        self.tail += 1
        if self.tail == self.length:
            self.tail = 0

    def dec_tail(self):
        self.tail -= 1
        if self.tail == -1:
            self.tail = self.length - 1

    def enqueue(self, item):
        if self.is_empty():
            self.list[0] = item
            self.head = 0
            self.tail = 0
            self.size += 1
        elif self.is_full():
            deq = self.list[self.head]
            self.list[self.head] = item
            self.inc_head()
            self.inc_tail
            return deq
        else: # list is not full and not empty
            self.inc_tail()
            self.list[self.tail] = item
            self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Circular buffer is empty')
        else:
            deq = self.list[self.head]
            self.list[self.head] = None
            self.inc_head()
            self.size -= 1
            if self.size == 0:
                self.head = None
                self.tail = None
            return deq
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list[self.head]
