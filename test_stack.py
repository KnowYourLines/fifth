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
    def test_pushes_and_pops_stack(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\nstack is []\nstack is [5]\nstack is []\n')

    @patch('builtins.input', side_effect=["PUSH 3", "POP 3", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_only_push_takes_integer_argument(self, stdout, mock_input):
        fifth()
        self.assertEqual(stdout.getvalue(), 'stack is []\nstack is [3]\nERROR\n')

if __name__ == '__main__':
    unittest.main()
