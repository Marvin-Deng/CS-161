import unittest
from hw2 import (
    FINAL_STATE,
    NEXT_STATE,
    SUCC_FN,
)

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


if __name__ == '__main__':
    unittest.main()