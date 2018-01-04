import unittest
from .viterbi import ViterbiTrellis
from .viterbi_exceptions import ViterbiTrellisEmptyLayerException


class MyTestCase(unittest.TestCase):
    def test_int_states(self):
        # Note that layer elements in the test trellis here aren't sorted
        # numerically, in order to have a more interesting result path.
        v = ViterbiTrellis([[2, 6, 4], [4, 6], [0, 2, 6]],
                           lambda x: x / 2.0,
                           lambda x, y: abs(y - x))
        best_path = v.viterbi_best_path()
        self.assertEqual(best_path, [2, 0, 1])

    def test_int_states_no_state_cost(self):
        # Note that layer elements in the test trellis here aren't sorted
        # numerically, in order to have a more interesting result path.
        v = ViterbiTrellis([[2, 6, 4], [4, 6], [0, 2, 6]],
                           lambda x: 0,
                           lambda x, y: abs(y - x))
        best_path = v.viterbi_best_path()
        self.assertEqual(best_path, [1, 1, 2])

    def test_empty_trellis(self):
        v = ViterbiTrellis([], lambda x: x, lambda x, y: y)
        best_path = v.viterbi_best_path()
        self.assertEqual(best_path, [])

    def test_empty_trellis_layer(self):
        v = ViterbiTrellis([[2, 6, 4], [], [0, 2, 6]],
                           lambda x: x,
                           lambda x, y: y)
        with self.assertRaises(ViterbiTrellisEmptyLayerException):
            v.viterbi_best_path()


if __name__ == '__main__':
    unittest.main()
