#!python

from treemap import TreeMap
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class TreeMapTest(unittest.TestCase):
    def test_init(self):
        tm = TreeMap()
        assert tm.size == 0
        assert tm.items == []
    
    def test_init_with_list(self):
        tm = TreeMap([(1,2),(2,3),(3,4)])
        assert tm.size == 3
        self.assertCountEqual(tm.items(), [(1,2),(2,3),(3,4)])

    def test_set(self):
        tm = TreeMap()
        assert tm.size == 0
        tm.set(1,2)
        assert tm.size == 1
        tm.set(2,3)
        assert tm.size == 2
        tm.set(3,4)
        assert tm.size == 3
        self.assertCountEqual(tm.items(), [(1,2),(2,3),(3,4)])
        tm.set(3,5)
        assert tm.size == 3
        self.assertCountEqual(tm.items(), [(1,2),(2,3),(3,5)])

    def test_contains(self):
        tm = TreeMap([(1,2),(2,3),(3,4)])
        assert tm.contains(1) is True
        assert tm.contains(2) is True
        assert tm.contains(3) is True
        assert tm.contains(4) is False
    
    def test_get(self):
        tm = TreeMap([(1,2),(2,3),(3,4)])
        assert tm.get(1) == 2
        assert tm.get(2) == 3
        assert tm.get(3) == 4
        with self.assertRaises(ValueError):
            cb.get(4)
    
    def test_delete(self):
        tm = TreeMap()
        assert tm.size == 0
        tm.set(1,2)
        assert tm.size == 1
        tm.set(2,3)
        assert tm.size == 2
        tm.set(3,4)
        assert tm.size == 3
        self.assertCountEqual(tm.items(), [(1,2),(2,3),(3,4)])
        tm.delete(3)
        assert tm.size == 2
        self.assertCountEqual(tm.items(), [(1,2),(2,3)])
        tm.delete(2)
        assert tm.size == 1
        tm.delete(1)
        assert tm.size == 0
        


if __name__ == '__main__':
    unittest.main()
