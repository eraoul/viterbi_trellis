import unittest
from viterbi import ViterbiTrellis


class MyTestCase(unittest.TestCase):
    def test_int_states(self):
        v = ViterbiTrellis([[3, 2, 1], [3, 4]], lambda x: x, lambda x, y: abs(y - x))
        best_path = v.viterbi_best_path()
        self.assertEqual(best_path, [2, 0])


if __name__ == '__main__':
    unittest.main()
