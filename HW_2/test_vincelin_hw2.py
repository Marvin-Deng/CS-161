"""
Unit tester for S24 COM SCI 161: Homework 2. All test cases for
Questions 1-3 come directly from the assignment spec or from instructor
answers on Piazza. The test cases for Question 4 check for some basic
invariants of the returned path of states.
"""

import itertools
import unittest
from argparse import ArgumentParser, ArgumentTypeError
from typing import Iterable, List, Literal, Optional, Tuple, Type

from hw2 import BFS, DFID, DFS, DFS_SOL

__author__ = "Vincent Lin"

StateTuple = Tuple[bool, bool, bool, bool]
QuestionNum = Literal[1, 2, 3, 4]

INDEX_HOMER = 0
INDEX_BABY = 1
INDEX_DOG = 2
INDEX_POISON = 3

DEFAULT_INITIAL_STATE: StateTuple = (False, False, False, False)
GOAL_STATE: StateTuple = (True, True, True, True)

# ==================================================================== #
# region Test Suites


class TestBFS(unittest.TestCase):
    """Compilation of the test cases from the spec for Question 1:

    >>> BFS("ROOT")
    ("ROOT",)
    >>> BFS(((("L", "E"), "F"), "T"))
    ("T", "F", "L", "E")
    >>> BFS(("R", ("I", ("G", ("H", "T")))))
    ("R", "I", "G", "H", "T")
    >>> BFS((("A", ("B",)), ("C",), "D"))
    ("D", "A", "C", "B")
    >>> BFS(("T", ("H", "R", "E"), "E"))
    ("T", "E", "H", "R", "E")
    >>> BFS(("A", (("C", (("E",), "D")), "B")))
    ("A", "B", "C", "D", "E")
    """

    def test_non_tuple(self) -> None:
        self.assertEqual(BFS("ROOT"), ("ROOT", ))

    def test_left_tree(self) -> None:
        received = BFS(((("L", "E"), "F"), "T"))
        expected = ("T", "F", "L", "E")
        self.assertEqual(received, expected)

    def test_right_tree(self) -> None:
        received = BFS(("R", ("I", ("G", ("H", "T")))))
        expected = ("R", "I", "G", "H", "T")
        self.assertEqual(received, expected)

    def test_abcd_tree(self) -> None:
        received = BFS((("A", ("B",)), ("C",), "D"))
        expected = ("D", "A", "C", "B")
        self.assertEqual(received, expected)

    def test_three_tree(self) -> None:
        received = BFS(("T", ("H", "R", "E"), "E"))
        expected = ("T", "E", "H", "R", "E")
        self.assertEqual(received, expected)

    def test_acedb_tree(self) -> None:
        received = BFS(("A", (("C", (("E",), "D")), "B")))
        expected = ("A", "B", "C", "D", "E")
        self.assertEqual(received, expected)


class TestDFS(unittest.TestCase):
    """Compilation of the test cases from the spec for Question 2:

    >>> DFS("ROOT")
    ("ROOT",)
    >>> DFS(((("L", "E"), "F"), "T"))
    ("L", "E", "F", "T")
    >>> DFS(("R", ("I", ("G", ("H", "T")))))
    ("R", "I", "G", "H", "T")
    >>> DFS((("A", ("B",)), ("C",), "D"))
    ("A", "B", "C", "D")
    >>> DFS(("T", ("H", "R", "E"), "E"))
    ("T", "H", "R", "E", "E")
    >>> DFS(("A", (("C", (("E",), "D")), "B")))
    ("A", "C", "E", "D", "B")
    """

    def test_non_tuple(self) -> None:
        self.assertEqual(DFS("ROOT"), ("ROOT", ))

    def test_left_tree(self) -> None:
        received = DFS(((("L", "E"), "F"), "T"))
        expected = ("L", "E", "F", "T")
        self.assertEqual(received, expected)

    def test_right_tree(self) -> None:
        received = DFS(("R", ("I", ("G", ("H", "T")))))
        expected = ("R", "I", "G", "H", "T")
        self.assertEqual(received, expected)

    def test_abcd_tree(self) -> None:
        received = DFS((("A", ("B",)), ("C",), "D"))
        expected = ("A", "B", "C", "D")
        self.assertEqual(received, expected)

    def test_three_tree(self) -> None:
        received = DFS(("T", ("H", "R", "E"), "E"))
        expected = ("T", "H", "R", "E", "E")
        self.assertEqual(received, expected)

    def test_acedb_tree(self) -> None:
        received = DFS(("A", (("C", (("E",), "D")), "B")))
        expected = ("A", "C", "E", "D", "B")
        self.assertEqual(received, expected)


