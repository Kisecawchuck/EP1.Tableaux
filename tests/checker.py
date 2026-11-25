from code_base_EP1 import *
import unittest

P, Q, R = vars('P', 'Q', 'R')

class TestValidade(unittest.TestCase):
    def test_modus_ponens(self):
        test_input = ArgumentForm(
                P, P >> Q,    #premises
                conclusion = Q
                )
        expected_output = True # expressão é válida
        actual_output = verificar_sequente(test_input.premises, test_input.conclusion)
        mostra_resultado(actual_output)
        self.assertEqual(expected_output, actual_output["valido"])

    def test_modus_tollens(self):
        test_input = ArgumentForm(
                P >> Q, ~Q,   #premises
                conclusion = ~P
                )
        expected_output = True
        actual_output = verificar_sequente(test_input.premises, test_input.conclusion)
        mostra_resultado(actual_output)
        self.assertEqual(expected_output, actual_output["valido"])

    def test_disjunctive_syllogism(self):
        test_input = ArgumentForm(
                P | Q, ~P,    #premises
                conclusion = Q
                )
        expected_output = True
        actual_output = verificar_sequente(test_input.premises, test_input.conclusion)
        mostra_resultado(actual_output)
        self.assertEqual(expected_output, actual_output["valido"])

    def test_hypothetical_syllogism(self):
        test_input = ArgumentForm(
                P >> Q, Q >> R,   #premises
                conclusion = R
                )
        expected_output = False
        actual_output = verificar_sequente(test_input.premises, test_input.conclusion)
        mostra_resultado(actual_output)
        self.assertEqual(expected_output, actual_output["valido"])

    def test_non_sequitur(self):
        test_input = ArgumentForm(
                P,        #premises
                conclusion = Q
                )
        expected_output = False
        actual_output = verificar_sequente(test_input.premises, test_input.conclusion)
        mostra_resultado(actual_output)
        self.assertEqual(expected_output, actual_output["valido"])

    def test_affirming_the_consequent(self):
        test_input = ArgumentForm(
                P >> Q, Q,    #premises
                conclusion = P
                )
        expected_output = False
        actual_output = verificar_sequente(test_input.premises, test_input.conclusion)
        mostra_resultado(actual_output)
        self.assertEqual(expected_output, actual_output["valido"])


if __name__ == '__main__':
    unittest.main()
