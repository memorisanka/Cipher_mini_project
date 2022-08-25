from input_output_handler import InputOutputHandler as io
from io import StringIO


class TestIO:
    def test_io_print_text(self, capsys):
        """Test for io.print_text() should print each text in new line."""

        io.print_text("test1", "test2")
        out, err = capsys.readouterr()

        assert out == "test1\ntest2\n"

    def test_io_read(self, monkeypatch):
        """Test for io.read should get text from user."""

        number_inputs = StringIO("test")
        monkeypatch.setattr('sys.stdin', number_inputs)

        assert io.read(number_inputs) == "test"