class TestDFID(unittest.TestCase):
    """Compilation of the test cases from the spec for Question 3:

    >>> DFID("ROOT", 0)
    ("ROOT",)
    >>> DFID(((("L", "E"), "F"), "T"), 3)
    ("T", "T", "F", "T", "F", "E", "L")
    >>> DFID(("R", ("I", ("G", ("H", "T")))), 4)
    ("R", "I", "R", "G", "I", "R", "T", "H", "G", "I", "R")
    >>> DFID(((("A", ("B",)), ("C",), "D")), 3)
    ("D", "D", "C", "A", "D", "C", "B", "A")
    >>> DFID(("T", ("H", "R", "E"), "E"), 2)
    ("E", "T", "E", "E", "R", "H", "T")
    >>> DFID(("A", (("C", (("E",), "D")), "B")), 5)
    ("A", "B", "A", "B", "C", "A", "B", "D", "C", "A", "B", "D", "E",
    "C", "A")
    """

    def test_non_tuple(self) -> None:
        self.assertEqual(DFID("ROOT", 0), ("ROOT", ))

    def test_left_tree(self) -> None:
        received = DFID(((("L", "E"), "F"), "T"), 3)
        expected = ("T", "T", "F", "T", "F", "E", "L")
        self.assertEqual(received, expected)

    def test_right_tree(self) -> None:
        received = DFID(("R", ("I", ("G", ("H", "T")))), 4)
        expected = ("R", "I", "R", "G", "I", "R", "T", "H", "G", "I", "R")
        self.assertEqual(received, expected)

    def test_abcd_tree(self) -> None:
        received = DFID((("A", ("B",)), ("C",), "D"), 3)
        expected = ("D", "D", "C", "A", "D", "C", "B", "A")
        self.assertEqual(received, expected)

    def test_three_tree(self) -> None:
        received = DFID(("T", ("H", "R", "E"), "E"), 2)
        expected = ("E", "T", "E", "E", "R", "H", "T")
        self.assertEqual(received, expected)

    def test_acedb_tree(self) -> None:
        received = DFID(("A", (("C", (("E",), "D")), "B")), 5)
        expected = ("A", "B", "A", "B", "C", "A", "B", "D", "C", "A", "B",
                    "D", "E", "C", "A")
        self.assertEqual(received, expected)

    # https://piazza.com/class/lubtfmab6ne4mp/post/55
    def test_zero_max_depth(self) -> None:
        self.assertEqual(DFID(("A", "B"), 0), ())


class TestDFS_SOL(unittest.TestCase):
    """Static tests for Q4."""

    def test_initial_is_already_goal_state(self) -> None:
        received_path = DFS_SOL(GOAL_STATE, [])
        expected_path = [GOAL_STATE]
        self.assertEqual(received_path, expected_path)

    def test_includes_initial_state(self) -> None:
        received_path = DFS_SOL(DEFAULT_INITIAL_STATE, [])
        self.assertEqual(received_path[0], DEFAULT_INITIAL_STATE)

    def test_reaches_goal_state(self) -> None:
        received_path = DFS_SOL(DEFAULT_INITIAL_STATE, [])
        self.assertEqual(received_path[-1], GOAL_STATE)


