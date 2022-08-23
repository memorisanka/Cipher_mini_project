from input_output_handler import InputOutputHandler
import unittest
from unittest.mock import patch


class TestsInputOutputHandler(unittest.TestCase):

    @patch('builtins.input', side_effect=["10", "20", "5"])
    def test_should_return_true_if_function_take_input_from_user(self, input):
        result = ""

        assert InputOutputHandler.read(result) == "10"
        assert InputOutputHandler.read(result) == "20"
        assert InputOutputHandler.read(result) == "5"
