import unittest
from code_base_EP1 import verifica_validade, vars, ListTree

P,Q,R = vars('P', 'Q', 'R')

tests = [
        {
            'function': verifica_validade,
            'input': [((P >> Q) >> (~P | Q), False)],
            'output': None
        }
        ]

class TestValidade(unittest.TestCase):
    def test_validade(self):
        for test in tests:
            function = test['function']
        input_val = test['input']
        expected_output = test['output']
        actual_output = function(input_val, dict(), dict(), ListTree().add_child(', '.join(str(c[0]) for c in input_val)))
        self.assertEqual(expected_output, actual_output[0])

if __name__ == '__main__':
    unittest.main()