def create_dynamic_DFS_SOL_tester(
    initial_state: StateTuple,
) -> Type[unittest.TestCase]:
    """
    Factory function for creating a dynamic `TestCase` for Q4,
    specialized for a specific initial state.
    """
    class TestInitialState(unittest.TestCase):
        INITIAL_STATE = initial_state

        @classmethod
        def setUpClass(cls) -> None:
            cls.received_path = DFS_SOL(cls.INITIAL_STATE, [])

        def test_valid_states(self) -> None:
            for index, state in enumerate(self.received_path):
                is_valid_state = check_valid_state(state)
                self.assertTrue(is_valid_state, (
                    f"Invalid state: {state!r} @ index {index} in path:\n"
                    f"{self.received_path!r}"
                ))

        def test_possible_transitions(self) -> None:
            for index in range(len(self.received_path) - 1):
                old_state = self.received_path[index]
                new_state = self.received_path[index + 1]
                is_valid_action = check_transition_is_a_possible_action(
                    old_state,
                    new_state,
                )
                self.assertTrue(is_valid_action, (
                    f"Invalid action: {old_state!r} -> {new_state!r} "
                    f"@ indices {index},{index + 1} in path:\n"
                    f"{self.received_path!r}"
                ))

    # Make the initial state show up as part of the class name if run in
    # verbose mode.
    tf_string = abbreviate_state_tuple(initial_state, as_tf_string=True)
    TestInitialState.__qualname__ = f"{TestInitialState.__name__}{tf_string}"
    return TestInitialState


# endregion
# ==================================================================== #
# region State Validators


def check_valid_state(state: StateTuple) -> bool:
    homer, baby, dog, poison = state
    # Dog and baby are unsupervised.
    if dog is baby and baby is not homer:
        return False
    # Baby and poison are unsupervised.
    if poison is baby and baby is not homer:
        return False
    return True


def check_transition_is_a_possible_action(
    old_state: StateTuple,
    new_state: StateTuple,
) -> bool:
    """
    Note that this only checks if the transition corresponds to one of
    the operators ("h", "b", "d", "p") and not if the resulting state is
    valid. State validity is tested orthogonally.
    """
    homer_old, *entities_old = old_state
    homer_new, *entities_new = new_state

    # Homer must move every transition.
    if homer_old is homer_new:
        return False

    # Homer could be the only entity that moved.
    homer_moved_alone = entities_old == entities_new

    # Or, Homer and exactly one other entity moved.
    homer_moved_with_one_entity = _exactly_one_difference(
        entities_old,
        entities_new,
    )

    return homer_moved_alone or homer_moved_with_one_entity


def _exactly_one_difference(
    iter1: Iterable[bool],
    iter2: Iterable[bool],
) -> bool:
    difference_seen = False
    for elem1, elem2 in zip(iter1, iter2):
        if elem1 != elem2:
            if difference_seen:
                return False
            difference_seen = True
    return difference_seen


# endregion
# ==================================================================== #
# region Formatting Helper Functions


def state_tuple_index_to_entity_name(index: int) -> str:
    if index == INDEX_HOMER:
        return "Homer"
    if index == INDEX_BABY:
        return "Baby"
    if index == INDEX_DOG:
        return "Dog"
    if index == INDEX_POISON:
        return "Poison"
    raise ValueError(
        f"index {index} is out of range for a state tuple"
    )


def abbreviate_state_tuple(
    state: StateTuple, *,
    as_tf_string: bool = False,
) -> str:
    chars = [("T" if flag else "F") for flag in state]
    if as_tf_string:
        return "".join(chars)  # e.g. "TTFF"
    return f"({','.join(chars)})"  # e.g. "(T,T,F,F)"


# endregion
# ==================================================================== #
# region Path Explainer


