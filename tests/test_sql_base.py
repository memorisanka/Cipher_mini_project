import unittest
from sql_base import DataBase


class TestDataBase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = DataBase()
        self.db.create_base()
        self.db.add_user("test", "test")

    def test_check_user(self) -> None:
        """Test user_check - return True if user exists in database, and False in opposite case"""

        assert (self.db.check_user("test", "test")) is True
        assert (self.db.check_user("test2", "test2")) is False

    def test_check_username(self) -> None:
        """Test username_check - return username if username exists in the database"""

        assert (self.db.check_username("test")) == "test"
        assert (self.db.check_username("test3")) is None

    def tearDown(self) -> None:
        del self.db
