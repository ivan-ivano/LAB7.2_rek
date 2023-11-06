import unittest
from LAB7_2_rek import find_min_element

a = [21, 94, 94, 36, 17, 91]


class TestFindMinElement(unittest.TestCase):
    def test_find_min_element(self):
        self.assertEqual(find_min_element(a), 17)  # add assertion here


if __name__ == '__main__':
    unittest.main()
