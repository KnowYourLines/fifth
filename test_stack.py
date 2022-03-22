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
        self.assertEqual(stdout.getvalue(), 'stack is []\nERROR\nstack is []\n')


if __name__ == '__main__':
    unittest.main()
