import unittest
from hw1 import (
    PAD,
    SUMS,
    ANON,
    TREE_HEIGHT,
)

class TestPadovanSequence(unittest.TestCase):
    def test_PAD_0_returns_1(self):
        self.assertEqual(PAD(0), 1)

    def test_PAD_1_returns_1(self):
        self.assertEqual(PAD(1), 1)

    def test_PAD_2_returns_1(self):
        self.assertEqual(PAD(2), 1)

    def test_PAD_3_returns_2(self):
        self.assertEqual(PAD(3), 2)

    def test_PAD_4_returns_2(self):
        self.assertEqual(PAD(4), 2)

    def test_PAD_5_returns_3(self):
        self.assertEqual(PAD(5), 3)

    def test_PAD_6_returns_4(self):
        self.assertEqual(PAD(6), 4)

    def test_PAD_7_returns_5(self):
        self.assertEqual(PAD(7), 5)

    def test_PAD_8_returns_7(self):
        self.assertEqual(PAD(8), 7)

    def test_PAD_9_returns_9(self):
        self.assertEqual(PAD(9), 9)

    def test_PAD_10_returns_12(self):
        self.assertEqual(PAD(10), 12)

    def test_PAD_20_returns_200(self):
        self.assertEqual(PAD(20), 200)


class TestSumsFunction(unittest.TestCase):
    def test_sums_for_PAD_0(self):
        self.assertEqual(SUMS(0), 0)

    def test_sums_for_PAD_1(self):
        self.assertEqual(SUMS(1), 0)

    def test_sums_for_PAD_2(self):
        self.assertEqual(SUMS(2), 0)

    def test_sums_for_PAD_3(self):
        self.assertEqual(SUMS(3), 1)

    def test_sums_for_PAD_4(self):
        self.assertEqual(SUMS(4), 1)

    def test_sums_for_PAD_5(self):
        self.assertEqual(SUMS(5), 2)

    def test_sums_for_PAD_6(self):
        self.assertEqual(SUMS(6), 3)

    def test_sums_for_PAD_7(self):
        self.assertEqual(SUMS(7), 4)

    def test_sums_for_PAD_8(self):
        self.assertEqual(SUMS(8), 6)

    def test_sums_for_PAD_9(self):
        self.assertEqual(SUMS(9), 8)

    def test_sums_for_PAD_10(self):
        self.assertEqual(SUMS(10), 11)

    def test_sums_for_PAD_20(self):
        self.assertEqual(SUMS(20), 199)


class TestAnonFunction(unittest.TestCase):
    def test_anon_with_number(self):
        self.assertEqual(ANON(42), '?')

    def test_anon_with_string(self):
        self.assertEqual(ANON("FOO"), '?')

    def test_anon_with_nested_tuples(self):
        self.assertEqual(ANON(((("L", "E"), "F"), "T")), ((('?','?'), '?'), '?'))
        self.assertEqual(ANON((5, "FOO", 3.1, -0.2)), ('?', '?', '?', '?'))
        self.assertEqual(ANON((1, ("FOO", 3.1), -0.2)), ('?', ('?', '?'), '?'))
        self.assertEqual(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))), ((('?', '?'), ('?', '?')), ('?', '?')))
        self.assertEqual(ANON(("R", ("I", ("G", ("H", "T"))))), ('?', ('?', ('?', ('?', '?')))))


class TestTreeHeight(unittest.TestCase):
    def test_height_of_single_node(self):
        self.assertEqual(TREE_HEIGHT(1), 0)

    def test_height_of_flat_tree(self):
        self.assertEqual(TREE_HEIGHT((5, "FOO", 3.1, -0.2)), 1)

    def test_height_with_one_subtree(self):
        self.assertEqual(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)), 2)

    def test_height_of_nested_tree(self):
        self.assertEqual(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))), 4)


if __name__ == '__main__':
    unittest.main()
