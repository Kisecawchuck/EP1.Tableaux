from code_base_EP1 import verify_valid, vars
import unittest

P,Q = vars('P', 'Q')

class TestValidade(unittest.TestCase):
    def test_validos(self):
        test_input = (P >> Q) >> (~P | Q)
        expected_output = None
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output[0])
    def test_satisfazivel(self):
        test_input = P | Q
        expected_output = {'P': False, 'Q': False}
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output[0])
    def test_insatisfazivel(self):
        test_input = P & ~P
        expected_output = {'P': False}
        actual_output = verify_valid(test_input)
        self.assertEqual(expected_output, actual_output[0])

if __name__ == '__main__':
    unittest.main()
