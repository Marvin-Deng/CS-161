import unittest
from hw2 import (
    BFS,
)

class TestBFS(unittest.TestCase):
    def test_BFS_root(self):
        self.assertEqual(BFS("ROOT"), ('ROOT',))

    def test_BFS_example2(self):
        self.assertEqual(BFS(((("L", "E"), "F"), "T")), ('T', 'F', 'L', 'E'))

    def test_BFS_example3(self):
        self.assertEqual(BFS(("R", ("I", ("G", ("H", "T"))))), ('R', 'I', 'G', 'H', 'T'))

    def test_BFS_example4(self):
        self.assertEqual(BFS((("A", ("B",)), ("C",), "D")), ('D', 'A', 'C', 'B'))

    def test_BFS_example5(self):
        self.assertEqual(BFS(("T", ("H", "R", "E"), "E")), ('T', 'E', 'H', 'R', 'E'))

    def test_BFS_example6(self):
        self.assertEqual(BFS(("A", (("C", (("E",), "D")), "B"))), ('A', 'B', 'C', 'D', 'E'))

if __name__ == '__main__':
    unittest.main()
