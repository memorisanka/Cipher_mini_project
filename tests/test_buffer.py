from buffer import Buffer


class TestBuffer:

    def setup(self):
        self.test_buffer = Buffer()

    def test_add_to_buffer(self):
        """Test should add record to buffer."""

        self.test_buffer.add({"Test": "test"})
        assert self.test_buffer.__len__() == 1

        self.test_buffer.add({"Test1": "test1"})
        assert self.test_buffer.__len__() == 2