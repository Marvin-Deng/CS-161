import unittest
from hw2 import (
    BFS,
    DFS,
    DFID,
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

class TestDFS(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(DFS("ROOT"), ('ROOT',))

    def test_example2(self):
        self.assertEqual(DFS(((("L", "E"), "F"), "T")), ('L', 'E', 'F', 'T'))

    def test_example3(self):
        self.assertEqual(DFS(("R", ("I", ("G", ("H", "T"))))), ('R', 'I', 'G', 'H', 'T'))

    def test_example4(self):
        self.assertEqual(DFS((("A", ("B",)), ("C",), "D")), ('A', 'B', 'C', 'D'))

    def test_example5(self):
        self.assertEqual(DFS(("T", ("H", "R", "E"), "E")), ('T', 'H', 'R', 'E', 'E'))

    def test_example6(self):
        self.assertEqual(DFS(("A", (("C", (("E",), "D")), "B"))), ('A', 'C', 'E', 'D', 'B'))

    def test_example4(self):
        self.assertEqual(DFS(("A", "B", "C", "D")), ('A', 'B', 'C', 'D'))

class TestDFID(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(DFID("ROOT", 0), ('ROOT',))

    def test_example2(self):
        self.assertEqual(DFID(((("L", "E"), "F"), "T"), 3), ('T', 'T', 'F', 'T', 'F', 'E', 'L'))

    def test_example3(self):
        self.assertEqual(DFID(("R", ("I", ("G", ("H", "T")))), 4), ('R', 'I', 'R', 'G', 'I', 'R', 'T', 'H', 'G', 'I', 'R'))

    def test_example4(self):
        self.assertEqual(DFID((("A", ("B",)), ("C",), "D"), 3), ('D', 'D', 'C', 'A', 'D', 'C', 'B', 'A'))

    def test_example5(self):
        self.assertEqual(DFID(("T", ("H", "R", "E"), "E"), 2), ('E', 'T', 'E', 'E', 'R', 'H', 'T'))

    def test_example6(self):
        self.assertEqual(DFID(("A", (("C", (("E",), "D")), "B")), 5), ('A', 'B', 'A', 'B', 'C', 'A', 'B', 'D', 'C', 'A', 'B', 'D', 'E', 'C', 'A'))


if __name__ == '__main__':
    unittest.main()
