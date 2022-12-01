import unittest
from reverse.reverse_number import reverse_number


class TestReverseNumber(unittest.TestCase):
    def test_reverse_number(self) -> None:
        self.assertEqual(reverse_number(12), 21)


unittest.main()
