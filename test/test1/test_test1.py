import unittest


class TestTest1(unittest.TestCase):

    def test_test1(self):
        self.assertEqual(1, 1)

    def test_test1_failed(self):
        self.assertEqual(1, 2)