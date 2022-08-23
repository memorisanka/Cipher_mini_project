from input_output_handler import InputOutputHandler
import unittest
from unittest.mock import patch, call


class TestsInputOutputHandler(unittest.TestCase):
    """Tests for Input Output Handler"""

    @patch('builtins.input', side_effect=["10", "20", "5"])
    def test_io_read_method(self, input):
        """Test for method IO read."""

        result = ""

        assert InputOutputHandler.read(result) == "10"
        assert InputOutputHandler.read(result) == "20"
        assert InputOutputHandler.read(result) == "5"

    @patch("builtins.print")
    def test_io_print(self, mocked_print):
        """Test for method IO print_text."""
        print("test1")
        print("test2")

        assert mocked_print.mock_calls == [call("test1"), call("test2")]


