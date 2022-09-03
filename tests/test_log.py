from log import UserLog
from unittest.mock import patch
from unittest.mock import Mock


class TestLog:
    @patch("builtins.input", side_effect=["1", "2"])
    def test_log_manager(self, input):
        """If the input is 1, function should return UserLog.log(),
        if the input is 2, function should return UserLog.new_user()"""

        UserLog.log = Mock(return_value="log_test.log")
        ul = UserLog()

        assert ul.log_manager() == ul.log()
        del ul

        UserLog.new_user = Mock(return_value="log_test.new_user")
        ul = UserLog()

        assert ul.log_manager() == ul.new_user()
        del ul

