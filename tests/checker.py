from code_base_EP1 import verify_valid, vars, Iff
import unittest

P, Q, R = vars('P', 'Q', 'R')

class TestValidade(unittest.TestCase):
    def test_validos(self):
        test_input = (P >> Q) >> (~P | Q)
        expected_output = None
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output)

        test_input = Iff(P >> Q, ~P | Q)
        expected_output = None
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_satisfazivel(self):
        test_input = (P | Q)
        expected_output = {'P': False, 'Q': False}
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output)

        test_input = P >> Q >> R
        expected_output = {'P': False, 'Q': True, 'R': False}
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_insatisfazivel(self):
        test_input = (P & ~P)
        expected_output = {'P': False}
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
