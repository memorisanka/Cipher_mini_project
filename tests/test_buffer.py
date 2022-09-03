from buffer import Buffer


class TestBuffer:
    def test_add_to_buffer(self):
        """Should add record to buffer."""
        self.test_buffer = Buffer()
        self.test_buffer.add({"Test": "test"})
        assert self.test_buffer.__len__() == 1

        self.test_buffer.add({"Test1": "test1"})
        assert self.test_buffer.__len__() == 2

        self.test_buffer.add({"Test1": "test_test"})
        assert self.test_buffer.__len__() == 3

        self.test_buffer.add({"Test": "test_test_test"})
        assert self.test_buffer.__len__() == 4
        self.test_buffer.clear()

    def test_peak_buffer(self, capsys):
        """Should create dictionary from buffer and return its content."""

        self.test_buffer = Buffer()
        self.test_buffer.add({"Test": "test"})
        self.test_buffer.peak()
        out, err = capsys.readouterr()
        assert out == "{'Test': ['test']}\n"

        self.test_buffer.clear()
