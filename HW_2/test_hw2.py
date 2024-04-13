import unittest
from hw2 import (
    BFS,
    DFS,
    DFID,
    FINAL_STATE,
    NEXT_STATE,
    SUCC_FN,
    ON_PATH,
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

class TestFinalState(unittest.TestCase):
    def test_final_state_all_true(self):
        S = (True, True, True, True)
        self.assertTrue(FINAL_STATE(S))

    def test_final_state_some_false(self):
        S = (True, True, False, True)
        self.assertFalse(FINAL_STATE(S))

    def test_final_state_all_false(self):
        S = (False, False, False, False)
        self.assertFalse(FINAL_STATE(S))

    def test_final_state_different_arrangement(self):
        S = (True, False, True, False)
        self.assertFalse(FINAL_STATE(S))

class TestNextState(unittest.TestCase):
    def test_invalid_current_state(self):
        S = (True, False, False, True)  # Baby unsupervised with dog
        A = "h"
        expected_state = []
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_only_homer_to_valid_state(self):
        S = (True, True, False, False)
        A = "h"
        expected_state = [(False, True, False, False)]
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_only_homer_to_invalid_state(self):
        S = (True, True, True, True)
        A = "h"
        expected_state = [] # Moves to invalid state where baby on same side as dog and poison
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_homer_and_baby_to_valid_state(self):
        S = (False, False, True, True)
        A = "b"
        expected_state = [(True, True, True, True)]
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_homer_and_baby_invalid_current_state(self):
        S = (True, False, True, True) # Homer and baby on opposite ends
        A = "b"
        expected_state = []
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_homer_and_dog_to_valid_state(self):
        S = (True, False, True, True) 
        A = "d"
        expected_state = [(False, False, False, True)]
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_homer_and_dog_to_invalid_state(self):
        S = (True, True, True, True) 
        A = "d"
        expected_state = [] # Baby left with poison
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_homer_and_dog_invalid_current_state(self):
        S = (True, True, False, True) # Homer and dog on opposite ends
        A = "d"
        expected_state = []
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_hommer_and_poison_to_valid_state(self):
        S = (True, True, False, True)
        A = "p"
        expected_state = [(False, True, False, False)]
        self.assertEqual(NEXT_STATE(S, A), expected_state)

    def test_move_hommer_and_poison_to_invalid_state(self):
        S = (True, True, True, True)
        A = "p"  
        expected_state = [] # Moves to invalid state, where baby and dog on the same side
        self.assertEqual(NEXT_STATE(S, A), expected_state)

class TestSUCC_FN(unittest.TestCase):
    def test_successor_states_with_all_entities_on_left_side(self):
        S = (True, True, True, True)
        expected_successor_states = [
            (False, False, True, True), # Move homer and baby
        ]
        self.assertEqual(SUCC_FN(S), expected_successor_states)

    def test_successor_states_with_all_entities_on_right_side(self):
        S = (False, False, False, False)
        expected_successor_states = [
            (True, True, False, False), # Move homer and baby
        ]
        self.assertEqual(SUCC_FN(S), expected_successor_states)

    def test_successor_states_where_dog_and_poison_opposite_baby(self): 
        S = (True, False, True, True)
        expected_successor_states = [
            (False, False, True, True), # Move only homer
            (False, False, False, True), # Move homer and dog
            (False, False, True, False), # Move homer and poison
        ]
        self.assertEqual(SUCC_FN(S), expected_successor_states)

    def test_successor_states_where_only_homer_and_baby_on_same_side(self): 
        S = (True, True, False, False)
        expected_successor_states = [
            (False, True, False, False), # Move only homer
            (False, False, False, False), # Move homer and baby
        ]
        self.assertEqual(SUCC_FN(S), expected_successor_states)

    def test_current_state_is_invalid(self): 
        S = (True, False, False, False)
        expected_successor_states = []
        self.assertEqual(SUCC_FN(S), expected_successor_states)

class TestON_PATH(unittest.TestCase):
    def test_current_state_on_stack(self): 
        S = (True, False, False, False)
        states = [(True, False, False, False), (False, False, False, False), (True, True, True, False)]
        self.assertTrue(ON_PATH(S, states))

    def test_current_state_not_on_stack(self): 
        S = (True, False, False, False)
        states = [(True, True, False, False), (False, False, False, False), (True, True, True, False)]
        self.assertFalse(ON_PATH(S, states))

if __name__ == '__main__':
    unittest.main()
