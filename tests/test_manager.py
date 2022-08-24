import unittest
from manager import Manager


class TestsManager(unittest.TestCase):

    def setUp(self) -> None:
        manager = Manager()

    def test_handle_instruction(self):
        manager = Manager()
        user_text = "2"
        instruction = manager.__handle_instruction(user_text)
        self.assertEqual(instruction, None)