class PathExplainer:
    """Class to help debug the path returned by solutions to Q4."""

    def __init__(self, path: List[StateTuple]) -> None:
        self._path = path
        self._validate_path_structure()

    def _validate_path_structure(self) -> None:
        if not isinstance(self._path, list):
            raise TypeError(
                "path should be type list, got "
                f"{type(self._path).__name__} instead"
            )
        for index, state in enumerate(self._path):
            if not isinstance(state, tuple):
                raise TypeError(
                    f"states should be type tuple, got {type(state).__name__} "
                    f"instead ({state!r} @ index {index})"
                )
            if len(state) != 4:
                raise ValueError(
                    f"states should be 4-tuples, got a {len(state)}-tuple "
                    f"instead ({state!r} @ index {index})"
                )
            if not all(isinstance(flag, bool) for flag in state):
                raise TypeError(
                    f"states should be tuples of bools, got {state!r} "
                    f"instead ({state!r} @ index {index})"
                )

    def explain_path(self) -> None:
        for index in range(len(self._path) - 1):
            old_state = self._path[index]
            new_state = self._path[index + 1]

            print("-" * 50)

            old_index_string = f"PATH[{index}]"
            new_index_string = f"PATH[{index + 1}]"
            print(f"Index:   {old_index_string:>9} ===> {new_index_string}")

            old_state_string = abbreviate_state_tuple(old_state)
            new_state_string = abbreviate_state_tuple(new_state)
            print(f"State:   {old_state_string} ===> {new_state_string}")

            old_state_drawing = self.draw_state(index)
            new_state_drawing = self.draw_state(index + 1)
            print()
            print(f"{old_state_string}: {old_state_drawing}")
            print(f"{new_state_string}: {new_state_drawing}")

            explanation = self.get_transition_explanation(index)
            print()
            print("\n".join(f">> {line}" for line in explanation))

    def get_transition_explanation(
        self,
        start_index_in_path: int,
    ) -> List[str]:
        old_state = self._path[start_index_in_path]
        new_state = self._path[start_index_in_path + 1]

        # List of (entity name, direction), where True means East ->
        # West and False means West -> East.
        entity_movements: List[Tuple[str, bool]] = []

        zipped = zip(old_state, new_state)
        for index, (entity_old, entity_new) in enumerate(zipped):
            if entity_old != entity_new:
                entity_name = state_tuple_index_to_entity_name(index)
                entity_movements.append((entity_name, entity_new))

        num_moved = len(entity_movements)

        def direction(westwards: bool) -> str:
            return "WEST (LEFT)" if westwards else "EAST (RIGHT)"

        if num_moved == 0:
            return ["No one moved."]

        if num_moved == 1:
            entity_name, westwards = entity_movements[0]
            return [
                f"Only {entity_name} moved, to the {direction(westwards)}.",
            ]

        # num_moved >= 2
        names_westwards: List[str] = []
        names_eastwards: List[str] = []
        for name, westwards in entity_movements:
            (names_westwards if westwards else names_eastwards).append(name)

        lines: List[str] = []
        if names_westwards:
            lines.append(
                ", ".join(names_westwards) +
                f" moved to the {direction(True)}.",
            )
        if names_eastwards:
            lines.append(
                ", ".join(names_eastwards) +
                f" moved to the {direction(False)}."
            )
        return lines

    def draw_state(self, index_in_path: int) -> str:
        """
        Example representations (one per line):

            ```
                 H,B || D,P
             H,B,D,P ||
                   D || H,B,P
            ```
        """
        state = self._path[index_in_path]

        west_tokens: List[str] = []
        east_tokens: List[str] = []
        for index, on_west_side in enumerate(state):
            token = state_tuple_index_to_entity_name(index)[0]
            (west_tokens if on_west_side else east_tokens).append(token)

        west_string = ",".join(west_tokens)
        east_string = ",".join(east_tokens)

        return f"{west_string:>8} || {east_string:<8}"


# endregion
# ==================================================================== #
# region Command Line Interface


def _chars_to_state_tuple(chars: str) -> StateTuple:
    if len(chars) != 4:
        raise ArgumentTypeError(
            f"expected string of length 4, received {chars!r} "
            f"(length {len(chars)})"
        )

    flags = []
    for char in chars:
        if char in ("T", "t"):
            flags.append(True)
        elif char in ("F", "f"):
            flags.append(False)
        else:
            raise ArgumentTypeError(
                "expected string with only T/t/F/f characters, received "
                f"{chars!r} (contains illegal character {char!r})"
            )

    state = tuple(flags)

    if not check_valid_state(state):
        raise ArgumentTypeError(f"{chars!r} encodes an invalid state!")

    return state


parser = ArgumentParser(description=__doc__)

parser.add_argument(
    "-i", "--initial-state",
    metavar="/{T,F}{4}/i",
    dest="initial_state",
    type=_chars_to_state_tuple,
    default=(False, False, False, False),
    help="initial state for Q4, in the format of 4 T/F's e.g. TTFF",
)
parser.add_argument(
    "-v", "--verbose",
    dest="verbose",
    action="store_true",
    help="forward the 'verbose' setting to unittest",
)
parser.add_argument(
    "-q", "--question",
    dest="question_num",
    type=int,
    choices=(1, 2, 3, 4),
    help="test a specific question only",
)
parser.add_argument(
    "-p", "--print-q4",
    dest="print_q4",
    action="store_true",
    help="print the path returned by your Q4 solution (skips tests)",
)
parser.add_argument(
    "-d", "--draw-q4",
    dest="draw_q4",
    action="store_true",
    help="draw the states returned by your Q4 solution (skips tests)",
)
parser.add_argument(
    "-e", "--explain-q4",
    dest="explain_q4",
    action="store_true",
    help="explain the path returned by your Q4 solution (skips tests)",
)
parser.add_argument(
    "-x", "--exhaustive-q4",
    dest="exhaustive_q4",
    action="store_true",
    help="test with ALL possible valid initial states for Q4 (overrides -i)",
)

