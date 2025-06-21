
#We have a function add(x, y) that adds two numbers.We test this function using TestMathOperations.It checks if add(2, 3) gives 5, and if add(-1, 1) gives 0.
#Unit testing is a way to check if small parts of a program (called functions) are working correctly.
# It is like testing each part of a machine before putting it all together.

import unittest

def add(x, y):
    return x + y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()