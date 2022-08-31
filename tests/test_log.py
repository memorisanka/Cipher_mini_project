from log import UserLog
from unittest.mock import patch
from unittest.mock import Mock


class TestLog:
    @patch("builtins.input", side_effect=["1", "2"])
    def test_log_manager(self, input):

        UserLog.log = Mock(return_value="log_test.log")
        m = UserLog()

        assert m.log_manager() == m.log()
        del m

        UserLog.new_user = Mock(return_value="log_test.new_user")
        m = UserLog()

        assert m.log_manager() == m.new_user()
        del m