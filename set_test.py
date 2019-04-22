from set import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set(['A','B','C','D','E'])
        assert test_set.length() == 5
        assert test_set.contains('A') == True
        assert test_set.contains('C') == True
        assert test_set.contains('E') == True

    def test_contains(self):
        test_set = Set(['A','B','C','D','E'])
        assert test_set.length() == 5
        assert test_set.contains('A') == True
        assert test_set.contains('B') == True
        assert test_set.contains('C') == True
        assert test_set.contains('D') == True
        assert test_set.contains('E') == True
        assert test_set.contains('F') == False
        assert test_set.contains('Z') == False

    def test_add(self):
        test_set = Set()
        assert test_set.length() == 0
        test_set.add('A')
        assert test_set.contains('A') == True
        test_set.add('B')
        assert test_set.contains('B') == True
        test_set.add('C')
        assert test_set.contains('C') == True
    
    def test_remove(self):
        test_set = Set(['A','B','C'])
        assert test_set.length() == 3
        test_set.remove('A')
        assert test_set.length() == 2
        assert test_set.contains('A') == False 
        test_set.remove('B')
        assert test_set.length() == 1
        assert test_set.contains('B') == False
        test_set.remove('C')
        assert test_set.length() == 0
        assert test_set.contains('C') == False

    def test_union(self):
        test_set = Set(['A','B','C','D','E'])
        other_set = Set(['C','D','E','F','G'])
        unions = test_set.union(other_set)
        union_items = unions.get_items()
        self.assertCountEqual(union_items, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_intersection(self):
        test_set = Set(['A','B','C','D','E'])
        other_set = Set(['C','D','E','F','G'])
        intersection = test_set.intersection(other_set)
        intersection_items = intersection.get_items()
        self.assertCountEqual(intersection_items, ['C', 'D', 'E'])

    def test_difference(self):
        test_set = Set(['A','B','C','D','E'])
        other_set = Set(['C','D','E','F','G'])
        difference = test_set.difference(other_set)
        difference_items = difference.get_items()
        self.assertCountEqual(difference_items, ['A','B'])


    def test_is_subset(self):
        pass

if __name__ == '__main__':
    unittest.main()
