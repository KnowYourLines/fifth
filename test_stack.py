import unittest
from io import StringIO
from unittest.mock import patch

from stack import fifth


class FifthTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=["END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_initial_stack(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\n')

    @patch('builtins.input', side_effect=["notavalidcommand", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_must_be_valid_command(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 3", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_push_to_stack(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\n')

    @patch('builtins.input', side_effect=["PUSH 3", "PUSH 5", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_push_multiple_values(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\nstack is [3, 5]\n')

    @patch('builtins.input', side_effect=["PUSH 3.2", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_push_must_be_integer(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 3 PUSH 5", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_push_one_value_at_a_time(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 3", "PUSH 5", "POP", "POP", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_pops_from_stack(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\nstack is [3, 5]\nstack is [3]\nstack is []\n')

    @patch('builtins.input', side_effect=["PUSH 3",  "POP", "PUSH 5", "POP", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_commands_applied_in_sequence(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\nstack is []\nstack is [5]\nstack is []\n')

    @patch('builtins.input', side_effect=["PUSH 3", "POP 3", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_only_push_takes_integer_argument(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 8", "PUSH 1", "PUSH 3", "SWAP", "PUSH 5",  "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_swaps_top_2_elements(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [8]\nstack is [8, 1]\nstack is [8, 1, 3]\nstack is [8, 3, 1]\nstack is [8, 3, 1, 5]\n')

    @patch('builtins.input', side_effect=["PUSH 8", "PUSH 1", "DUP",  "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_duplicates_last_element(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [8]\nstack is [8, 1]\nstack is [8, 1, 1]\n')

    @patch('builtins.input', side_effect=["PUSH 8", "PUSH 1", "+", "PUSH 1", "+", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [8]\nstack is [8, 1]\nstack is [9]\nstack is [9, 1]\nstack is [10]\n')

    @patch('builtins.input', side_effect=["PUSH 8", "PUSH 2", "*", "PUSH 2", "*", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [8]\nstack is [8, 2]\nstack is [16]\nstack is [16, 2]\nstack is [32]\n')

    @patch('builtins.input', side_effect=["PUSH 2", "PUSH 8", "-", "PUSH 2", "*", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtracts_bottom_from_top_of_stack(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nstack is [2, 8]\nstack is [-6]\nstack is [-6, 2]\nstack is [-12]\n')

    @patch('builtins.input', side_effect=["PUSH 8", "PUSH 2", "/", "PUSH 2", "/", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divides_bottom_from_top_of_stack(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [8]\nstack is [8, 2]\nstack is [4]\nstack is [4, 2]\nstack is [2]\n')

    @patch('builtins.input', side_effect=["PUSH 2", "PUSH 8", "/", "PUSH 6", "+", "PUSH 8", "/",  "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_rounds_down(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nstack is [2, 8]\nstack is [0]\nstack is [0, 6]\nstack is [6]\nstack is [6, 8]\nstack is [0]\n')

    @patch('builtins.input', side_effect=["PUSH 2", "+"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition_needs_2_elements(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 2", "-"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction_needs_2_elements(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 2", "*"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication_needs_2_elements(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 2", "/"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_needs_2_elements(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nERROR\n')

    @patch('builtins.input', side_effect=["PUSH 2", "SWAP"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_swap_needs_2_elements(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nstack is [2]\nERROR\n')

    @patch('builtins.input', side_effect=["POP"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_pop_needs_element(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nERROR\n')

    @patch('builtins.input', side_effect=["DUP"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_dup_needs_element(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(),
                         'stack is []\nERROR\n')


if __name__ == '__main__':
    unittest.main()
