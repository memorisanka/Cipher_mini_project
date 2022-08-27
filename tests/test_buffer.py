from buffer import Buffer


class TestBuffer:

    def setup(self):
        self.test_buffer = Buffer()

    def test_add_to_buffer(self):
        """Should add record to buffer."""

        self.test_buffer.add({"Test": "test"})
        assert self.test_buffer.__len__() == 1

        self.test_buffer.add({"Test1": "test1"})
        assert self.test_buffer.__len__() == 2

        self.test_buffer.add({"Test1": "test_test"})
        assert self.test_buffer.__len__() == 3

        self.test_buffer.add({"Test": "test_test_test"})
        assert self.test_buffer.__len__() == 4

    def test_peak_buffer(self):
        """Should return buffer_dict's content."""

        assert self.test_buffer.peak() == {
            "Test": ["test", "test_test_test"],
            "Test1": ["test1", "test_test"],
        }
