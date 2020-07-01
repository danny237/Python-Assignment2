""" Unitest for check_anagram """

import unittest
from check_anagram import check_anagram



class TestAnagram(unittest.TestCase):

    def test_positive(self):
        #test for positive
        self.assertEqual(check_anagram('poop', 'oopp'), True)

    def test_negative(self):
        #test for negative
        self.assertNotEqual(check_anagram('hahaha', 'hehehe'), False)
