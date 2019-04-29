from redact_problem import redact_words
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
        # set([1,1,1,2,3]) = set([3,2,1])
        # >>> True
        # self.assertCountEqual([1,1,1,2,3], [3,2,1])
        # >>> False


class Redact_Test(unittest.TestCase):
    def test_with_integers(self):
        original = [1,2,3,4,5,6,7,8,9]
        banned = [1,3,5,7,9]
        redacted_words = (redact_words(original, banned))
        self.assertCountEqual(redacted_words, [2,4,6,8])

    def test_with_strings(self):
        original = 'hello my name is Jake'.split(' ')
        banned = 'hello Jake'.split(' ')
        redacted_words = redact_words(original, banned)
        self.assertCountEqual(redacted_words, 'my name is'.split(' '))

    def test_with_extra_banned_words(self):
        original = [1,2,3,4,5,6,7,8]
        banned = [1,3,5,7,9,11,13]
        redacted_words = redact_words(original, banned)
        self.assertCountEqual(redacted_words, [2,4,6,8])

    def test_with_no_banned_words(self):
        original = [1,2,3,4,5,6,7,8]
        banned = []
        redacted_words = redact_words(original, banned)
        self.assertCountEqual(redacted_words, original)

    def test_with_no_words(self):
        original = []
        banned = [1,2,3,4,5]
        assert redact_words(original, banned) == []

    def test_with_no_matching_words(self):
        original = [1,2,3,4,5,6,7,8]
        banned = [11,12,13,14]
        redacted_words = redact_words(original, banned)
        self.assertCountEqual(redacted_words, original)
    
    

        

if __name__ == '__main__':
    unittest.main()