# endregion
# ==================================================================== #
# region Driver Code


def main() -> None:
    """Main driver function.

    Parse command line options to configure and then run the unit tests.
    """
    args = parser.parse_args()

    initial_state: StateTuple = args.initial_state
    verbose: bool = args.verbose
    question_num: Optional[QuestionNum] = args.question_num

    print_q4: bool = args.print_q4
    draw_q4: bool = args.draw_q4
    explain_q4: bool = args.explain_q4
    exhaustive_q4: bool = args.exhaustive_q4

    if print_q4 or draw_q4 or explain_q4:
        complete_path = DFS_SOL(initial_state, [])
        if print_q4:
            _pretty_print_path(complete_path)
        if draw_q4:
            _draw_path(complete_path)
        if explain_q4:
            explainer = PathExplainer(complete_path)
            explainer.explain_path()
        return  # Skip tests.

    _run_unit_tests(verbose, question_num, initial_state, exhaustive_q4)


def _pretty_print_path(path: List[StateTuple]) -> None:
    for index, state in enumerate(path):
        abbreviated = abbreviate_state_tuple(state)
        print(f"{index}: {abbreviated}")


def _draw_path(path: List[StateTuple]) -> None:
    explainer = PathExplainer(path)
    for index, state in enumerate(path):
        state_drawing = explainer.draw_state(index)
        abbreviated_state = abbreviate_state_tuple(state)
        print(f"{index}: {state_drawing} {abbreviated_state}")


def _run_unit_tests(
    verbose: bool,
    question_num: Optional[QuestionNum],
    q4_initial_state: StateTuple,
    q4_try_all_initial_states: bool,
) -> None:
    """Start the unittest runtime.

    Note that we cannot just use `unittest.main()` since that parses
    command line arguments, interfering with our argparse CLI.
    Furthermore, we have a dynamic `TestCase` that cannot be discovered
    anyway as it needs to be created through a factory function.
    """
    test_suite_classes = _get_test_suite_classes(
        question_num,
        q4_initial_state,
        q4_try_all_initial_states,
    )

    loader = unittest.TestLoader()
    test_suites = [
        loader.loadTestsFromTestCase(cls) for cls in test_suite_classes
    ]
    all_tests_suite = unittest.TestSuite(test_suites)

    test_runner = unittest.TextTestRunner(verbosity=(2 if verbose else 1))
    test_runner.run(all_tests_suite)


def _get_test_suite_classes(
    question_num: Optional[QuestionNum],
    q4_initial_state: StateTuple,
    q4_try_all_initial_states: bool,
) -> List[Type[unittest.TestCase]]:
    static_test_suite_classes = [
        TestBFS,
        TestDFS,
        TestDFID,
        TestDFS_SOL,
    ]

    q4_initial_states: List[StateTuple]
    if q4_try_all_initial_states:
        q4_initial_states = [
            state for state in itertools.product((True, False), repeat=4)
            if check_valid_state(state)  # type: ignore
        ]
    else:
        q4_initial_states = [q4_initial_state]

    dynamic_test_suite_classes = [create_dynamic_DFS_SOL_tester(initial_state)
                                  for initial_state in q4_initial_states]

    test_suite_classes = static_test_suite_classes + dynamic_test_suite_classes

    # Return the test suite(s) for the specified question only.
    if question_num is not None:
        specific_test_suite = [test_suite_classes[question_num - 1]]
        if question_num == 4:
            return specific_test_suite + dynamic_test_suite_classes
        return specific_test_suite

    # Otherwise return ALL test suites.
    return test_suite_classes


# endregion

if __name__ == "__main__":
    main()
