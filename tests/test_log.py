from log import UserLog
from unittest.mock import patch
from unittest.mock import Mock


class TestLog:
    @patch("builtins.input", side_effect=["1"])
    def test_if_log_manager_return_log(self, input):

        ul = UserLog()
        ul.log = Mock(return_value="ul.log")

        assert ul.log_manager() == ul.log()
        del ul

    @patch("builtins.input", side_effect=["2"])
    def test_if_log_manager_return_new_user(self, input):

        ul = UserLog()
        ul.new_user = Mock(return_value="ul.new_user")

        assert ul.log_manager() == ul.new_user()
        del ul

    def test_log_with_correct_user_input(self, monkeypatch):
        name = "test"
        password = "test"
        answers = iter([name, password])

        ul = UserLog()
        monkeypatch.setattr("builtins.input", lambda value: next(answers))
        ul.log()

        assert ul.counter == 0

        del ul

    def test_log_with_incorrect_user_input(self, monkeypatch):
        name = "test"
        password = "test43423"
        password2 = "test"
        answers = iter([name, password, name, password, name, password2])

        ul = UserLog()
        monkeypatch.setattr("builtins.input", lambda value: next(answers))
        ul.log()

        assert ul.counter == 2

        del ul
