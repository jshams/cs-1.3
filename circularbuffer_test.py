from circularbuffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        cb = CircularBuffer()
        assert cb.head is None
        assert cb.length == 10
        assert cb.is_empty() is True

    def test_init_with_list(self):
        cb = CircularBuffer(['A', 'B', 'C'])
        assert cb.head == 0
        assert cb.list[0] == 'A'
        assert cb.size == 3
        assert cb.tail == 2
        # assert cb.is_empty() is False

    def test_size(self):
        cb = CircularBuffer()
        assert cb.size == 0
        cb.enqueue('A')
        assert cb.size == 1
        cb.enqueue('B')
        assert cb.size == 2
        cb.dequeue()
        assert cb.size == 1
        cb.dequeue()
        assert cb.size == 0

    def test_enqueue(self):
        cb = CircularBuffer()
        cb.enqueue('A')
        assert cb.peek() == 'A'
        assert cb.size == 1
        cb.enqueue('B')
        assert cb.peek() == 'A'
        assert cb.size == 2
        cb.enqueue('C')
        assert cb.peek() == 'A'
        assert cb.size == 3
        assert cb.is_empty() is False

    def test_front(self):
        cb = CircularBuffer()
        assert cb.peek() is None
        cb.enqueue('A')
        assert cb.peek() == 'A'
        cb.enqueue('B')
        assert cb.peek() == 'A'
        cb.dequeue()
        assert cb.peek() == 'B'
        cb.dequeue()
        assert cb.peek() is None

    def test_dequeue(self):
        cb = CircularBuffer(['A', 'B', 'C'])
        assert cb.dequeue() == 'A'
        assert cb.size == 2
        assert cb.dequeue() == 'B'
        assert cb.size == 1
        assert cb.dequeue() == 'C'
        assert cb.size == 0
        assert cb.is_empty() is True
        with self.assertRaises(ValueError):
            cb.dequeue()
