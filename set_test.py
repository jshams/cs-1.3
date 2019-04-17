from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set(['A','B','C','D','E'])
        assert = test_set.length() == 5
        assert test_set.test_contains('A') == True
        assert test_set.test_contains('C') == True
        assert test_set.test_contains('E') == True

    def test_contains(self):
        test_set = Set(['A','B','C','D','E'])
        assert = test_set.length() == 5
        assert test_set.test_contains('A') == True
        assert test_set.test_contains('B') == True
        assert test_set.test_contains('C') == True
        assert test_set.test_contains('D') == True
        assert test_set.test_contains('E') == True
        assert test_set.test_contains('F') == False
        assert test_set.test_contains('Z') == False

    def test_add(self):
        test_set = Set()
        assert test_set.length() == 0
        test_set.add('A')
        assert test_set.test_contains('A') == True
        test_set.add('B')
        assert test_set.test_contains('B') == True
        test_set.add('C')
        assert test_set.test_contains('C') == True
    
    def test_remove(self):
        test_set = Set(['A','B','C','D','E'])
        assert test_set.length() == 5
        test_set.remove('A')
        assert test_set.length() == 4
        assert test_set.test_contains('A') == False 


    def test_union(self):
    
    def test_intersection(self):

    def test_difference(self):

    def test_is_subset(self):

    

if __name__ == '__main__':
    unittest.main()
